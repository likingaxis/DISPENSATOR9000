import sqlite3
import yaml
import os

DB_PATH = 'courses/software-engineering/.derived/fragments.db'
OUT_PATH = 'courses/software-engineering/course-model/exam-intelligence.yaml'

def get_questions_text():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT content FROM fragments 
        WHERE source_file LIKE '%risposte_domande_orali%'
    ''')
    rows = cursor.fetchall()
    conn.close()
    return " ".join([r[0] for r in rows]).lower()

def analyze_priority():
    text = get_questions_text()
    
    # We will do a basic keyword frequency analysis for Chapter 2 concepts
    concepts = {
        'waterfall-model': ['waterfall', 'cascata'],
        'spiral-model': ['spirale'],
        'incremental-development': ['incrementale', 'iterativo'],
        'corporate-models': ['microsoft', 'synch', 'netscape'],
        'agile-and-scrum': ['agile', 'scrum', 'sprint'],
        'cmm': ['cmm', 'capability maturity']
    }
    
    intelligence = {
        'exam_intelligence_version': "1.0",
        'concepts': {}
    }
    
    for concept_id, keywords in concepts.items():
        count = sum(text.count(k) for k in keywords)
        
        priority = 'low'
        if count > 5:
            priority = 'high'
        elif count > 1:
            priority = 'medium'
            
        intelligence['concepts'][concept_id] = {
            'priority': priority,
            'observed_question_types': ['explanation' if count > 0 else 'none']
        }
        
    return intelligence

if __name__ == '__main__':
    data = analyze_priority()
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)
    print(f"Generated {OUT_PATH}")
