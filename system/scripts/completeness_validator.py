import yaml
import sys
import os

def clean_yaml_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove markdown blocks if present
        if "```yaml" in content:
            content = content.split("```yaml")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
            
        return yaml.safe_load(content)
    except Exception as e:
        return None, f"YAML parsing error: {e}"

def validate_completeness(reconciler_yaml_path, completeness_yaml_path):
    # 1. Load Reconciler Output
    reconciler_data = clean_yaml_file(reconciler_yaml_path)
    if isinstance(reconciler_data, tuple):
        return False, f"Failed to parse Reconciler YAML: {reconciler_data[1]}"
        
    # Extract expected issues
    expected_issues = {}
    for unit in reconciler_data.get('semantic_units', []):
        for issue in unit.get('completeness_issues', []):
            if 'issue_id' in issue:
                expected_issues[issue['issue_id']] = issue.get('expected_resolution', 'resolve')

    # 2. Load Completeness Reviewer Output
    review_data = clean_yaml_file(completeness_yaml_path)
    if isinstance(review_data, tuple):
        return False, f"Failed to parse Completeness YAML: {review_data[1]}"
        
    if 'editorial_completeness_validation' not in review_data:
        return False, "Missing 'editorial_completeness_validation' root key."
        
    val = review_data['editorial_completeness_validation']
    
    # 3. Check Overall Status
    if val.get('status') != 'PASS':
        return False, "Completeness Reviewer returned FAIL status."
        
    # 4. Deterministic Enforcement
    resolved_ids = set()
    unresolved_ids = set()
    unsupported_ids = set()
    
    for issue in val.get('issues', []):
        issue_id = issue.get('issue_id')
        status = issue.get('status')
        if status == 'resolved':
            resolved_ids.add(issue_id)
        elif status == 'unresolved':
            unresolved_ids.add(issue_id)

    # Check that all expected issues were addressed
    for exp_id, expected_res in expected_issues.items():
        if exp_id not in resolved_ids and exp_id not in unresolved_ids:
            return False, f"Issue ID {exp_id} was ignored by the Completeness Reviewer."
            
        if expected_res == 'resolve':
            if exp_id in unresolved_ids or exp_id in val.get('unresolved', []):
                return False, f"Expected issue {exp_id} to be resolved, but it is unresolved."
        elif expected_res == 'preserve_unresolved':
            # If it was preserve_unresolved, the LLM should mark it as resolved (meaning it respected the rule)
            # OR if it was unsupported_additions, fail it.
            if exp_id in val.get('unsupported_additions', []):
                return False, f"Issue {exp_id} was marked as preserve_unresolved, but the Writer hallucinated an addition (unsupported_additions)."
                
    if len(val.get('unresolved', [])) > 0:
        return False, f"There are unresolved issues: {val.get('unresolved')}"
        
    if len(val.get('unsupported_additions', [])) > 0:
        return False, f"There are unsupported additions: {val.get('unsupported_additions')}"
        
    return True, "Completeness Contract Validated successfully."

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python completeness_validator.py <reconciler_output.yaml> <completeness_output.yaml>")
        sys.exit(1)
        
    reconciler_yaml = sys.argv[1]
    completeness_yaml = sys.argv[2]
    
    is_valid, msg = validate_completeness(reconciler_yaml, completeness_yaml)
    if is_valid:
        print("[PASS] " + msg)
        sys.exit(0)
    else:
        print("[FAIL] " + msg)
        sys.exit(1)
