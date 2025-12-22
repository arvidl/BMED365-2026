#!/usr/bin/env python3
"""Script to translate remaining cells (16-29) in B2-learning-in-nn.ipynb"""

import json

with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

translations = {
    # Cell 16 - Reproducibility functions
    "# === REPRODUSERBARHETSFUNKSJONER ===": "# === REPRODUCIBILITY FUNCTIONS ===",
    '"""Sett alle random seeds for reproduserbarhet"""': '"""Set all random seeds for reproducibility"""',
    "🎲 Random seeds satt til": "🎲 Random seeds set to",
    "(for reproduserbarhet)": "(for reproducibility)",
    '"""Opprett DataLoader med reproduserbar shuffle"""': '"""Create DataLoader with reproducible shuffle"""',
    "✅ Reproduserbarhetsfunksjoner definert": "✅ Reproducibility functions defined",
    "   - set_random_seeds(seed): Setter alle random seeds": "   - set_random_seeds(seed): Sets all random seeds",
    "   - create_deterministic_dataloader(): Oppretter DataLoader med reproduserbar shuffle": "   - create_deterministic_dataloader(): Creates DataLoader with reproducible shuffle",
    
    # Cell 17 - Backpropagation demonstration
    "# Demonstrer backpropagation med et enkelt eksempel": "# Demonstrate backpropagation with a simple example",
    "# Definer en enkel funksjon": "# Define a simple function",
    "# Tap": "# Loss",
    "# Input data": "# Input data",
    "# Modellparametere (trenger gradienter)": "# Model parameters (need gradients)",
    "=== Backpropagation Demonstrasjon ===": "=== Backpropagation Demonstration ===",
    "Sann verdi": "True value",
    "Initiale vekter": "Initial weights",
    "# Fremover-pass": "# Forward pass",
    "Prediksjon": "Prediction",
    "Tap": "Loss",
    "# Bakover-pass (beregn gradienter)": "# Backward pass (calculate gradients)",
    "Gradienter": "Gradients",
    "# Manuell verifikasjon": "# Manual verification",
    "Manuell verifikasjon": "Manual verification",
    
    # Cell 18
    "_Visuell demonstrasjon av backpropagation_": "_Visual demonstration of backpropagation_",
    
    # Cell 19 - Explanation
    "### 📊 Forklaring av Backpropagation-Visualiseringen (i figuren som konstrueres nedenfor)": "### 📊 Explanation of the Backpropagation Visualization (in the figure constructed below)",
    "Figuren under viser en komplett **backpropagation-demonstrasjon** som illustrerer hvordan et nevralt nettverk lærer. Her er en kort forklaring av hver del:": "The figure below shows a complete **backpropagation demonstration** that illustrates how a neural network learns. Here is a brief explanation of each part:",
    "#### 🧠 **Nevralt Nettverk: Fremover-pass** (øverst til venstre)": "#### 🧠 **Neural Network: Forward Pass** (top left)",
    "- **Input**: x1=2.0 og x2=3.0 (blå noder)": "- **Input**: x1=2.0 and x2=3.0 (blue nodes)",
    "- **Vekter**: w1=1.0 og w2=1.0 (røde piler)": "- **Weights**: w1=1.0 and w2=1.0 (red arrows)",
    "- **Bias**: b=0.0 (oransje node)": "- **Bias**: b=0.0 (orange node)",
    "- **Summeringsnode**: z=5.0 (lilla node med Σ-symbol)": "- **Summation node**: z=5.0 (purple node with Σ symbol)",
    "- **Output**: y=5.0 (grønn node)": "- **Output**: y=5.0 (green node)",
    "- **Prosess**: Input → Vekter → Summering → Output": "- **Process**: Input → Weights → Summation → Output",
    "#### 📊 **Feil-beregning** (øverst til høyre)": "#### 📊 **Error Calculation** (top right)",
    "- **Sann verdi**: 10.0 (grønn søyle)": "- **True value**: 10.0 (green bar)",
    "- **Prediksjon**: 5.0 (rød søyle)": "- **Prediction**: 5.0 (red bar)",
    "- **Feil**: 5.0 (lilla pil)": "- **Error**: 5.0 (purple arrow)",
    "- **Tap**: 25.0 (kvadratet av feilen)": "- **Loss**: 25.0 (square of the error)",
    "#### ⚡ **Gradient-beregning** (nederst til venstre)": "#### ⚡ **Gradient Calculation** (bottom left)",
    "- **Kjerneregelen**: ∂L/∂w = ∂L/∂y × ∂y/∂z × ∂z/∂w": "- **Chain rule**: ∂L/∂w = ∂L/∂y × ∂y/∂z × ∂z/∂w",
    "- **Gradienter**: w1=-20.0, w2=-30.0, b=-10.0": "- **Gradients**: w1=-20.0, w2=-30.0, b=-10.0",
    "- **Betydning**: Negative verdier betyr at vektene må økes for å redusere feilen": "- **Meaning**: Negative values mean the weights must be increased to reduce the error",
    "#### 🔄 **Vekt-oppdatering** (nederst til høyre)": "#### 🔄 **Weight Update** (bottom right)",
    "- **Før oppdatering**: w1=1.0, w2=1.0, b=0.0 (røde søyler)": "- **Before update**: w1=1.0, w2=1.0, b=0.0 (red bars)",
    "- **Etter oppdatering**: w1=3.0, w2=4.0, b=1.0 (grønne søyler)": "- **After update**: w1=3.0, w2=4.0, b=1.0 (green bars)",
    "- **Læring**: Vektene justeres i retning som reduserer feilen": "- **Learning**: Weights are adjusted in the direction that reduces the error",
    "#### 📚 **Matematisk Forklaring** (nederst i midten)": "#### 📚 **Mathematical Explanation** (bottom center)",
    "- **Symbolsk derivasjon** av alle gradienter": "- **Symbolic derivation** of all gradients",
    "- **Kjerneregelen** forklart i detalj": "- **Chain rule** explained in detail",
    "- **Trinn-for-trinn beregninger** med faktiske verdier": "- **Step-by-step calculations** with actual values",
    '**Hovedpoeng**: Dette viser hvordan AI "lærer" ved å iterativt justere sine interne parametere (w1, w2, b) basert på feilen i prediksjonen - "lærer av sine feil"': '**Main point**: This shows how AI "learns" by iteratively adjusting its internal parameters (w1, w2, b) based on the error in the prediction - "learning from its mistakes"',
    
    # Cell 20 - Code visualization
    "# Visuell demonstrasjon av backpropagation": "# Visual demonstration of backpropagation",
    '"""Forbedret visuell demonstrasjon av backpropagation med mer illustrativ design"""': '"""Improved visual demonstration of backpropagation with more illustrative design"""',
    "🧠 === BACKPROPAGATION DEMONSTRASJON === 🧠": "🧠 === BACKPROPAGATION DEMONSTRATION === 🧠",
    "# Opprett visualisering med bedre layout": "# Create visualization with better layout",
    "# Opprett grid layout": "# Create grid layout",
    "# 1. Nevralt nettverk diagram (forbedret med summeringsnode)": "# 1. Neural network diagram (improved with summation node)",
    "Nevralt Nettverk: Fremover-pass": "Neural Network: Forward Pass",
    "# Input lag": "# Input layer",
    "# Vekter og piler til summeringsnode": "# Weights and arrows to summation node",
    "# Vis mellomliggende beregninger": "# Show intermediate calculations",
    "# Summeringsnode": "# Summation node",
    "# Piler fra vekter til summeringsnode": "# Arrows from weights to summation node",
    "# Bias til summeringsnode": "# Bias to summation node",
    "# Output fra summeringsnode": "# Output from summation node",
    "# Vis summeringsformel": "# Show summation formula",
    "# 2. Feil-beregning": "# 2. Error calculation",
    "Feil-beregning": "Error Calculation",
    "# Sann verdi vs prediksjon med bedre design": "# True value vs prediction with better design",
    "# Feil-pil med bedre design": "# Error arrow with better design",
    "Feil": "Error",
    "# Tap med bedre design": "# Loss with better design",
    "# 3. Gradient-beregning": "# 3. Gradient calculation",
    "Gradient-beregning (Bakover-pass)": "Gradient Calculation (Backward Pass)",
    "# Kjerneregelen med bedre design": "# Chain rule with better design",
    "Kjerneregelen": "Chain Rule",
    "# Gradienter med bedre visualisering": "# Gradients with better visualization",
    "# Lag gradient-bars med bedre design": "# Create gradient bars with better design",
    "# Legg til gradient-verdier over bars": "# Add gradient values above bars",
    "# Legg til piler som viser retning": "# Add arrows showing direction",
    "Gradient-verdi": "Gradient value",
    "# 4. Vekt-oppdatering": "# 4. Weight update",
    "Vekt-oppdatering": "Weight Update",
    "# Før og etter med bedre design": "# Before and after with better design",
    "# Gamle vekter": "# Old weights",
    "Før": "Before",
    "# Nye vekter": "# New weights",
    "Etter": "After",
    "# Piler som viser endring med bedre design": "# Arrows showing change with better design",
    "# Legg til verdier over bars": "# Add values above bars",
    "Vekt-verdi": "Weight value",
    "# 5. Matematisk forklaring": "# 5. Mathematical explanation",
    "Matematisk Forklaring og Symbolsk Derivasjon": "Mathematical Explanation and Symbolic Derivation",
    "# Legg til matematiske formler": "# Add mathematical formulas",
    "FREMOVER-PASS": "FORWARD PASS",
    "TAP-FUNKSJON": "LOSS FUNCTION",
    "SYMBOLSK DERIVASJON (Kjerneregelen)": "SYMBOLIC DERIVATION (Chain Rule)",
    "For w1": "For w1",
    "For w2": "For w2",
    "For b": "For b",
    "OPPDATERING (Læringsrate α = 0.1)": "UPDATE (Learning rate α = 0.1)",
    "Ny w1": "New w1",
    "Ny w2": "New w2",
    "Ny b": "New b",
    "NY PREDIKSJON": "NEW PREDICTION",
    "# Legg til kjerneregelen som egen seksjon": "# Add chain rule as separate section",
    "KJERNEREGELEN (Chain Rule)": "THE CHAIN RULE",
    "Hvis y = f(g(x)), da er dy/dx = (dy/dg) × (dg/dx)": "If y = f(g(x)), then dy/dx = (dy/dg) × (dg/dx)",
    "I vårt tilfelle": "In our case",
    "# Kjør den forbedrede visuelle demonstrasjonen": "# Run the improved visual demonstration",
    "📊 === DETALJERT INFORMASJON ===": "📊 === DETAILED INFORMATION ===",
    "🔄 === FREMOVER-PASS ===": "🔄 === FORWARD PASS ===",
    "⬅️ === BAKOVER-PASS (GRADIENTER) ===": "⬅️ === BACKWARD PASS (GRADIENTS) ===",
    "🔄 === VEKT-OPPDATERING ===": "🔄 === WEIGHT UPDATE ===",
    "🔄 === NY PREDIKSJON ===": "🔄 === NEW PREDICTION ===",
    
    # Cell 21 - Error explanation
    "## 🤔 Hvorfor Økte Feilen etter Oppdatering?": "## 🤔 Why Did the Error Increase After the Update?",
    "Du har lagt merke til noe viktig: **Feilen økte fra 5.0 til 9.0** etter oppdatering! Dette skjer av flere grunner:": "You have noticed something important: **The error increased from 5.0 to 9.0** after the update! This happens for several reasons:",
    "### 📈 **Hva Skjedde:**": "### 📈 **What Happened:**",
    "- **Før oppdatering**: Prediksjon = 5.0, Feil = |10.0 - 5.0| = 5.0": "- **Before update**: Prediction = 5.0, Error = |10.0 - 5.0| = 5.0",
    "- **Etter oppdatering**: Prediksjon = 19.0, Feil = |10.0 - 19.0| = 9.0": "- **After update**: Prediction = 19.0, Error = |10.0 - 19.0| = 9.0",
    "### 🔍 **Hvorfor Dette Skjer:**": "### 🔍 **Why This Happens:**",
    "#### 1. **For Høy Læringsrate (α = 0.1)**": "#### 1. **Learning Rate Too High (α = 0.1)**",
    "- Læringsraten er **for stor** for dette problemet": "- The learning rate is **too large** for this problem",
    '- Nettverket tar **for store steg** og "hopper over" det optimale punktet': '- The network takes **steps that are too large** and "jumps over" the optimal point',
    "- Som å gå forbi dalen når du skal ned et fjell": "- Like walking past the valley when going down a mountain",
    "#### 2. **Gradienter er Negative**": "#### 2. **Gradients are Negative**",
    "- Alle gradienter er negative: w1=-20, w2=-30, b=-10": "- All gradients are negative: w1=-20, w2=-30, b=-10",
    "- Dette betyr at vektene må **økes** for å redusere feilen": "- This means the weights must be **increased** to reduce the error",
    "- Men vi økte dem **for mye** i ett steg": "- But we increased them **too much** in one step",
    "#### 3. **Ikke-Lineært Problem**": "#### 3. **Non-Linear Problem**",
    "- Selv om funksjonen ser lineær ut, er optimaliseringen kompleks": "- Even though the function looks linear, the optimization is complex",
    '- Store endringer kan føre til **oscillering** rundt optimum': '- Large changes can lead to **oscillation** around the optimum',
    "### 🛠️ **Hvordan Fikse Dette:**": "### 🛠️ **How to Fix This:**",
    "#### **Reduser Læringsraten:**": "#### **Reduce the Learning Rate:**",
    "- Prøv α = 0.01 i stedet for 0.1": "- Try α = 0.01 instead of 0.1",
    "- Mindre steg = mer stabil læring": "- Smaller steps = more stable learning",
    "#### **Iterativ Oppdatering:**": "#### **Iterative Update:**",
    "- Gjenta prosessen flere ganger med mindre steg": "- Repeat the process multiple times with smaller steps",
    "- Hver iterasjon vil bringe oss nærmere optimum": "- Each iteration will bring us closer to the optimum",
    "#### **Adaptive Læringsrater:**": "#### **Adaptive Learning Rates:**",
    "- Moderne algoritmer justerer læringsraten automatisk": "- Modern algorithms adjust the learning rate automatically",
    "- F.eks. Adam, RMSprop, AdaGrad": "- E.g., Adam, RMSprop, AdaGrad",
    "### 🎯 **Læring:**": "### 🎯 **Takeaway:**",
    'Dette demonstrerer at **læring i AI ikke alltid er lineær** - noen ganger må vi "gå tilbake" for å finne den beste løsningen.': 'This demonstrates that **learning in AI is not always linear** - sometimes we have to "go back" to find the best solution.',
    "**I neste iterasjon** ville nettverket justere seg i motsatt retning og gradvis finne det optimale punktet.": "**In the next iteration** the network would adjust in the opposite direction and gradually find the optimal point.",
    
    # Cell 22
    "_Forskjellen mellom gradient nedstigning og backpropagation_": "_The difference between gradient descent and backpropagation_",
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

print("Translation part 4 complete!")

