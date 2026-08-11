import argparse
import os
import sys
import yaml
import shutil
import sqlite3
import re
from datetime import datetime
import uuid
import hashlib
from PIL import Image

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

def wait_for_user(phase_name, input_path, output_path, extra_message=""):
    print("\n" + "="*70)
    print(f"AZIONE RICHIESTA: {phase_name}")
    print("="*70)
    if extra_message:
        print(extra_message)
    print(f"1. APRI questo file e COPIA tutto il suo contenuto:\n   -> {input_path}")
    print("2. INCOLLA il testo nella chat del tuo LLM (es. Opus/Claude).")
    print("3. COPIA la risposta generata dall'LLM.")
    print(f"4. INCOLLA e SALVA la risposta in questo file:\n   -> {output_path}")
    print("-" * 70)
    import time
    print(f"Polling for {output_path} to be populated...")
    while True:
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            print("File populated! Continuing...")
            break
        time.sleep(2)

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

def get_page_text(cursor, source_id, page_num):
    cursor.execute("SELECT content FROM fragments WHERE source_id = ? AND page_num = ? ORDER BY block_order", (source_id, page_num))
    rows = cursor.fetchall()
    return "\n".join([r[0] for r in rows if r[0]])

def strip_obsidian_images(text):
    if not text:
        return text
    return re.sub(r'!\[\[.*?\]\]', '', text)

def compile_visual_coverage(selector_output_path, visual_coverage_path):
    data = clean_yaml_file(selector_output_path)
    if not isinstance(data, dict):
        print(f"[ERROR] Invalid selector output YAML.")
        return False

    required_visuals = []
    recommended_visuals = []
    uncovered_required = []

    if 'slides' in data:
        for slide in data.get('slides', []):
            for vc in slide.get('visual_concepts', []):
                req = vc.get('requirement')
                status = vc.get('coverage_status')
                pref = vc.get('preferred_asset')
                
                if req == 'required':
                    if status == 'covered' and pref and pref.get('obsidian_path'):
                        required_visuals.append({
                            'visual_id': f"visual-{vc.get('concept_id', 'unknown')}",
                            'concept': {
                                'id': vc.get('concept_id'),
                                'label': vc.get('label') or vc.get('concept_id')
                            },
                            'asset': {
                                'obsidian_path': pref.get('obsidian_path')
                            },
                            'placement': vc.get('placement') or {'width': 500}
                        })
                    else:
                        uncovered_required.append(vc)
                elif req == 'recommended':
                    if status == 'covered' and pref and pref.get('obsidian_path'):
                        recommended_visuals.append({
                            'visual_id': f"visual-{vc.get('concept_id', 'unknown')}",
                            'concept': {
                                'id': vc.get('concept_id'),
                                'label': vc.get('label') or vc.get('concept_id')
                            },
                            'asset': {
                                'obsidian_path': pref.get('obsidian_path')
                            },
                            'placement': vc.get('placement') or {'width': 500}
                        })
    else:
        # Fallback se il modello ha già usato il formato corretto
        return False

    contract = {
        'visual_coverage_version': '1.0',
        'required_visuals': required_visuals,
        'recommended_visuals': recommended_visuals
    }

    if uncovered_required:
        contract['uncovered_required_visuals'] = uncovered_required

    with open(visual_coverage_path, 'w', encoding='utf-8') as f:
        yaml.dump(contract, f, allow_unicode=True, sort_keys=False)

    return len(uncovered_required) > 0

def get_nearest_header(markdown_text, search_str):
    lines = markdown_text.split('\n')
    current_header = ""
    for line in lines:
        if line.startswith('#'):
            current_header = line.strip()
        if search_str in line:
            return current_header
    return ""

def check_placement(expected_label, actual_header):
    if not actual_header:
        return False
    actual_header_clean = re.sub(r'^#+\s*', '', actual_header).lower()
    expected_label_clean = expected_label.lower()
    
    stop_words = {"modello", "def", "il", "la", "lo", "i", "gli", "le", "un", "una", "di", "a", "da", "in", "con", "su", "per", "tra", "fra"}
    words_a = set(re.findall(r'\b\w{3,}\b', actual_header_clean)) - stop_words
    words_e = set(re.findall(r'\b\w{3,}\b', expected_label_clean)) - stop_words
    
    if not words_a and not words_e:
        return True
        
    if words_a.intersection(words_e):
        return True
        
    if actual_header_clean in expected_label_clean or expected_label_clean in actual_header_clean:
        return True
        
    return False

def validate_visual_coverage(reviewer_output_path, visual_coverage_path, sel_dir):
    print("\n[VALIDATION] Running Visual Coverage Validator...")
    if not os.path.exists(reviewer_output_path) or not os.path.exists(visual_coverage_path):
        return False, "Missing output files for validation."

    with open(reviewer_output_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    cov_data = clean_yaml_file(visual_coverage_path)
    if not isinstance(cov_data, dict):
        return False, "Invalid visual-coverage YAML."

    required_assets = []
    recommended_assets = []
    uncovered_required = cov_data.get('uncovered_required_visuals', [])

    for item in cov_data.get('required_visuals', []):
        asset_info = item.get('asset', {})
        path = asset_info.get('obsidian_path')
        if path:
            required_assets.append({
                'obsidian_path': path,
                'width': item.get('placement', {}).get('width'),
                'concept_id': item.get('concept', {}).get('id'),
                'concept_label': item.get('concept', {}).get('label')
            })
    for item in cov_data.get('recommended_visuals', []):
        path = item.get('asset', {}).get('obsidian_path')
        if path:
            recommended_assets.append(path)

    embed_pattern = re.compile(r'!\[\[\s*([^\|\]\s]+)(?:\|(\d+))?\s*\]\]')
    matches = embed_pattern.findall(markdown_text)
    
    found_paths = [m[0].strip() for m in matches]
    found_widths = {m[0].strip(): int(m[1]) for m in matches if m[1]}

    missing_required = []
    duplicate_required = []
    width_mismatches = []
    unexpected_assets = []
    placement_errors = []

    req_paths = [r['obsidian_path'] for r in required_assets]
    allowed_paths = set(req_paths + recommended_assets)

    for req in required_assets:
        p = req['obsidian_path']
        count = found_paths.count(p)
        if count == 0:
            missing_required.append(p)
        elif count > 1:
            duplicate_required.append(p)
        else:
            # Check VC6 Placement
            label = req.get('concept_label') or req.get('concept_id') or ''
            header = get_nearest_header(markdown_text, p)
            if not check_placement(label, header):
                placement_errors.append(f"{p} is under header '{header}' but expected near '{label}'")
        
        if req['width'] and p in found_widths:
            if found_widths[p] != req['width']:
                width_mismatches.append(f"{p} (expected {req['width']}, got {found_widths[p]})")

    for p in found_paths:
        if p not in allowed_paths:
            unexpected_assets.append(p)

    status = "PASS"
    errors = []

    if missing_required:
        status = "FAIL"
        errors.append(f"Missing required visuals ({len(missing_required)}): {missing_required}")
    if duplicate_required:
        status = "FAIL"
        errors.append(f"Duplicate required visuals: {duplicate_required}")
    if unexpected_assets:
        status = "FAIL"
        errors.append(f"Unexpected / rejected assets found in markdown: {unexpected_assets}")
    if width_mismatches:
        status = "FAIL"
        errors.append(f"Width mismatches: {width_mismatches}")
    if placement_errors:
        status = "FAIL"
        errors.append(f"Placement errors (VC6): {placement_errors}")

    validation_result = {
        'status': status,
        'validated_at': datetime.now().isoformat(),
        'required_total': len(required_assets),
        'required_present': len(required_assets) - len(missing_required),
        'missing_required': missing_required,
        'duplicate_required': duplicate_required,
        'unexpected_assets': unexpected_assets,
        'width_mismatches': width_mismatches,
        'placement_errors': placement_errors,
        'uncovered_required_concepts': uncovered_required,
        'errors': errors
    }

    validation_path = os.path.join(sel_dir, "validation.yaml")
    with open(validation_path, 'w', encoding='utf-8') as f:
        yaml.dump(validation_result, f, allow_unicode=True, sort_keys=False)

    if uncovered_required:
        print(f"\n[VISUAL COVERAGE WARNING] {len(uncovered_required)} required visual concept(s) are UNCOVERED!")
        for unc in uncovered_required:
            print(f"  - {unc.get('concept_id', 'unknown')}: {unc.get('label', unc.get('reason', 'no suitable asset'))}")

    if status == "PASS":
        print(f"[VALIDATION SUCCESS] All {len(required_assets)} required visuals are correctly placed in the markdown!")
        return True, "PASS"
    else:
        print(f"[VALIDATION FAIL] Visual Coverage Validation Failed!")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False, f"Validation Failed: {errors}"

def prep_reconciler(topic_id):
    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")
    run_dir = os.path.join(RUNS_DIR, topic_id, run_id)
    os.makedirs(run_dir, exist_ok=True)
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    
    print(f"\n[{run_id}] Running retrieval for {topic_id}...")
    retriever.generate_topic_context(topic_id)
    retriever_out = os.path.join(COURSE_DIR, "runtime", "topic-context", f"{topic_id}.yaml")
    if not os.path.exists(retriever_out):
        print(f"[ERROR] Retriever failed to generate {retriever_out}")
        sys.exit(1)

    evidence_path = os.path.join(run_dir, "evidence-package.yaml")
    shutil.copy2(retriever_out, evidence_path)
    
    reconciler_prompt_path = os.path.join(PROMPTS_DIR, "reconcile.md")
    with open(reconciler_prompt_path, 'r', encoding='utf-8') as f:
        reconciler_prompt = f.read()
    with open(evidence_path, 'r', encoding='utf-8') as f:
        evidence_content = f.read()
        
    reconciler_input_path = os.path.join(run_dir, "reconciler-input.md")
    with open(reconciler_input_path, 'w', encoding='utf-8') as f:
        f.write(reconciler_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: EVIDENCE PACKAGE\n\n```yaml\n")
        f.write(evidence_content)
        f.write("\n```\n")
        
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

    # 1. Slide-Centric Asset Selection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    slides_map = {} # key: (topic_id, source_id, page)
    
    for topic_id in topics:
        topic_runs_dir = os.path.join(RUNS_DIR, topic_id)
        if not os.path.exists(topic_runs_dir): continue
        latest_run = sorted(os.listdir(topic_runs_dir))[-1]
        rec_yaml = os.path.join(topic_runs_dir, latest_run, "reconciler-output.yaml")
        if not os.path.exists(rec_yaml): continue
        
        data = clean_yaml_file(rec_yaml)
        if isinstance(data, tuple) or not isinstance(data, dict): continue
        
        for unit in data.get('semantic_units', []):
            unit_id = unit.get('id')
            unit_title = unit.get('title')
            for ref in unit.get('visual_asset_refs', []):
                if not ref.get('excluded') and ref.get('obsidian_path'):
                    asset_id = ref.get('asset_id')
                    source_id = ref.get('source_id')
                    page = ref.get('page')
                    obsidian_path = ref.get('obsidian_path')
                    
                    key = (topic_id, source_id, page)
                    if key not in slides_map:
                        slide_text = get_page_text(cursor, source_id, page)
                        slides_map[key] = {
                            'topic_id': topic_id,
                            'source_id': source_id,
                            'page': page,
                            'slide_title': unit_title or f"Page {page}",
                            'slide_text': slide_text,
                            'semantic_units': [],
                            'candidate_assets': []
                        }
                    
                    if unit_id and unit_id not in slides_map[key]['semantic_units']:
                        slides_map[key]['semantic_units'].append({
                            'concept_id': unit_id,
                            'label': unit_title
                        })
                    
                    # Fetch full physical metadata from DB
                    cursor.execute("SELECT width, height, aspect_ratio, bbox, asset_type, classification FROM assets WHERE id = ?", (asset_id,))
                    asset_row = cursor.fetchone()
                    
                    asset_meta = {
                        'asset_id': asset_id,
                        'obsidian_path': obsidian_path,
                        'asset_type': asset_row[4] if asset_row else 'embedded_image',
                        'width': asset_row[0] if asset_row else None,
                        'height': asset_row[1] if asset_row else None,
                        'aspect_ratio': asset_row[2] if asset_row else None,
                        'bbox': asset_row[3] if asset_row else None,
                        'classification': asset_row[5] if asset_row else None
                    }
                    
                    # Prevent duplicates in candidate_assets
                    if not any(a['asset_id'] == asset_id for a in slides_map[key]['candidate_assets']):
                        slides_map[key]['candidate_assets'].append(asset_meta)
                    
                    src_img = os.path.join(COURSE_DIR, obsidian_path)
                    if os.path.exists(src_img):
                        shutil.copy2(src_img, os.path.join(img_dir, os.path.basename(obsidian_path)))

    conn.close()

    slides_list = list(slides_map.values())

    candidates_yaml_path = os.path.join(sel_dir, "candidates.yaml")
    with open(candidates_yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump({'slides': slides_list}, f, allow_unicode=True, sort_keys=False)

    selector_prompt_path = os.path.join(PROMPTS_DIR, "asset-selector.md")
    with open(selector_prompt_path, 'r', encoding='utf-8') as f: selector_prompt = f.read()
    
    selector_input_path = os.path.join(sel_dir, "selector-input.md")
    with open(selector_input_path, 'w', encoding='utf-8') as f:
        f.write(selector_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: SLIDES AND CANDIDATE ASSETS\n\n```yaml\n")
        f.write(yaml.dump({'slides': slides_list}, allow_unicode=True, sort_keys=False))
        f.write("\n```\n")

    selector_output_path = os.path.join(sel_dir, "selector-output.yaml")
    with open(selector_output_path, 'w', encoding='utf-8') as f: pass

    extra_msg = f"IMPORTANTE: Allega tutte le immagini contenute in:\n   -> {img_dir}\ninsieme al file selector-input.md!"
    wait_for_user("ASSET SELECTOR & COVERAGE MAPPER (Fase 1/2)", selector_input_path, selector_output_path, extra_message=extra_msg)
    
# ---------------- PATCH 6: SEMANTIC CROP LOOP ----------------
    visual_coverage_path = os.path.join(sel_dir, "visual-coverage.yaml")
    if os.path.exists(selector_output_path):
        has_uncovered = compile_visual_coverage(selector_output_path, visual_coverage_path)
        
        if has_uncovered:
            print("\n[INFO] Found uncovered required visual concepts. Initiating Semantic Cropper (Patch 6)...")
            # Parse selector output to find what to crop
            selector_data = clean_yaml_file(selector_output_path)
            crop_requests = []
            if isinstance(selector_data, dict) and 'slides' in selector_data:
                for topic in selector_data['slides']:
                    for vc in topic.get('visual_concepts', []):
                        if vc.get('requirement') == 'required' and vc.get('coverage_status') == 'uncovered_no_suitable_asset':
                            # Find if page_render exists for this slide
                            src = topic.get('source_id')
                            pg = topic.get('page')
                            key = (topic.get('topic_id'), src, str(pg)) # need to match slides_map key type
                            page_render_asset = None
                            for slide in slides_list:
                                if slide['source_id'] == src and str(slide['page']) == str(pg):
                                    slide_text = slide.get('slide_text', '')
                                    for a in slide['candidate_assets']:
                                        if a['asset_type'] == 'page_render':
                                            page_render_asset = a
                                            break
                                    break
                            if page_render_asset:
                                crop_requests.append({
                                    'concept_id': vc.get('concept_id'),
                                    'label': vc.get('label', ''),
                                    'source_id': src,
                                    'page': pg,
                                    'slide_text': slide_text,
                                    'page_render_asset_id': page_render_asset['asset_id'],
                                    'page_render_path': page_render_asset['obsidian_path']
                                })
            
            if crop_requests:
                cropper_img_dir = os.path.join(sel_dir, "cropper-images")
                os.makedirs(cropper_img_dir, exist_ok=True)
                for req in crop_requests:
                    src_path = os.path.join(COURSE_DIR, req['page_render_path'])
                    if os.path.exists(src_path):
                        shutil.copy2(src_path, os.path.join(cropper_img_dir, os.path.basename(src_path)))
                
                cropper_input_path = os.path.join(sel_dir, "cropper-input.md")
                cropper_output_path = os.path.join(sel_dir, "cropper-output.yaml")
                
                cropper_prompt_path = os.path.join(PROMPTS_DIR, "semantic-cropper.md")
                with open(cropper_prompt_path, 'r', encoding='utf-8') as f: cropper_prompt = f.read()
                
                with open(cropper_input_path, 'w', encoding='utf-8') as f:
                    f.write(cropper_prompt)
                    f.write("\n\n---\n\n# RUNTIME INPUT: CROP REQUESTS\n\n```yaml\n")
                    f.write(yaml.dump({'requests': crop_requests}, allow_unicode=True, sort_keys=False))
                    f.write("\n```\n")
                
                with open(cropper_output_path, 'w', encoding='utf-8') as f: pass
                
                extra_msg_cropper = f"IMPORTANTE:\nallega al Vision LLM tutte le immagini contenute in:\n{cropper_img_dir}\n\nOgni immagine corrisponde a una crop_request presente in cropper-input.md."
                wait_for_user("SEMANTIC CROPPER (Fase 1.5)", cropper_input_path, cropper_output_path, extra_message=extra_msg_cropper)
                
                if os.path.exists(cropper_output_path):
                    crop_data = clean_yaml_file(cropper_output_path)
                    if isinstance(crop_data, dict) and 'crop_responses' in crop_data:
                        conn = sqlite3.connect(DB_PATH)
                        cursor = conn.cursor()
                        for resp in crop_data['crop_responses']:
                            if resp.get('status') == 'found':
                                bbox = resp.get('bbox', {})
                                x0, y0, x1, y1 = bbox.get('x0'), bbox.get('y0'), bbox.get('x1'), bbox.get('y1')
                                if all(v is not None for v in [x0, y0, x1, y1]) and 0 <= float(x0) < float(x1) <= 1 and 0 <= float(y0) < float(y1) <= 1:
                                    x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
                                    # avoid full page crop
                                    crop_area = (x1 - x0) * (y1 - y0)
                                    if crop_area > 0.90:
                                        print(f"Crop for {resp['concept_id']} rejected: too large (almost full page).")
                                        continue
                                    
                                    src_id = resp['source_id']
                                    pg = resp['page']
                                    cid = resp['concept_id']
                                    
                                    # find original image path
                                    orig_img_path = None
                                    for req in crop_requests:
                                        if req['source_id'] == src_id and str(req['page']) == str(pg) and req['concept_id'] == cid:
                                            orig_img_path = req['page_render_path']
                                            break
                                    
                                    if orig_img_path:
                                        full_img_path = os.path.join(COURSE_DIR, orig_img_path)
                                        if os.path.exists(full_img_path):
                                            try:
                                                with Image.open(full_img_path) as img:
                                                    w, h = img.width, img.height
                                                    left = int(x0 * w)
                                                    upper = int(y0 * h)
                                                    right = int(x1 * w)
                                                    lower = int(y1 * h)
                                                    
                                                    if right - left < 10 or lower - upper < 10:
                                                        print(f"Crop for {cid} rejected: too small.")
                                                        continue
                                                        
                                                    cropped_img = img.crop((left, upper, right, lower))
                                                    
                                                    # Calcola UUID prima per evitare collisioni sul filename
                                                    crop_key = f"{src_id}:{pg}:{cid}:{x0},{y0},{x1},{y1}"
                                                    asset_id = str(uuid.uuid5(uuid.NAMESPACE_URL, crop_key))
                                                    
                                                    safe_cid = re.sub(r'[^A-Za-z0-9_-]+', '-', cid)
                                                    new_filename = f"{src_id}_p{pg}_crop_{safe_cid}_{asset_id[:8]}.png"
                                                    new_path = os.path.join(COURSE_DIR, "assets", new_filename)
                                                    cropped_img.save(new_path)
                                                    
                                                    # Insert into DB
                                                    obsidian_path = f"assets/{new_filename}"
                                                    
                                                    cursor.execute('''
                                                        INSERT OR IGNORE INTO assets (id, source_id, source_file, page_num, file_path, bbox, asset_type, width, height, aspect_ratio, image_hash, classification, excluded_from_candidates)
                                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                                    ''', (asset_id, src_id, "", int(pg), new_filename, f"{left},{upper},{right},{lower}", "semantic_crop", cropped_img.width, cropped_img.height, cropped_img.width/cropped_img.height if cropped_img.height > 0 else 0, "", "uncertain", 0))
                                                    
                                                    # Update slides_list to include the new candidate!
                                                    new_meta = {
                                                        'asset_id': asset_id,
                                                        'obsidian_path': obsidian_path,
                                                        'asset_type': 'semantic_crop',
                                                        'width': cropped_img.width,
                                                        'height': cropped_img.height,
                                                        'aspect_ratio': cropped_img.width/cropped_img.height if cropped_img.height > 0 else 0,
                                                        'bbox': f"{left},{upper},{right},{lower}",
                                                        'classification': 'uncertain'
                                                    }
                                                    for slide in slides_list:
                                                        if slide['source_id'] == src_id and str(slide['page']) == str(pg):
                                                            slide['candidate_assets'].append(new_meta)
                                                            break
                                                            
                                                    # Copy to img_dir so LLM can see it
                                                    shutil.copy2(new_path, os.path.join(img_dir, new_filename))
                                                    print(f"Successfully cropped {cid} from {orig_img_path}")
                                            except Exception as e:
                                                print(f"Error cropping {orig_img_path}: {e}")
                        conn.commit()
                        conn.close()
                        
                        # Phase 1 Recovery Pass!
                        with open(candidates_yaml_path, 'w', encoding='utf-8') as f:
                            yaml.dump({'slides': slides_list}, f, allow_unicode=True, sort_keys=False)
                        with open(selector_input_path, 'w', encoding='utf-8') as f:
                            f.write(selector_prompt)
                            f.write("\n\n---\n\n# RUNTIME INPUT: SLIDES AND CANDIDATE ASSETS (RECOVERY PASS)\n\n```yaml\n")
                            f.write(yaml.dump({'slides': slides_list}, allow_unicode=True, sort_keys=False))
                            f.write("\n```\n")
                        
                        with open(selector_output_path, 'w', encoding='utf-8') as f: pass
                        
                        extra_msg = f"IMPORTANTE: Allega tutte le immagini contenute in:\n   -> {img_dir}\ninsieme al file selector-input.md (RECOVERY PASS)!"
                        wait_for_user("ASSET SELECTOR (Recovery Pass 2/2)", selector_input_path, selector_output_path, extra_message=extra_msg)
                        
                        # Final check
                        has_uncovered = compile_visual_coverage(selector_output_path, visual_coverage_path)
                        
            if has_uncovered:
                print(f"\n[ERROR] Pipeline blocked (BLOCKED_UPSTREAM): uncovered required visual concept(s) found even after Semantic Cropper.")
                sys.exit(1)

    with open(visual_coverage_path, 'r', encoding='utf-8') as f:
        visual_coverage_yaml = f.read()
    # ---------------- END PATCH 6 ----------------


    # 2. Chapter Reviewer (Assembler)
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
                raw_draft = f.read()
                # Deterministically strip any obsidian image embeds from draft!
                clean_draft = strip_obsidian_images(raw_draft)
                merged_drafts.append(f"<!-- TOPIC START: {topic_id} -->\n{clean_draft}\n<!-- TOPIC END: {topic_id} -->")
    
    reviewer_input_path = os.path.join(rev_dir, "reviewer-input.md")
    with open(reviewer_input_path, 'w', encoding='utf-8') as f:
        f.write(reviewer_prompt)
        f.write("\n\n---\n\n# RUNTIME INPUT: CHAPTER DEFINITION\n\n```yaml\n")
        f.write(yaml.dump({'chapter': {'id': chapter_id, 'topics': topics}}, allow_unicode=True, sort_keys=False))
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: STYLE GUIDE\n\n")
        f.write(style_guide)
        f.write("\n\n---\n\n# RUNTIME INPUT: COURSE MEMORY\n\n```yaml\n")
        f.write(course_memory)
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: VISUAL COVERAGE CONTRACT\n\n```yaml\n")
        f.write(visual_coverage_yaml)
        f.write("\n```\n\n---\n\n# RUNTIME INPUT: TOPIC DRAFTS (TEXT ONLY)\n\n")
        f.write("\n\n".join(merged_drafts))
        
    reviewer_output_path = os.path.join(rev_dir, "reviewer-output.md")
    with open(reviewer_output_path, 'w', encoding='utf-8') as f: pass

    wait_for_user("CHAPTER ASSEMBLER & REVIEWER (Fase 2/2)", reviewer_input_path, reviewer_output_path)
    
    # 3. Deterministic Visual Coverage Validation
    is_valid, msg = validate_visual_coverage(reviewer_output_path, visual_coverage_path, sel_dir)
    if not is_valid:
        print(f"\n[ERROR] Chapter promotion BLOCKED due to Visual Coverage Validation failure: {msg}")
        return

    candidate_path = os.path.join(CHAPTER_DRAFTS_DIR, f"{chapter_id}.md")
    shutil.copy2(reviewer_output_path, candidate_path)
    print(f"\n[{run_id}] Chapter built and validated successfully! Candidate saved to: {candidate_path}")

def approve_chapter(chapter_id):
    candidate_path = os.path.join(CHAPTER_DRAFTS_DIR, f"{chapter_id}.md")
    if not os.path.exists(candidate_path):
        print(f"Candidate chapter {chapter_id} not found in {CHAPTER_DRAFTS_DIR}")
        return
        
    os.makedirs(CANONICAL_DIR, exist_ok=True)
    canonical_path = os.path.join(CANONICAL_DIR, f"{chapter_id}.md")
    shutil.copy2(candidate_path, canonical_path)
    
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
