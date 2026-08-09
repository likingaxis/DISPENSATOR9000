import os
import yaml
import sqlite3
import argparse
from typing import List, Dict, Any

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    BM25Okapi = None

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COURSE_DIR = os.path.join(BASE_DIR, "courses", "software-engineering")
DB_PATH = os.path.join(COURSE_DIR, ".derived", "fragments.db")
COURSE_YAML_PATH = os.path.join(COURSE_DIR, "course-model", "course.yaml")
REGISTRY_PATH = os.path.join(COURSE_DIR, "course-model", "source-registry.yaml")
OUT_DIR = os.path.join(COURSE_DIR, "runtime", "topic-context")

def load_yaml(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_source_map(registry_data: List[Dict]) -> Dict[str, str]:
    return {item['id']: item['file'] for item in registry_data}

def find_topic(course_data: Dict, topic_id: str) -> Dict:
    for chapter in course_data.get('chapters', []):
        for topic in chapter.get('topics', []):
            if topic['id'] == topic_id:
                return topic
    return None

def fetch_primary_evidence(cursor, topic: Dict, source_map: Dict[str, str]) -> List[Dict]:
    evidence = []
    for official in topic.get('official_sources', []):
        source_id = official['source_id']
        file_path = source_map.get(source_id)
        if file_path:
            file_path = file_path.replace('/', '\\')
        if not file_path:
            continue
            
        ranges = official.get('page_ranges', [])
        for r in ranges:
            start_page, end_page = r[0], r[1]
            cursor.execute('''
                SELECT page_num, block_id, content, bbox
                FROM fragments
                WHERE source_file = ? AND page_num >= ? AND page_num <= ?
                ORDER BY page_num, block_order
            ''', (file_path, start_page, end_page))
            
            for row in cursor.fetchall():
                evidence.append({
                    'source_id': source_id,
                    'file': file_path,
                    'page': row[0],
                    'block_id': row[1],
                    'content': row[2],
                    'bbox': row[3],
                    'is_primary': True
                })
    return evidence

def fetch_secondary_evidence(cursor, topic: Dict, source_map: Dict[str, str], top_k: int = 10) -> List[Dict]:
    evidence = []
    query_parts = [topic.get('title', '')] + topic.get('aliases', []) + topic.get('concepts', [])
    query = " ".join(query_parts).lower().split()
    
    if not BM25Okapi:
        print("BM25 non installato. Skipping secondary sources.")
        return []

    for source_id in topic.get('secondary_sources', []):
        file_path = source_map.get(source_id)
        if file_path:
            file_path = file_path.replace('/', '\\')
        if not file_path:
            continue
            
        # Fetch all fragments for this source
        cursor.execute('''
            SELECT id, page_num, block_order, content
            FROM fragments
            WHERE source_file = ?
            ORDER BY page_num, block_order
        ''', (file_path,))
        rows = cursor.fetchall()
        
        if not rows:
            continue
            
        # Prepare corpus for BM25
        corpus = [row[3].lower().split() for row in rows]
        bm25 = BM25Okapi(corpus)
        scores = bm25.get_scores(query)
        
        # Get top K indices
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        
        # For each top fragment, fetch neighbor context on the same page
        for idx in top_indices:
            if scores[idx] <= 0:
                continue # Skip zero matches
                
            main_frag = rows[idx]
            page_num = main_frag[1]
            main_block_order = main_frag[2]
            
            # Fetch neighbor context: -1 and +1 on the SAME page
            cursor.execute('''
                SELECT block_id, content, block_order, bbox
                FROM fragments
                WHERE source_file = ? AND page_num = ? 
                  AND (block_order = ? OR block_order = ? OR block_order = ?)
                ORDER BY block_order
            ''', (file_path, page_num, main_block_order - 1, main_block_order, main_block_order + 1))
            
            combined_content = []
            block_ids = []
            bbox_list = []
            
            for crow in cursor.fetchall():
                block_ids.append(crow[0])
                combined_content.append(crow[1])
                bbox_list.append(crow[3])
                
            evidence.append({
                'source_id': source_id,
                'file': file_path,
                'page': page_num,
                'block_ids': block_ids,
                'content': "\n".join(combined_content),
                'bboxes': bbox_list,
                'is_primary': False,
                'bm25_score': scores[idx]
            })
            
    return evidence

def fetch_assets(cursor, topic: Dict, source_map: Dict[str, str]) -> List[Dict]:
    assets = []
    for official in topic.get('official_sources', []):
        source_id = official['source_id']
        file_path = source_map.get(source_id)
        if file_path:
            file_path = file_path.replace('/', '\\')
        if not file_path:
            continue
            
        ranges = official.get('page_ranges', [])
        for r in ranges:
            start_page, end_page = r[0], r[1]
            cursor.execute('''
                SELECT id, page_num, file_path, asset_type
                FROM assets
                WHERE source_file = ? AND page_num >= ? AND page_num <= ?
            ''', (file_path, start_page, end_page))
            
            for row in cursor.fetchall():
                assets.append({
                    'asset_id': row[0],
                    'source_id': source_id,
                    'page': row[1],
                    'path': row[2],
                    'type': row[3]
                })
    return assets

def estimate_tokens(text: str) -> int:
    # A very rough heuristic: ~4 chars per token
    return len(text) // 4

def generate_topic_context(topic_id: str):
    print(f"Generating context for topic: {topic_id}")
    os.makedirs(OUT_DIR, exist_ok=True)
    
    course_data = load_yaml(COURSE_YAML_PATH)
    registry_data = load_yaml(REGISTRY_PATH)
    source_map = get_source_map(registry_data)
    
    topic = find_topic(course_data, topic_id)
    if not topic:
        print(f"Topic {topic_id} not found.")
        return
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    primary = fetch_primary_evidence(cursor, topic, source_map)
    secondary = fetch_secondary_evidence(cursor, topic, source_map, top_k=10)
    assets = fetch_assets(cursor, topic, source_map)
    
    conn.close()
    
    # Stats
    primary_text = "\n".join([p['content'] for p in primary])
    secondary_text = "\n".join([s['content'] for s in secondary])
    total_tokens = estimate_tokens(primary_text) + estimate_tokens(secondary_text)
    
    out_file = os.path.join(OUT_DIR, f"{topic_id}.md")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"# Topic Context\n\n")
        f.write(f"**topic_id**: {topic_id}\n")
        f.write(f"**title**: {topic.get('title')}\n\n")
        
        f.write("## Retrieval Metadata\n")
        f.write(f"- Primary fragments: {len(primary)}\n")
        f.write(f"- Secondary fragments: {len(secondary)}\n")
        f.write(f"- Visual assets candidate: {len(assets)}\n")
        f.write(f"- Estimated context tokens: ~{total_tokens}\n\n")
        
        f.write("## 1. Primary Evidence (Official Coverage)\n\n")
        if not primary:
            f.write("*No primary evidence found.*\n\n")
        else:
            # Group by source_id and page
            current_source = None
            current_page = -1
            for p in primary:
                if p['source_id'] != current_source:
                    current_source = p['source_id']
                    f.write(f"### Source: {current_source} (`{p['file']}`)\n")
                if p['page'] != current_page:
                    current_page = p['page']
                    f.write(f"#### Page {current_page}\n")
                
                f.write(f"> {p['content'].replace(chr(10), ' ')}\n\n")
                
        f.write("## 2. Secondary Evidence (BM25 Lexical + Concepts)\n\n")
        if not secondary:
            f.write("*No secondary evidence found.*\n\n")
        else:
            # Sort secondary by source and score
            secondary.sort(key=lambda x: (x['source_id'], -x['bm25_score']))
            current_source = None
            for s in secondary:
                if s['source_id'] != current_source:
                    current_source = s['source_id']
                    f.write(f"### Source: {current_source} (`{s['file']}`)\n")
                f.write(f"#### Page {s['page']} (BM25: {s['bm25_score']:.2f})\n")
                f.write(f"> {s['content'].replace(chr(10), ' ')}\n\n")
                
        f.write("## 3. Visual Assets Candidates\n\n")
        if not assets:
            f.write("*No visual assets found.*\n\n")
        else:
            for a in assets:
                f.write(f"- **asset_id**: {a['asset_id']}\n")
                f.write(f"  source: {a['source_id']}\n")
                f.write(f"  page: {a['page']}\n")
                f.write(f"  type: {a['type']}\n")
                f.write(f"  path: `{a['path']}`\n\n")
                
    print(f"Context written to {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_id", help="The topic ID to generate context for")
    args = parser.parse_args()
    generate_topic_context(args.topic_id)
