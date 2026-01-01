import json
import os

def generate_pages():
    with open('data/calligraphers.json', 'r') as f:
        calligraphers = json.load(f)
    
    for c in calligraphers:
        slug = c['slug']
        dir_path = f'content/calligraphers/{slug}'
        os.makedirs(dir_path, exist_ok=True)
        
        content = f"""---
title: "{c['name']}"
date: 2024-01-01
description: "Profile of {c['name']}, a verified Arabic calligrapher based in {c['base']}."
base: "{c['base']}"
specialty: "{c['specialty']}"
website: "{c['website']}"
contact: "{c['contact']}"
scripts: {json.dumps(c['scripts'])}
languages: {json.dumps(c['languages'])}
featured: {str(c.get('featured', False)).lower()}
proof_notes: "{c['proof_notes']}"
sources: {json.dumps(c['sources'])}
---

{c['bio']}
"""
        with open(f'{dir_path}/index.md', 'w') as f:
            f.write(content)

if __name__ == "__main__":
    generate_pages()
