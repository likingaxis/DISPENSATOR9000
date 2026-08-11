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
    
    # Load new files for Patch 8A/8B
    backbone_map_path = os.path.join(COURSE_DIR, 'course-model', 'editorial-backbone-map.yaml')
    parsed_backbone_path = os.path.join(COURSE_DIR, 'course-model', 'parsed-backbone.yaml')
    exam_intelligence_path = os.path.join(COURSE_DIR, 'course-model', 'exam-intelligence.yaml')
    
    backbone_map = load_yaml(backbone_map_path) if os.path.exists(backbone_map_path) else {}
    parsed_backbone = load_yaml(parsed_backbone_path) if os.path.exists(parsed_backbone_path) else {}
    exam_intelligence = load_yaml(exam_intelligence_path) if os.path.exists(exam_intelligence_path) else {}
    
    # 1. Editorial Backbone
    backbone_secs = []
    topic_block_ids = set()
    
    if topic_id in backbone_map.get('topics', {}):
        sec_ids = backbone_map['topics'][topic_id].get('backbone_sections', [])
        for s_id in sec_ids:
            for sec in parsed_backbone.get('sections', []):
                if sec['section_id'] == s_id:
                    backbone_secs.append(sec)
                    for block in sec.get('blocks', []):
                        topic_block_ids.add(block['block_id'])
                    break
                    
    # Patch 10A: Curated Backbone Images as Candidates
    for vb in parsed_backbone.get('visual_bindings', []):
        after_block = vb.get('original_placement', {}).get('after_block')
        before_block = vb.get('original_placement', {}).get('before_block')
        
        if (after_block and after_block in topic_block_ids) or (before_block and before_block in topic_block_ids):
            obsidian_path = vb.get('obsidian_path')
            # Check if file exists
            if obsidian_path and os.path.exists(os.path.join(COURSE_DIR, obsidian_path)):
                candidate = {
                    'asset_id': vb.get('asset_id'),
                    'obsidian_path': obsidian_path,
                    'asset_type': 'curated_backbone_image',
                    'provenance': {
                        'source_type': 'editorial_backbone',
                        'source_id': 'notes-90'
                    },
                    'curation': {
                        'explicitly_embedded': True
                    },
                    'original_binding': vb.get('original_placement', {})
                }
                
                # Try to associate with a concept if we had that mapping logic, 
                # but for now we just append to the topic's global candidate pool
                assets.append(candidate)
                    
    # 2. Split Secondary Evidence
    lecture_expansion = [s for s in secondary if s['source_id'] == 'theory-summary']
    condensed_ref = [s for s in secondary if s['source_id'] == 'isw1-summary']
    
    # 3. Exam Intelligence
    exam = exam_intelligence.get('concepts', {}).get(topic_id, {})
    
    output = {
        'topic_id': topic_id,
        'title': topic.get('title'),
        'editorial_backbone': {
            'source': 'notes-90',
            'sections': backbone_secs
        },
        'lecture_expansion': {
            'source': 'lecture-166',
            'evidence': lecture_expansion
        },
        'condensed_reference': {
            'source': 'notes-50',
            'evidence': condensed_ref
        },
        'official_course_evidence': {
            'source': 'slides',
            'evidence': primary
        },
        'exam_intelligence': exam,
        'visual_assets_candidates': assets
    }
    
    out_file = os.path.join(OUT_DIR, f"{topic_id}.yaml")
    with open(out_file, 'w', encoding='utf-8') as f:
        yaml.dump(output, f, sort_keys=False, allow_unicode=True)
                
    print(f"Context written to {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_id", help="The topic ID to generate context for")
    args = parser.parse_args()
    generate_topic_context(args.topic_id)
