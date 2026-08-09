import fitz  # PyMuPDF
import sqlite3
import os
import uuid
import hashlib

# Usa percorsi assoluti basati sulla cartella corrente per sicurezza
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "courses", "software-engineering", ".derived", "fragments.db")
SOURCES_DIR = os.path.join(BASE_DIR, "courses", "software-engineering", "sources")
ASSETS_DIR = os.path.join(BASE_DIR, "courses", "software-engineering", "assets")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # DROP delle tabelle per permettere re-run sicuri
    cursor.execute('DROP TABLE IF EXISTS fragments')
    cursor.execute('DROP TABLE IF EXISTS assets')
    
    cursor.execute('''
    CREATE TABLE fragments (
        id TEXT PRIMARY KEY,
        source_id TEXT,
        source_file TEXT,
        page_num INTEGER,
        block_id TEXT,
        content TEXT,
        bbox TEXT,
        block_order INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE assets (
        id TEXT PRIMARY KEY,
        source_id TEXT,
        source_file TEXT,
        page_num INTEGER,
        file_path TEXT,
        bbox TEXT,
        asset_type TEXT,
        width INTEGER,
        height INTEGER,
        aspect_ratio REAL,
        image_hash TEXT,
        classification TEXT,
        excluded_from_candidates BOOLEAN
    )
    ''')
    
    conn.commit()
    return conn

def ingest_pdfs(conn):
    cursor = conn.cursor()
    
    if not os.path.exists(SOURCES_DIR):
        print(f"Error: Directory {SOURCES_DIR} not found.")
        return
        
    for root, _, files in os.walk(SOURCES_DIR):
        for filename in files:
            if not filename.lower().endswith(".pdf"):
                continue
                
            file_path = os.path.join(root, filename)
            # source_file sarà il path relativo a SOURCES_DIR
            rel_source_file = os.path.relpath(file_path, SOURCES_DIR)
            source_id = hashlib.md5(rel_source_file.encode()).hexdigest()[:8]
            
            print(f"Processing {rel_source_file}...")
            try:
                doc = fitz.open(file_path)
            except Exception as e:
                print(f"Failed to open {filename}: {e}")
                continue
                
            for page_num, page in enumerate(doc):
                # 1. Estrarre il testo blocco per blocco (provenance esatta)
                blocks = page.get_text("blocks")
                for block_order, block in enumerate(blocks):
                    # formati block PyMuPDF: (x0, y0, x1, y1, "text", block_no, block_type)
                    x0, y0, x1, y1, text, block_no, block_type = block
                    bbox = f"{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}"
                    
                    if block_type == 0:  # 0 significa testo
                        text_content = text.strip()
                        if not text_content: 
                            continue
                        
                        frag_id = str(uuid.uuid4())
                        block_id = f"b{block_no}"
                        cursor.execute('''
                            INSERT INTO fragments (id, source_id, source_file, page_num, block_id, content, bbox, block_order)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (frag_id, source_id, rel_source_file, page_num, block_id, text_content, bbox, block_order))
                
                # 2. Estrarre immagini embedded
                image_list = page.get_images(full=True)
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    try:
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        
                        asset_id = str(uuid.uuid4())
                        asset_filename = f"{source_id}_p{page_num}_i{img_index}.{image_ext}"
                        asset_path = os.path.join(ASSETS_DIR, asset_filename)
                        
                        with open(asset_path, "wb") as f:
                            f.write(image_bytes)
                            
                        image_hash = hashlib.md5(image_bytes).hexdigest()
                        
                        width = base_image.get("width", 0)
                        height = base_image.get("height", 0)
                        aspect_ratio = (width / height) if height > 0 else 0.0
                        
                        cursor.execute('''
                            INSERT INTO assets (id, source_id, source_file, page_num, file_path, bbox, asset_type, width, height, aspect_ratio, image_hash, classification, excluded_from_candidates)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (asset_id, source_id, rel_source_file, page_num, asset_filename, None, "embedded_image", width, height, aspect_ratio, image_hash, "uncertain", 0))
                    except Exception as e:
                        print(f"Error extracting image {xref} on page {page_num}: {e}")
                        
                # 3. Mappare i vettoriali (vector graphics) per estrazione manuale / crop successivo
                drawings = page.get_drawings()
                if drawings:
                    rect = page.rect
                    bbox = f"{rect.x0:.1f},{rect.y0:.1f},{rect.x1:.1f},{rect.y1:.1f}"
                    asset_id = str(uuid.uuid4())
                    cursor.execute('''
                        INSERT INTO assets (id, source_id, source_file, page_num, file_path, bbox, asset_type, width, height, aspect_ratio, image_hash, classification, excluded_from_candidates)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (asset_id, source_id, rel_source_file, page_num, "VIRTUAL_RENDER_REQUIRED", bbox, "vector_diagram_region", 0, 0, 0.0, None, "uncertain", 0))

    conn.commit()
    
    print("Running post-processing asset classification...")
    # 4. Post-processing: Compute repetition per document and classify
    cursor.execute("SELECT DISTINCT source_id FROM assets")
    source_ids = [row[0] for row in cursor.fetchall()]
    
    for sid in source_ids:
        # Get total pages for this source
        cursor.execute("SELECT MAX(page_num) FROM fragments WHERE source_id = ?", (sid,))
        max_page = cursor.fetchone()[0]
        total_pages = (max_page + 1) if max_page is not None else 1
        
        # Get image hashes and count pages they appear on
        cursor.execute('''
            SELECT image_hash, COUNT(DISTINCT page_num) as page_count
            FROM assets 
            WHERE source_id = ? AND image_hash IS NOT NULL
            GROUP BY image_hash
        ''', (sid,))
        
        for row in cursor.fetchall():
            img_hash = row[0]
            page_count = row[1]
            
            # Find all assets with this hash in this document
            cursor.execute('''
                SELECT id, width, height, aspect_ratio 
                FROM assets 
                WHERE source_id = ? AND image_hash = ?
            ''', (sid, img_hash))
            
            assets_to_update = cursor.fetchall()
            for asset_row in assets_to_update:
                asset_id = asset_row[0]
                width = asset_row[1]
                height = asset_row[2]
                aspect_ratio = asset_row[3]
                
                decorative_score = 0
                
                # Rule 1: High repetition (>25% of pages)
                if (page_count / total_pages) > 0.25:
                    decorative_score += 3
                
                # Rule 2: Geometric heuristics
                if width > 0 and height > 0:
                    if width < 150 or height < 150:
                        decorative_score += 1
                    if aspect_ratio > 3.5 or aspect_ratio < 0.28:
                        decorative_score += 1
                        
                if decorative_score >= 3:
                    classification = 'likely_decorative'
                    excluded = 1
                else:
                    classification = 'uncertain'
                    excluded = 0
                    
                cursor.execute('''
                    UPDATE assets 
                    SET classification = ?, excluded_from_candidates = ?
                    WHERE id = ?
                ''', (classification, excluded, asset_id))

    conn.commit()
    print("Ingestion complete!")

if __name__ == "__main__":
    conn = init_db()
    ingest_pdfs(conn)
    conn.close()
