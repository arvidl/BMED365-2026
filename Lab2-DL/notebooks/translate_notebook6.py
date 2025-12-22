#!/usr/bin/env python3
"""Script to translate final cells (27-29) in B2-learning-in-nn.ipynb"""

import json

with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

translations = {
    # Cell 27 - Summary and next steps
    "## Oppsummering og Veien Videre": "## Summary and The Way Forward",
    "### Hva vi har lært": "### What We Have Learned",
    "1. **Gradient Nedstigning** er kjernen i læring - vi finner minimum ved å følge gradienten": "1. **Gradient Descent** is the core of learning - we find the minimum by following the gradient",
    "2. **Backpropagation** beregner gradienter automatisk ved hjelp av kjerneregelen": "2. **Backpropagation** calculates gradients automatically using the chain rule",
    "3. **Trening** innebærer å iterativt oppdatere vekter for å minimere feil": "3. **Training** involves iteratively updating weights to minimize error",
    "4. **Overtilpasning** er en stor utfordring som kan løses med regularisering*": "4. **Overfitting** is a major challenge that can be solved with regularization*",
    "5. **Generalisering** er målet - modellen skal fungere på nye data": "5. **Generalization** is the goal - the model should work on new data",
    '(*) **Regularisering** er teknikker som legger til "straff" for komplekse modeller, slik at de ikke lærer for spesifikt på treningsdataene og kan generalisere bedre på nye, usette data.': '(*) **Regularization** refers to techniques that add "penalties" for complex models, so they don\'t learn too specifically on training data and can generalize better to new, unseen data.',
    "### Praktiske tips for Medisinsk AI": "### Practical Tips for Medical AI",
    "- **Start enkelt**: Begynn med enkle modeller først": "- **Start simple**: Begin with simple models first",
    "- **Valider grundig**: Bruk cross-validation og holdout-sett": "- **Validate thoroughly**: Use cross-validation and holdout sets",
    "- **Vær skeptisk**: Test modellen på nye data før implementering": "- **Be skeptical**: Test the model on new data before implementation",
    "- **Dokumenter alt**: Hold styr på hyperparametere og resultater": "- **Document everything**: Keep track of hyperparameters and results",
    "- **Samarbeid**: Inkluder klinikere i utviklingsprosessen": "- **Collaborate**: Include clinicians in the development process",
    "### Neste Steg: Klassifikasjon av UCI Heart Disease dataset med dyplæringsmodell": "### Next Step: Classification of UCI Heart Disease dataset with deep learning model",
    "I neste del (01c_UCI_heart_disease_klassifikasjon.ipynb) skal vi utforske:": "In the next part (01c_UCI_heart_disease_classification.ipynb) we will explore:",
    "1. **Nedlasting og preprosessering** av reelle UCI Heart Disease data": "1. **Download and preprocessing** of real UCI Heart Disease data",
    "2. **Eksplorativ dataanalyse** med visualiseringer": "2. **Exploratory data analysis** with visualizations",
    "3. **Forbedret nevralt nettverk** med batch normalization og dropout": "3. **Improved neural network** with batch normalization and dropout",
    "4. **Detaljert trening** med adaptive læringsrate": "4. **Detailed training** with adaptive learning rate",
    "5. **Omfattende evaluering** med forvirringsmatrise, ROC-kurve og ytelses-metrikker": "5. **Comprehensive evaluation** with confusion matrix, ROC curve and performance metrics",
    "6. **Feature importance analyse** for å forstå hvilke faktorer som er viktigst": "6. **Feature importance analysis** to understand which factors are most important",
    "7. **Klinisk tolkning** og praktiske anbefalinger": "7. **Clinical interpretation** and practical recommendations",
    "### Refleksjonsspørsmål": "### Reflection Questions",
    "1. Hvorfor er overtilpasning spesielt farlig i medisinsk AI?": "1. Why is overfitting especially dangerous in medical AI?",
    "2. Hvordan kan vi sikre at en medisinsk AI-modell generaliserer godt?": "2. How can we ensure that a medical AI model generalizes well?",
    "3. Hvilke etiske utfordringer ser du med automatisk medisinsk diagnostikk?": "3. What ethical challenges do you see with automatic medical diagnostics?",
    "4. Hvordan kan vi kombinere menneskelig ekspertise med maskinlæring?": "4. How can we combine human expertise with machine learning?",
}

def translate_cell(cell_content):
    result = cell_content
    for norwegian, english in translations.items():
        result = result.replace(norwegian, english)
    return result

for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        translated = translate_cell(content)
        cell['source'] = [line + '\n' if i < len(translated.split('\n')) - 1 else line 
                         for i, line in enumerate(translated.split('\n'))]
    elif cell['cell_type'] == 'code':
        new_source = []
        for line in cell['source']:
            translated_line = translate_cell(line)
            new_source.append(translated_line)
        cell['source'] = new_source

with open('B2-learning-in-nn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print("Translation part 6 complete!")

