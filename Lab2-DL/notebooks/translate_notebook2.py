#!/usr/bin/env python3
"""Script to translate remaining cells in B2-learning-in-nn.ipynb from Norwegian to English"""

import json

# Read the notebook
with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Additional translation dictionary
translations = {
    # Cell 1 - Code comments
    "# Importer nødvendige biblioteker": "# Import necessary libraries",
    "# Sett opp plotting": "# Set up plotting",
    "🎓 Klar for læring i nevrale nettverk!": "🎓 Ready for learning in neural networks!",
    "CUDA tilgjengelig": "CUDA available",
    "MPS tilgjengelig": "MPS available",
    
    # Cell 3 - Gradient Descent
    "## 3. Gradient Nedstigning: Veien til optimalisering og \"motoren\" i AI-læring": "## 3. Gradient Descent: The Path to Optimization and the \"Engine\" of AI Learning",
    "### Intuisjon: Å Finne Det Laveste Punktet": "### Intuition: Finding the Lowest Point",
    "Tenk deg at du er blindfoldet på en fjelltopp og skal finne dalen. Du kan:": "Imagine you are blindfolded on a mountaintop and need to find the valley. You can:",
    "1. **Føle terrenget** rundt deg (beregne gradient)": "1. **Feel the terrain** around you (calculate gradient)",
    "2. **Gå i retning** som går nedover (oppdater vekter)": "2. **Walk in the direction** that goes downhill (update weights)",
    "3. **Gjenta** til du når bunnen (konvergens)": "3. **Repeat** until you reach the bottom (convergence)",
    "Dette er nøyaktig det gradient descent gjør!": "This is exactly what gradient descent does!",
    "### Matematisk Forståelse": "### Mathematical Understanding",
    "**Gradient** = retningen med størst stigning": "**Gradient** = the direction with greatest slope",
    "**Gradient Nedstigning** = gå i motsatt retning (nedover)": "**Gradient Descent** = go in the opposite direction (downhill)",
    "- **α** (alpha) = læringsrate (stegstørrelse)": "- **α** (alpha) = learning rate (step size)",
    "- **∇L(θ)** = gradient (retning)": "- **∇L(θ)** = gradient (direction)",
    "- **-** = gå i motsatt retning": "- **-** = go in the opposite direction",
    
    # Cell 4
    "_Visualisering av gradient nedstigning langs én dimensjon_": "_Visualization of gradient descent along one dimension_",
    
    # Cell 5 - Code
    "# Visualiser gradient descent på en enkel funksjon": "# Visualize gradient descent on a simple function",
    "# Definer en enkel funksjon": "# Define a simple function",
    "# Gradient descent simulering": "# Gradient descent simulation",
    "# Startpunkt": "# Starting point",
    "# Beregn gradient": "# Calculate gradient",
    "# Oppdater x": "# Update x",
    "# Plot resultatet": "# Plot the result",
    "# Legg til piler for å vise retning": "# Add arrows to show direction",
    "# Marker minimum": "# Mark minimum",
    "Gradient Nedstigning: Finne Minimum": "Gradient Descent: Finding Minimum",
    "Globalt minimum": "Global minimum",
    "Startpunkt": "Starting point",
    "Sluttpunkt": "Endpoint",
    "Optimalt": "Optimal",
    
    # Cell 6
    "_3D visualisering av gradient nedstigning i to dimensjoner_": "_3D visualization of gradient descent in two dimensions_",
    
    # Cell 7
    "### Gradient Nedstigning i 2D: Fra Fjell til Dal": "### Gradient Descent in 2D: From Mountain to Valley",
    "I virkeligheten har nevrale nettverk tusenvis av parametere, ikke bare én. La oss se hvordan gradient nedstigning fungerer i to dimensjoner:": "In reality, neural networks have thousands of parameters, not just one. Let's see how gradient descent works in two dimensions:",
    "#### Hva Skjer i 2D?": "#### What Happens in 2D?",
    "**Merk**: 2D refererer til parameterrommet: input-dimensjonene (x,y), ikke visualiseringen som er 3D plot av 2D funksjon (høyde z=f(x,y) som tredje dimensjon)": "**Note**: 2D refers to the parameter space: the input dimensions (x,y), not the visualization which is a 3D plot of a 2D function (height z=f(x,y) as the third dimension)",
    "- **Gradient** blir en vektor": "- **Gradient** becomes a vector",
    "- **Retning** viser hvor terrenget stiger mest": "- **Direction** shows where the terrain rises most",
    "- **Størrelse** viser hvor bratt det er": "- **Magnitude** shows how steep it is",
    "- **Oppdatering**": "- **Update**",
    "#### Geografisk Analogi": "#### Geographic Analogy",
    "Tenk deg at du er på en fjelltopp og skal finne dalen:": "Imagine you are on a mountaintop and need to find the valley:",
    "- **Gradient** = retningen med størst stigning": "- **Gradient** = the direction with greatest slope",
    "- **Gradient Nedstigning** = gå i motsatt retning": "- **Gradient Descent** = go in the opposite direction",
    "- **Læringsrate** = hvor store steg du tar": "- **Learning rate** = how large steps you take",
    "- **Minimum** = dalen (optimal løsning)": "- **Minimum** = the valley (optimal solution)",
    "#### Visualisering": "#### Visualization",
    "Nedenfor ser du to visualiseringer:": "Below you see two visualizations:",
    "1. **Konturplot**: Som et topografisk kart med høydelinjer": "1. **Contour plot**: Like a topographic map with elevation lines",
    "2. **3D Overflate**: Som et faktisk fjell med dal": "2. **3D Surface**: Like an actual mountain with a valley",
    
    # Cell 8 - Code
    '"""Visualiser gradient descent på en 2D funksjon"""': '"""Visualize gradient descent on a 2D function"""',
    "# Definer en 2D funksjon": "# Define a 2D function",
    "# Dette har minimum ved": "# This has minimum at",
    "# Lag et grid for plotting": "# Create a grid for plotting",
    "# Lagre historie": "# Store history",
    "# Beregn gradient": "# Calculate gradient",
    "# Oppdater posisjon": "# Update position",
    "# Plot 1: Konturplot med gradient descent": "# Plot 1: Contour plot with gradient descent",
    "# Plot gradient descent path": "# Plot gradient descent path",
    "# Marker start og slutt": "# Mark start and end",
    "Gradient Nedstigning i 2D: Konturplot": "Gradient Descent in 2D: Contour Plot",
    "# Plot 2: 3D overflateplot": "# Plot 2: 3D surface plot",
    "# Plot gradient descent path på overflaten": "# Plot gradient descent path on the surface",
    "Gradient Nedstigning i 2D: 3D Overflate": "Gradient Descent in 2D: 3D Surface",
    "# Print resultater": "# Print results",
    "=== Gradient Nedstigning i 2D ===": "=== Gradient Descent in 2D ===",
    "Antall iterasjoner": "Number of iterations",
    "Læringsrate": "Learning rate",
    
    # Cell 9
    "_Visualisering av en mer kompleks flate med illustrasjon av gradient nedstigning_": "_Visualization of a more complex surface with illustration of gradient descent_",
    
    # Cell 10 - Code
    "# Finn det globale minimum numerisk": "# Find the global minimum numerically",
    "# Generer data for overflateplottet": "# Generate data for the surface plot",
    "# Opprett figur og 3D-akse": "# Create figure and 3D axis",
    "# Plot overflaten": "# Plot the surface",
    "# Justert læringsrate": "# Adjusted learning rate",
    "# Økt antall iterasjoner": "# Increased number of iterations",
    "# Interpoler banen for å få 25 ekvidistante punkter": "# Interpolate the path to get 25 equidistant points",
    "# Plot gradient descent banen": "# Plot gradient descent path",
    "# Plot ekvidistante punkter": "# Plot equidistant points",
    "# Marker start- og sluttpunkt": "# Mark start and end points",
    "# Marker globalt minimum": "# Mark global minimum",
    "# Legg til koordinater som tekst": "# Add coordinates as text",
    "# Legg til tekstboks for å forklare optimeringsproblemet": "# Add text box to explain the optimization problem",
    "# Legg til tittel og etiketter": "# Add title and labels",
    "Optimering med Gradient Nedstigning": "Optimization with Gradient Descent",
    "# Legg til fargelinjen": "# Add the colorbar",
    "Funksjonsverdi": "Function value",
    "# Roter figuren for bedre visning": "# Rotate the figure for better viewing",
    "# Skriv figuren til en png-fil": "# Write the figure to a png file",
    "# Vis objekt-funksjonen i LaTeX-format": "# Show the objective function in LaTeX format",
    "=== Objekt-funksjonen (tap funksjon) ===": "=== Objective function (loss function) ===",
    "Start": "Start",
    "Slutt": "End",
    "Globalt Minimum": "Global Minimum",
    
    # Cell 11
    "LaTeX-formatering:": "LaTeX formatting:",
    
    # Cell 13
    "## 4. Backpropagation: Hvordan Gradienter Beregnes (Bakover-propagering av Feil)": "## 4. Backpropagation: How Gradients Are Calculated (Backward Propagation of Errors)",
    
    # Cell 14
    "### Historisk Utvikling av Backpropagation": "### Historical Development of Backpropagation",
    "#### - De Tidlige Årene (1940-1960)": "#### - The Early Years (1940-1960)",
    "Første matematiske modell av nevroner": "First mathematical model of neurons",
    "Viste at nevrale nettverk kan beregne logiske funksjoner": "Showed that neural networks can compute logical functions",
    "Grunnlaget for moderne nevrale nettverk": "Foundation for modern neural networks",
    "Utviklet Perceptron-algoritmen": "Developed the Perceptron algorithm",
    "Kunne lære enkle klassifikasjonsoppgaver": "Could learn simple classification tasks",
    "**Begrensning**: Kun lineært separerbare problemer": "**Limitation**: Only linearly separable problems",
    "#### - Gjennombruddet (1960-1980)": "#### - The Breakthrough (1960-1980)",
    "Første som beskrev backpropagation-algoritmen": "First to describe the backpropagation algorithm",
    "Doktorgradsarbeid ved Harvard University": "Doctoral work at Harvard University",
    "**Problemet**: Arbeidet ble ikke anerkjent på den tiden": "**Problem**: The work was not recognized at the time",
    "Gjenoppdaget og populariserte backpropagation": "Rediscovered and popularized backpropagation",
    '**Gjennombrudd**: Viste at algoritmen kunne løse komplekse problemer': '**Breakthrough**: Showed that the algorithm could solve complex problems',
    "#### - Moderne Utvikling (1980-2020)": "#### - Modern Development (1980-2020)",
    "Utviklet Convolutional Neural Networks (CNN)": "Developed Convolutional Neural Networks (CNN)",
    "Backpropagation for bildebehandling": "Backpropagation for image processing",
    "**Praktisk anvendelse**: Håndskrift-gjenkjenning": "**Practical application**: Handwriting recognition",
    "Viste at dype nettverk kunne lære": "Showed that deep networks could learn",
    "Backpropagation med mange lag": "Backpropagation with many layers",
    "**Gjennombrudd**: ImageNet-konkurransen (2012)": "**Breakthrough**: ImageNet competition (2012)",
    "### Backpropagation i Biologiske Systemer?": "### Backpropagation in Biological Systems?",
    "#### Kort Svar: **NEI, men...**": "#### Short Answer: **NO, but...**",
    "Det er **ikke** holdepunkter for at backpropagation, som vi kjenner den fra AI, brukes i biologiske systemer, men det finnes relaterte mekanismer.": "There is **no** evidence that backpropagation, as we know it from AI, is used in biological systems, but there are related mechanisms.",
    "#### Hvorfor Ikke i Biologien?": "#### Why Not in Biology?",
    "**1. Matematiske Krav**": "**1. Mathematical Requirements**",
    "- Krever **kontinuerlig deriverbarhet** av alle funksjoner": "- Requires **continuous differentiability** of all functions",
    "- Biologiske systemer er **diskret** og **stokastiske**": "- Biological systems are **discrete** and **stochastic**",
    '- **Synapser** kan ikke "beregne deriverte"': '- **Synapses** cannot "calculate derivatives"',
    "**2. Informasjonsflyt**": "**2. Information Flow**",
    "- Backpropagation krever **feil-signaler** som sendes bakover": "- Backpropagation requires **error signals** sent backwards",
    "- Biologiske nevroner sender  **forward-signaler**": "- Biological neurons send **forward signals**",
    '- **Ingen direkte "backward-pass"** i hjernen': '- **No direct "backward pass"** in the brain',
    "**3. Tidsaspekt**": "**3. Time Aspect**",
    "- Backpropagation krever **synkronisert** beregning": "- Backpropagation requires **synchronized** computation",
    "- Biologiske systemer er **asynkrone** og **parallell**": "- Biological systems are **asynchronous** and **parallel**",
    "- **Tidsskala** er helt forskjellig": "- **Time scale** is completely different",
    "#### Hva Bruker Hjernen I Stedet?": "#### What Does the Brain Use Instead?",
    "**1. Synaptisk Plastisitet**": "**1. Synaptic Plasticity**",
    '- **Hebb\'s regel**: "Nevroner som fyrer sammen, kobles sammen"': '- **Hebb\'s rule**: "Neurons that fire together, wire together"',
    "- **LTP/LTD**: Synapser forsterkes/svekkes basert på aktivitet": "- **LTP/LTD**: Synapses strengthen/weaken based on activity",
    "- **Spike-timing dependent plasticity (STDP)**": "- **Spike-timing dependent plasticity (STDP)**",
    "**2. Lokal Læring**": "**2. Local Learning**",
    "- Hver synapse lærer **uavhengig** av andre": "- Each synapse learns **independently** of others",
    "- **Ingen global koordinering** som backpropagation": "- **No global coordination** like backpropagation",
    '- **Dopamin** og andre signalstoffer som "belønning"': '- **Dopamine** and other signaling molecules as "reward"',
    "**3. Konkurranse og Seleksjon**": "**3. Competition and Selection**",
    "- **Neural Darwinism**: Sterke forbindelser overlever": "- **Neural Darwinism**: Strong connections survive",
    "- **Pruning**: Svake forbindelser fjernes": "- **Pruning**: Weak connections are removed",
    "- **Neurogenese**: Nye nevroner dannes": "- **Neurogenesis**: New neurons are formed",
    "#### Moderne Forskning: Biologisk Inspirerte Algoritmer": "#### Modern Research: Biologically Inspired Algorithms",
    "**1. Feedback Alignment (2016)**": "**1. Feedback Alignment (2016)**",
    "- Bruker **tilfeldige** feedback-vekter": "- Uses **random** feedback weights",
    "- **Ikke** den samme algoritmen, men inspirert av biologien": "- **Not** the same algorithm, but inspired by biology",
    "- Viser at eksakt backpropagation ikke er nødvendig": "- Shows that exact backpropagation is not necessary",
    "**2. Target Propagation**": "**2. Target Propagation**",
    "- Bruker **målrettede** signaler i stedet for gradienter": "- Uses **targeted** signals instead of gradients",
    "- Mer biologisk plausibel": "- More biologically plausible",
    "- **Forskningsområde**: Hvordan kan hjernen lære uten backpropagation?": "- **Research area**: How can the brain learn without backpropagation?",
    "**3. Spiking Neural Networks**": "**3. Spiking Neural Networks**",
    "- Modellerer **spike-baserte** nevroner": "- Models **spike-based** neurons",
    "- Mer realistisk biologisk modell": "- More realistic biological model",
    "- **Utfordring**: Vanskelig å trene": "- **Challenge**: Difficult to train",
    "**Hvorfor Dette er Viktig for Helsepersonell:**": "**Why This is Important for Healthcare Professionals:**",
    "1. **Forståelse av AI-grenser**": "1. **Understanding AI limitations**",
    "   - AI er **ikke** en kopi av hjernen": "   - AI is **not** a copy of the brain",
    "   - **Forskjellige** læringsmekanismer": "   - **Different** learning mechanisms",
    "   - **Komplementære** til menneskelig intelligens": "   - **Complementary** to human intelligence",
    "2. **Fremtidige Utviklinger**": "2. **Future Developments**",
    "   - **Biologisk inspirerte** algoritmer kan være bedre": "   - **Biologically inspired** algorithms may be better",
    "   - **Mer robuste** og **energieffektive** systemer": "   - **More robust** and **energy-efficient** systems",
    "   - **Bedre** for applikasjoner innen medisin og helse": "   - **Better** for medical and health applications",
    "3. **Etiske Implikasjoner**": "3. **Ethical Implications**",
    "   - AI er **ikke** menneskelig intelligens": "   - AI is **not** human intelligence",
    "   - **Forskjellige** styrker og svakheter": "   - **Different** strengths and weaknesses",
    "   - **Viktig** for klinisk beslutningstaking": "   - **Important** for clinical decision-making",
    "#### Konklusjon": "#### Conclusion",
    "Backpropagation er en **kunstig** algoritme som ikke finnes i biologien, men:": "Backpropagation is an **artificial** algorithm that does not exist in biology, but:",
    "- **Inspirert** av biologiske prinsipper": "- **Inspired** by biological principles",
    "- **Komplementær** til biologisk læring": "- **Complementary** to biological learning",
    "- **Viktig** for å forstå AI-grenser": "- **Important** for understanding AI limitations",
    "- **Relevant** for fremtidige medisinske applikasjoner": "- **Relevant** for future medical applications",
    "**For medisinere og helserbeidere**: Dette hjelper å forstå at AI er et **verktøy**, ikke en erstatning for menneskelig klinisk vurdering.": "**For physicians and healthcare workers**: This helps understand that AI is a **tool**, not a replacement for human clinical judgment.",
}

def translate_cell(cell_content):
    """Translate Norwegian content to English"""
    result = cell_content
    for norwegian, english in translations.items():
        result = result.replace(norwegian, english)
    return result

# Process each cell
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

# Save the translated notebook
with open('B2-learning-in-nn.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print("Translation part 2 complete!")

