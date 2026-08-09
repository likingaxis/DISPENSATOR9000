import os
import sys
import yaml
import sqlite3
import argparse
import shutil
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COURSE_DIR = os.path.join(BASE_DIR, "courses", "software-engineering")
DB_PATH = os.path.join(COURSE_DIR, ".derived", "fragments.db")
RUNS_DIR = os.path.join(COURSE_DIR, "runtime", "runs")
DRAFTS_DIR = os.path.join(COURSE_DIR, "runtime", "topic-drafts")
PROMPTS_DIR = os.path.join(BASE_DIR, "system", "prompts")

sys.path.append(os.path.dirname(__file__))
import retriever

def wait_for_user(filepath, message):
    print(f"\n{'-'*60}")
    print(message)
    print(f"File to edit: {filepath}")
    print(f"{'-'*60}")
    input("Press ENTER when you have saved the file...")

def validate_reconciler_yaml(yaml_path):
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return False, f"YAML syntax error: {e}"
        
    if not isinstance(data, dict):
        return False, "Root must be a dictionary."
        
    if 'topic_id' not in data:
        return False, "Missing 'topic_id'."
    if 'semantic_units' not in data:
        return False, "Missing 'semantic_units'."
        
    allowed_statuses = [
        'primary_supported', 
        'corroborated_by_primary', 
        'secondary_only_but_compatible', 
        'conflicts_with_primary'
    ]
    
    for unit in data.get('semantic_units', []):
        for claim in unit.get('claims', []):
            if 'statement' not in claim:
                return False, f"Claim missing 'statement' in unit {unit.get('id')}"
            if 'status' not in claim:
                return False, f"Claim missing 'status' in unit {unit.get('id')}"
            if claim['status'] not in allowed_statuses:
                return False, f"Invalid status '{claim['status']}' in unit {unit.get('id')}"
            if 'provenance' not in claim or not claim['provenance']:
                return False, f"Claim missing 'provenance' in unit {unit.get('id')}"
                
    return True, "Valid"

def resolve_assets(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    if not os.path.exists(DB_PATH):
        print(f"Warning: DB not found at {DB_PATH}. Skipping asset resolution.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for unit in data.get('semantic_units', []):
        if 'visual_asset_refs' in unit:
            for ref in unit['visual_asset_refs']:
                asset_id = ref.get('asset_id')
                if asset_id:
                    cursor.execute("SELECT file_path FROM assets WHERE id = ?", (asset_id,))
                    row = cursor.fetchone()
                    if row and row[0] != "VIRTUAL_RENDER_REQUIRED":
                        ref['obsidian_path'] = f"assets/{row[0]}"
                        
    conn.close()
    
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_id")
    args = parser.parse_args()
    
    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")
    run_dir = os.path.join(RUNS_DIR, args.topic_id, run_id)
    os.makedirs(run_dir, exist_ok=True)
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    
    metadata_path = os.path.join(run_dir, "run-metadata.yaml")
    metadata = {
        'topic_id': args.topic_id,
        'run_id': run_id,
        'versions': {
            'retriever': 'v0.1',
            'reconciler_prompt': 'v1',
            'writer_prompt': 'v1'
        },
        'status': {
            'retrieval': 'in_progress',
            'reconciliation': 'pending',
            'writing': 'pending',
            'review': 'pending',
            'user_approval': 'pending'
        },
        'artifacts': {
            'evidence_package': 'evidence-package.md',
            'reconciler_output': 'reconciler-output.yaml',
            'writer_output': 'writer-output.md'
        }
    }
    
    def save_metadata():
        with open(metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, allow_unicode=True, sort_keys=False)
            
    save_metadata()
    
    # 1. Retrieval
    print(f"\n[{run_id}] Running retrieval for {args.topic_id}...")
    retriever.generate_topic_context(args.topic_id)
    retriever_out = os.path.join(COURSE_DIR, "runtime", "topic-context", f"{args.topic_id}.md")
    
    if not os.path.exists(retriever_out):
        print(f"[ERROR] Retriever failed to generate {retriever_out}")
        sys.exit(1)

    evidence_path = os.path.join(run_dir, "evidence-package.md")
    shutil.copy2(retriever_out, evidence_path)
    metadata['status']['retrieval'] = 'completed'
    metadata['status']['reconciliation'] = 'in_progress'
    save_metadata()
    
    # 2. Reconciler
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
        
    reconciler_output_path = os.path.join(run_dir, "reconciler-output.yaml")
    # Touch empty file
    with open(reconciler_output_path, 'w', encoding='utf-8') as f:
        pass
        
    while True:
        wait_for_user(
            reconciler_output_path,
            f"1. Run the Reconciler LLM using the bundle at: {reconciler_input_path}\n"
            f"2. Save the LLM YAML output to: {reconciler_output_path}"
        )
        is_valid, msg = validate_reconciler_yaml(reconciler_output_path)
        if is_valid:
            print("Validation passed!")
            break
        else:
            print(f"\n[ERROR] YAML validation failed: {msg}")
            print("Please correct the file and try again.")
            
    # OD-W2 Resolution
    print("Resolving visual assets...")
    resolve_assets(reconciler_output_path)
    metadata['status']['reconciliation'] = 'completed'
    metadata['status']['writing'] = 'in_progress'
    save_metadata()
    
    # 3. Writer
    writer_prompt_path = os.path.join(PROMPTS_DIR, "writer.md")
    style_guide_path = os.path.join(BASE_DIR, "profile", "style-guide.md")
    course_memory_path = os.path.join(COURSE_DIR, "course-model", "course-memory.yaml")
    
    with open(writer_prompt_path, 'r', encoding='utf-8') as f:
        writer_prompt = f.read()
    with open(style_guide_path, 'r', encoding='utf-8') as f:
        style_guide = f.read()
    with open(course_memory_path, 'r', encoding='utf-8') as f:
        course_memory = f.read()
    with open(reconciler_output_path, 'r', encoding='utf-8') as f:
        reconciled_yaml = f.read()
        
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
        
    writer_output_path = os.path.join(run_dir, "writer-output.md")
    # Touch empty file
    with open(writer_output_path, 'w', encoding='utf-8') as f:
        pass
        
    wait_for_user(
        writer_output_path,
        f"1. Run the Writer LLM using the bundle at: {writer_input_path}\n"
        f"2. Save the LLM Markdown output to: {writer_output_path}"
    )
    
    # Save to topic drafts
    draft_path = os.path.join(DRAFTS_DIR, f"{args.topic_id}.md")
    shutil.copy2(writer_output_path, draft_path)
    
    metadata['status']['writing'] = 'completed'
    save_metadata()
    
    print(f"\n[{run_id}] Run completed! Draft saved to: {draft_path}")

if __name__ == "__main__":
    main()
