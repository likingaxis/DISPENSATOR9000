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
        asset_type TEXT
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
                        
                        cursor.execute('''
                            INSERT INTO assets (id, source_id, source_file, page_num, file_path, bbox, asset_type)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', (asset_id, source_id, rel_source_file, page_num, asset_filename, None, "embedded_image"))
                    except Exception as e:
                        print(f"Error extracting image {xref} on page {page_num}: {e}")
                        
                # 3. Mappare i vettoriali (vector graphics) per estrazione manuale / crop successivo
                drawings = page.get_drawings()
                if drawings:
                    rect = page.rect
                    bbox = f"{rect.x0:.1f},{rect.y0:.1f},{rect.x1:.1f},{rect.y1:.1f}"
                    asset_id = str(uuid.uuid4())
                    cursor.execute('''
                        INSERT INTO assets (id, source_id, source_file, page_num, file_path, bbox, asset_type)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (asset_id, source_id, rel_source_file, page_num, "VIRTUAL_RENDER_REQUIRED", bbox, "vector_diagram_region"))

    conn.commit()
    print("Ingestion complete!")

if __name__ == "__main__":
    conn = init_db()
    ingest_pdfs(conn)
    conn.close()
