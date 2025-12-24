#!/usr/bin/env python3
"""Fix Norwegian file paths and directory names in B2-learning-in-nn.ipynb"""

import json

# Read the notebook
with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Define translations as (old_text, new_text) pairs
translations = [
    # Fix paths and filenames
    ("./ressurser//graf-for-illustrasjon-av-optimering-3D.png", "./resources/optimization-3D-illustration.png"),
    ("./ressurser/graf-for-illustrasjon-av-optimering-3D.png", "./resources/optimization-3D-illustration.png"),
    ("./ressurser/illustrasjon-av-backpropagation.png", "./resources/backpropagation-illustration.png"),
    
    # Fix comments
    ("# Write the figure to a png file kalt graf-for-illustrasjon-av-optimering-3D.png",
     "# Write the figure to a png file called optimization-3D-illustration.png"),
]

# Apply translations to all cells (including outputs)
def translate_content(content):
    if isinstance(content, str):
        for old_text, new_text in translations:
            content = content.replace(old_text, new_text)
        return content
    elif isinstance(content, list):
        return [translate_content(item) for item in content]
    elif isinstance(content, dict):
        return {k: translate_content(v) for k, v in content.items()}
    else:
        return content

notebook = translate_content(notebook)

# Write the updated notebook
with open('B2-learning-in-nn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("✅ Fixed all Norwegian file paths and directory names!")


