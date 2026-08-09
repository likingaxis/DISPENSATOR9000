import argparse
import os
import sys
import yaml
import shutil
import sqlite3
from datetime import datetime

# Usa percorsi assoluti basati sulla cartella corrente per sicurezza
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COURSE_DIR = os.path.join(BASE_DIR, "courses", "software-engineering")
RUNS_DIR = os.path.join(COURSE_DIR, "runtime", "runs")
CHAPTER_RUNS_DIR = os.path.join(COURSE_DIR, "runtime", "chapter-runs")
CHAPTER_DRAFTS_DIR = os.path.join(COURSE_DIR, "runtime", "chapter-drafts")
CANONICAL_DIR = os.path.join(COURSE_DIR, "canonical")
DRAFTS_DIR = os.path.join(COURSE_DIR, ".derived", "drafts")
PROMPTS_DIR = os.path.join(BASE_DIR, "system", "prompts")
DB_PATH = os.path.join(COURSE_DIR, ".derived", "fragments.db")

sys.path.append(os.path.dirname(__file__))
import retriever

def wait_for_user(step_name, input_file, output_file, extra_message=""):
    print(f"\n{'='*70}")
    print(f"AZIONE RICHIESTA: {step_name}")
    print(f"{'='*70}")
    if extra_message:
        print(extra_message)
    print(f"1. APRI questo file e COPIA tutto il suo contenuto:")
    print(f"   -> {input_file}")
    print(f"2. INCOLLA il testo nella chat del tuo LLM (es. Opus/Claude).")
    print(f"3. COPIA la risposta generata dall'LLM.")
    print(f"4. INCOLLA e SALVA la risposta in questo file:")
    print(f"   -> {output_file}")
    print(f"{'-'*70}")
    input("PREMI INVIO qui sotto *SOLO DOPO* aver salvato il file...")

def clean_yaml_file(yaml_path):
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if content.strip().startswith("```"):
            lines = content.strip().split('\n')
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].startswith("```"):
                lines = lines[:-1]
            content = '\n'.join(lines)
            with open(yaml_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return yaml.safe_load(content)
    except Exception as e:
        return None, f"YAML syntax error: {e}"

def validate_reconciler_yaml(yaml_path):
    data = clean_yaml_file(yaml_path)
    if isinstance(data, tuple): return False, data[1] # error
    if not isinstance(data, dict): return False, "Root must be a dictionary."
    if 'topic_id' not in data: return False, "Missing 'topic_id'."
    if 'semantic_units' not in data: return False, "Missing 'semantic_units'."
    return True, "Valid"

def resolve_assets(yaml_path):
    data = clean_yaml_file(yaml_path)
    if isinstance(data, tuple) or not os.path.exists(DB_PATH): return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for unit in data.get('semantic_units', []):
        if 'visual_asset_refs' in unit:
            for ref in unit['visual_asset_refs']:
                asset_id = ref.get('asset_id')
                if asset_id:
                    cursor.execute("SELECT file_path, excluded_from_candidates FROM assets WHERE id = ?", (asset_id,))
                    row = cursor.fetchone()
                    if row and row[0] != "VIRTUAL_RENDER_REQUIRED":
                        file_path = row[0]
                        excluded = row[1]
                        if not excluded:
                            ref['obsidian_path'] = f"assets/{file_path}"
                        else:
                            ref['excluded'] = True
    conn.close()
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def get_chapter_topics(chapter_id):
    course_map = os.path.join(COURSE_DIR, "course-model", "course.yaml")
    with open(course_map, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    for chap in data.get('chapters', []):
        if chap['id'] == chapter_id:
            return [t['id'] for t in chap.get('topics', [])]
    return []

def get_nearby_text(cursor, source_id, page_num):
    cursor.execute("SELECT content FROM fragments WHERE source_id = ? AND page_num = ? ORDER BY block_order LIMIT 3", (source_id, page_num))
    rows = cursor.fetchall()
    return " ".join([r[0] for r in rows]).replace("\n", " ")

def prep_reconciler(topic_id):
    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")
    run_dir = os.path.join(RUNS_DIR, topic_id, run_id)
    os.makedirs(run_dir, exist_ok=True)
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    
    print(f"\n[{run_id}] Running retrieval for {topic_id}...")
    retriever.generate_topic_context(topic_id)
    retriever_out = os.path.join(COURSE_DIR, "runtime", "topic-context", f"{topic_id}.md")
    if not os.path.exists(retriever_out):
        print(f"[ERROR] Retriever failed to generate {retriever_out}")
        sys.exit(1)

    evidence_path = os.path.join(run_dir, "evidence-package.md")
    shutil.copy2(retriever_out, evidence_path)
    
    reconciler_prompt_path = os.path.join(PROMPTS_DIR, "reconcile.md")
    with open(reconciler_prompt_path, 'r', encoding='utf-8') as f:
        reconciler_prompt = f.read()
    with open(evidence_path, 'r', encoding='utf-8') as f:
        evidence_content = f.read()
        
    reconciler_input_path = os.path.join(run_dir, "reconciler-input.md")
    with open(reconciler_input_path, 'w', encoding='utf-8') as f:
        f.write(reconciler_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: EVIDENCE PACKAGE\n\n")
        f.write(evidence_content)
        
    print(f"[{run_id}] prep-reconciler completed! Input saved to: {reconciler_input_path}")
    print(f"Next: generate reconciler-output.yaml and then run prep-writer {topic_id} {run_id}")

def prep_writer(topic_id, run_id):
    run_dir = os.path.join(RUNS_DIR, topic_id, run_id)
    if not os.path.exists(run_dir):
        print(f"[ERROR] Run directory not found: {run_dir}")
        sys.exit(1)
        
    reconciler_output_path = os.path.join(run_dir, "reconciler-output.yaml")
    if not os.path.exists(reconciler_output_path):
        print(f"[ERROR] {reconciler_output_path} not found.")
        sys.exit(1)
        
    is_valid, msg = validate_reconciler_yaml(reconciler_output_path)
    if not is_valid:
        print(f"[ERROR] YAML validation failed: {msg}")
        sys.exit(1)
        
    # Validation per evitare mix accidentali tra run:
    # controlliamo che il topic_id all'interno del YAML corrisponda a quello in input
    data = clean_yaml_file(reconciler_output_path)
    yaml_topic_id = data.get('topic_id')
    if yaml_topic_id != topic_id:
        print(f"[ERROR] Mismatch: yaml topic_id '{yaml_topic_id}' != '{topic_id}'")
        sys.exit(1)
        
    print(f"[{run_id}] Validation passed! Resolving visual assets...")
    resolve_assets(reconciler_output_path)
    
    writer_prompt_path = os.path.join(PROMPTS_DIR, "writer.md")
    style_guide_path = os.path.join(BASE_DIR, "profile", "style-guide.md")
    course_memory_path = os.path.join(COURSE_DIR, "course-model", "course-memory.yaml")
    
    with open(writer_prompt_path, 'r', encoding='utf-8') as f: writer_prompt = f.read()
    with open(style_guide_path, 'r', encoding='utf-8') as f: style_guide = f.read()
    with open(course_memory_path, 'r', encoding='utf-8') as f: course_memory = f.read()
    with open(reconciler_output_path, 'r', encoding='utf-8') as f: reconciled_yaml = f.read()
        
    writer_input_path = os.path.join(run_dir, "writer-input.md")
    with open(writer_input_path, 'w', encoding='utf-8') as f:
        f.write(writer_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: STYLE GUIDE\n\n")
        f.write(style_guide)
        f.write("\n\n---\n\n# RUNTIME INPUT: COURSE MEMORY\n\n```yaml\n")
        f.write(course_memory)
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: RECONCILER REPORT\n\n```yaml\n")
        f.write(reconciled_yaml)
        f.write("\n```\n")
        
    print(f"[{run_id}] prep-writer completed! Input saved to: {writer_input_path}")

def build_chapter(chapter_id):
    topics = get_chapter_topics(chapter_id)
    if not topics:
        print(f"Chapter {chapter_id} not found or has no topics.")
        return

    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")
    run_dir = os.path.join(CHAPTER_RUNS_DIR, chapter_id, run_id)
    sel_dir = os.path.join(run_dir, "asset-selector")
    img_dir = os.path.join(sel_dir, "images")
    rev_dir = os.path.join(run_dir, "reviewer")
    mem_dir = os.path.join(run_dir, "memory")
    
    for d in [img_dir, rev_dir, mem_dir]:
        os.makedirs(d, exist_ok=True)
    os.makedirs(CHAPTER_DRAFTS_DIR, exist_ok=True)

    # 1. Asset Selection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    candidates = []
    for topic_id in topics:
        topic_runs_dir = os.path.join(RUNS_DIR, topic_id)
        if not os.path.exists(topic_runs_dir): continue
        latest_run = sorted(os.listdir(topic_runs_dir))[-1]
        rec_yaml = os.path.join(topic_runs_dir, latest_run, "reconciler-output.yaml")
        if not os.path.exists(rec_yaml): continue
        
        data = clean_yaml_file(rec_yaml)
        if isinstance(data, tuple) or not isinstance(data, dict): continue
        
        for unit in data.get('semantic_units', []):
            for ref in unit.get('visual_asset_refs', []):
                if not ref.get('excluded') and ref.get('obsidian_path'):
                    asset_id = ref.get('asset_id')
                    source_id = ref.get('source_id')
                    page = ref.get('page')
                    obsidian_path = ref.get('obsidian_path')
                    
                    nearby = get_nearby_text(cursor, source_id, page)
                    
                    candidates.append({
                        'asset_id': asset_id,
                        'topic_id': topic_id,
                        'source_id': source_id,
                        'page': page,
                        'obsidian_path': obsidian_path,
                        'nearby_text': nearby[:200] + "..." if len(nearby) > 200 else nearby
                    })
                    
                    src_img = os.path.join(COURSE_DIR, obsidian_path)
                    if os.path.exists(src_img):
                        shutil.copy2(src_img, os.path.join(img_dir, os.path.basename(obsidian_path)))

    conn.close()

    candidates_yaml_path = os.path.join(sel_dir, "candidates.yaml")
    with open(candidates_yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump({'candidate_assets': candidates}, f, allow_unicode=True, sort_keys=False)

    selector_prompt_path = os.path.join(PROMPTS_DIR, "asset-selector.md")
    with open(selector_prompt_path, 'r', encoding='utf-8') as f: selector_prompt = f.read()
    
    selector_input_path = os.path.join(sel_dir, "selector-input.md")
    with open(selector_input_path, 'w', encoding='utf-8') as f:
        f.write(selector_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: CANDIDATE ASSETS\n\n```yaml\n")
        f.write(yaml.dump({'candidate_assets': candidates}, allow_unicode=True, sort_keys=False))
        f.write("\n```\n")

    selector_output_path = os.path.join(sel_dir, "selector-output.yaml")
    with open(selector_output_path, 'w', encoding='utf-8') as f: pass

    extra_msg = f"⚠ IMPORTANTE: Allega tutte le immagini contenute in:\n   -> {img_dir}\ninsieme al file selector-input.md!"
    wait_for_user("ASSET SELECTOR (Fase 1/2)", selector_input_path, selector_output_path, extra_message=extra_msg)
    
    selected_assets_yaml = ""
    with open(selector_output_path, 'r', encoding='utf-8') as f:
        selected_assets_yaml = f.read()

    # 2. Chapter Reviewer
    reviewer_prompt_path = os.path.join(PROMPTS_DIR, "chapter-reviewer.md")
    with open(reviewer_prompt_path, 'r', encoding='utf-8') as f: reviewer_prompt = f.read()
    style_guide_path = os.path.join(BASE_DIR, "profile", "style-guide.md")
    with open(style_guide_path, 'r', encoding='utf-8') as f: style_guide = f.read()
    course_memory_path = os.path.join(COURSE_DIR, "course-model", "course-memory.yaml")
    with open(course_memory_path, 'r', encoding='utf-8') as f: course_memory = f.read()
    
    merged_drafts = []
    for topic_id in topics:
        draft_path = os.path.join(DRAFTS_DIR, f"{topic_id}.md")
        if os.path.exists(draft_path):
            with open(draft_path, 'r', encoding='utf-8') as f:
                merged_drafts.append(f"<!-- TOPIC START: {topic_id} -->\n{f.read()}\n<!-- TOPIC END: {topic_id} -->")
    
    reviewer_input_path = os.path.join(rev_dir, "reviewer-input.md")
    with open(reviewer_input_path, 'w', encoding='utf-8') as f:
        f.write(reviewer_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: CHAPTER DEFINITION\n\n```yaml\n")
        f.write(yaml.dump({'chapter': {'id': chapter_id, 'topics': topics}}, allow_unicode=True, sort_keys=False))
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: STYLE GUIDE\n\n")
        f.write(style_guide)
        f.write("\n\n---\n\n# RUNTIME INPUT: COURSE MEMORY\n\n```yaml\n")
        f.write(course_memory)
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: SELECTED ASSETS\n\n```yaml\n")
        f.write(selected_assets_yaml)
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: TOPIC DRAFTS\n\n")
        f.write("\n\n".join(merged_drafts))
        
    reviewer_output_path = os.path.join(rev_dir, "reviewer-output.md")
    with open(reviewer_output_path, 'w', encoding='utf-8') as f: pass

    wait_for_user("CHAPTER ASSEMBLER & REVIEWER (Fase 2/2)", reviewer_input_path, reviewer_output_path)
    
    candidate_path = os.path.join(CHAPTER_DRAFTS_DIR, f"{chapter_id}.md")
    shutil.copy2(reviewer_output_path, candidate_path)
    print(f"\n[{run_id}] Chapter built! Candidate saved to: {candidate_path}")

def approve_chapter(chapter_id):
    candidate_path = os.path.join(CHAPTER_DRAFTS_DIR, f"{chapter_id}.md")
    if not os.path.exists(candidate_path):
        print(f"Candidate chapter {chapter_id} not found in {CHAPTER_DRAFTS_DIR}")
        return
        
    os.makedirs(CANONICAL_DIR, exist_ok=True)
    canonical_path = os.path.join(CANONICAL_DIR, f"{chapter_id}.md")
    shutil.copy2(candidate_path, canonical_path)
    
    # Save approval metadata
    manifest = {
        'chapter_id': chapter_id,
        'approved_at': datetime.now().isoformat(),
        'source_candidate': candidate_path
    }
    manifest_path = os.path.join(CANONICAL_DIR, f"{chapter_id}_metadata.yaml")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False)
        
    print(f"Chapter {chapter_id} approved and promoted to {canonical_path}")

def update_memory(chapter_id):
    manifest_path = os.path.join(CANONICAL_DIR, f"{chapter_id}_metadata.yaml")
    if not os.path.exists(manifest_path):
        print(f"[ERROR] Approval metadata {manifest_path} not found. Are you sure this chapter was approved using 'approve-chapter'?")
        return

    canonical_path = os.path.join(CANONICAL_DIR, f"{chapter_id}.md")
    if not os.path.exists(canonical_path):
        print(f"[ERROR] Canonical chapter {chapter_id} not found in {CANONICAL_DIR}. Approve it first!")
        return
        
    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")
    mem_dir = os.path.join(CHAPTER_RUNS_DIR, chapter_id, run_id, "memory")
    os.makedirs(mem_dir, exist_ok=True)
    
    memory_prompt_path = os.path.join(PROMPTS_DIR, "memory-update.md")
    with open(memory_prompt_path, 'r', encoding='utf-8') as f: memory_prompt = f.read()
    with open(canonical_path, 'r', encoding='utf-8') as f: canonical_content = f.read()
    course_memory_path = os.path.join(COURSE_DIR, "course-model", "course-memory.yaml")
    with open(course_memory_path, 'r', encoding='utf-8') as f: course_memory = f.read()
    
    mem_input_path = os.path.join(mem_dir, "memory-input.md")
    with open(mem_input_path, 'w', encoding='utf-8') as f:
        f.write(memory_prompt)
        f.write(f"\n\n---\n\n# RUNTIME INPUT: CHAPTER {chapter_id}\n\n")
        f.write(canonical_content)
        f.write("\n\n---\n\n# RUNTIME INPUT: CURRENT COURSE MEMORY\n\n```yaml\n")
        f.write(course_memory)
        f.write("\n```\n")
        
    mem_output_path = os.path.join(mem_dir, "memory-output.yaml")
    with open(mem_output_path, 'w', encoding='utf-8') as f: pass
    
    wait_for_user("MEMORY UPDATE", mem_input_path, mem_output_path)
    print(f"Memory update proposal saved to {mem_output_path}.")
    print("Please review it manually and merge changes into course-model/course-memory.yaml.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=['prep-reconciler', 'prep-writer', 'build-chapter', 'approve-chapter', 'update-memory'])
    parser.add_argument("target_id")
    parser.add_argument("run_id", nargs="?", help="Required for prep-writer")
    args = parser.parse_args()
    
    if args.command == 'prep-reconciler':
        prep_reconciler(args.target_id)
    elif args.command == 'prep-writer':
        if not args.run_id:
            print("ERROR: run_id is required for prep-writer")
            sys.exit(1)
        prep_writer(args.target_id, args.run_id)
    elif args.command == 'build-chapter':
        build_chapter(args.target_id)
    elif args.command == 'approve-chapter':
        approve_chapter(args.target_id)
    elif args.command == 'update-memory':
        update_memory(args.target_id)

if __name__ == "__main__":
    main()
