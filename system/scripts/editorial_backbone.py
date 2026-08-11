import os
import re
import yaml
import hashlib
import sys

def generate_id(*args):
    s = "|".join(str(a) for a in args).encode('utf-8')
    return "backbone-b" + hashlib.sha256(s).hexdigest()[:8]

def parse_markdown(filepath, source_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    img_pattern = re.compile(r'!\[\[(.*?)\]\]|!\[.*?\]\((.*?)\)')
    
    sections = []
    visual_bindings = []
    
    current_headings = {}
    
    current_section = {
        'section_id': 'sec-root',
        'heading': 'Root',
        'level': 0,
        'heading_path': 'Root',
        'blocks': []
    }
    sections.append(current_section)
    
    current_block_lines = []
    in_code_block = False
    
    last_block_id = None
    
    def flush_block():
        nonlocal current_block_lines, last_block_id
        if not current_block_lines:
            return
            
        chunk = "".join(current_block_lines).strip()
        current_block_lines = []
        if not chunk:
            return
            
        # extract images
        images = []
        for match in img_pattern.finditer(chunk):
            img_path = match.group(1) or match.group(2)
            if img_path and '|' in img_path:
                img_path = img_path.split('|')[0]
            images.append(img_path)
            
        clean_chunk = img_pattern.sub('', chunk).strip()
        
        if clean_chunk:
            block_type = 'paragraph'
            if clean_chunk.startswith('- ') or clean_chunk.startswith('* ') or re.match(r'^\d+\.\s', clean_chunk):
                block_type = 'list'
            elif clean_chunk.startswith('```'):
                block_type = 'code'
                
            block_index = len(current_section['blocks'])
            block_id = generate_id(source_id, current_section['heading_path'], block_index, clean_chunk)
            
            block = {
                'block_id': block_id,
                'type': block_type,
                'content': clean_chunk
            }
            current_section['blocks'].append(block)
            last_block_id = block_id
            
        for img in images:
            v_bind = {
                'asset_id': "img-" + hashlib.sha256((source_id + img + str(last_block_id)).encode('utf-8')).hexdigest()[:8],
                'obsidian_path': img,
                'original_placement': {
                    'after_block': last_block_id
                }
            }
            visual_bindings.append(v_bind)

    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            current_block_lines.append(line)
            continue
            
        if in_code_block:
            current_block_lines.append(line)
            continue
            
        heading_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if heading_match:
            flush_block()
            
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            
            current_headings = {lvl: t for lvl, t in current_headings.items() if lvl < level}
            current_headings[level] = title
            
            heading_path = " > ".join(current_headings[lvl] for lvl in sorted(current_headings.keys()))
            section_id = "sec-" + hashlib.sha256(heading_path.encode('utf-8')).hexdigest()[:8]
            
            current_section = {
                'section_id': section_id,
                'heading': title,
                'level': level,
                'heading_path': heading_path,
                'blocks': []
            }
            sections.append(current_section)
            continue
            
        if not stripped:
            flush_block()
        else:
            current_block_lines.append(line)
            
    flush_block()

    return {
        'editorial_backbone_version': "1.0",
        'source': {
            'id': source_id,
            'file': os.path.basename(filepath)
        },
        'sections': sections,
        'visual_bindings': visual_bindings
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Parse Editorial Backbone")
    parser.add_argument('--input', type=str, required=True, help="Path to markdown file")
    parser.add_argument('--output', type=str, required=True, help="Path to output yaml")
    parser.add_argument('--source-id', type=str, default='notes-90', help="Source ID")
    
    args = parser.parse_args()
    
    data = parse_markdown(args.input, args.source_id)
    with open(args.output, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        
    print(f"Parsed {args.input} into {args.output}")
    print(f"Sections: {len(data['sections'])}")
    print(f"Visual bindings: {len(data['visual_bindings'])}")

if __name__ == '__main__':
    main()
