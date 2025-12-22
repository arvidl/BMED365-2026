#!/usr/bin/env python3
"""Final cleanup script to translate remaining Norwegian text in B2-learning-in-nn.ipynb"""

import json

# Read the notebook
with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Define translations as (old_text, new_text) pairs
translations = [
    # Cell 21 - Why error increases after update
    ("## 🤔 Hvorfor Økte Erroren etter Oppdatering?", "## 🤔 Why Did the Error Increase After the Update?"),
    ("Du har lagt merke til noe viktig: **Erroren økte fra 5.0 til 9.0** etter oppdatering! Dette skjer av flere grunner:", 
     "You noticed something important: **The error increased from 5.0 to 9.0** after the update! This happens for several reasons:"),
    ("- **Before oppdatering**: Prediction = 5.0, Error = |10.0 - 5.0| = 5.0",
     "- **Before update**: Prediction = 5.0, Error = |10.0 - 5.0| = 5.0"),
    ("- **After oppdatering**: Prediction = 19.0, Error = |10.0 - 19.0| = 9.0",
     "- **After update**: Prediction = 19.0, Error = |10.0 - 19.0| = 9.0"),
    ("#### 1. **For Høy Learning rate (α = 0.1)**", "#### 1. **Too High Learning Rate (α = 0.1)**"),
    ("- Learning raten er **for stor** for dette problemet", "- The learning rate is **too large** for this problem"),
    ("#### 2. **Gradients er Negative**", "#### 2. **Gradients are Negative**"),
    ("#### **Reduser Learning raten:**", "#### **Reduce the Learning Rate:**"),
    ("#### **Adaptive Learning rater:**", "#### **Adaptive Learning Rates:**"),
    
    # Cell 25 - Batch processing
    ("#### 🏥 **Medisinsk Eksempel: Hjerte-kar-sykdom Prediction**", 
     "#### 🏥 **Medical Example: Cardiovascular Disease Prediction**"),
    ("Batch størrelse", "Batch size"),
    ("Epoke", "Epoch"),
]

# Apply translations to all cells
for cell in notebook['cells']:
    if cell['cell_type'] in ['markdown', 'code']:
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                new_line = line
                for old_text, new_text in translations:
                    new_line = new_line.replace(old_text, new_text)
                new_source.append(new_line)
            cell['source'] = new_source
        else:
            new_source = source
            for old_text, new_text in translations:
                new_source = new_source.replace(old_text, new_text)
            cell['source'] = new_source

# Write the updated notebook
with open('B2-learning-in-nn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("✅ Final cleanup complete - all remaining Norwegian text has been translated to English!")

