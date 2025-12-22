#!/usr/bin/env python3
"""Script to translate remaining cells (15-25) in B2-learning-in-nn.ipynb"""

import json

with open('B2-learning-in-nn.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

translations = {
    # Cell 15 - Backpropagation explanation
    "### 2. Backpropagation: Hvordan Gradienter Beregnes": "### 2. Backpropagation: How Gradients Are Calculated",
    "#### Hva er Backpropagation?": "#### What is Backpropagation?",
    "**Backpropagation** (bakover-propagering) er algoritmen som lar nevrale nettverk lære. Den beregner hvordan hver vekt i nettverket påvirker den totale feilen, slik at vi kan justere vektene for å gjøre nettverket bedre.": "**Backpropagation** (backward propagation) is the algorithm that allows neural networks to learn. It calculates how each weight in the network affects the total error, so we can adjust the weights to make the network better.",
    "#### Medisinsk Analogi: Feilretting i Diagnostikk": "#### Medical Analogy: Error Correction in Diagnostics",
    "Tenk deg at du som lege har gitt en feil diagnose:": "Imagine that you as a doctor have given an incorrect diagnosis:",
    "- **Fremover-pass** = Gjennomfør diagnostisk prosess": "- **Forward pass** = Carry out diagnostic process",
    "- **Beregn feil** = Sammenlign din diagnose med sannheten": "- **Calculate error** = Compare your diagnosis with the truth",
    "- **Bakover-pass** = Analyser hvilke faktorer som førte til feilen": "- **Backward pass** = Analyze which factors led to the error",
    "- **Juster** = Endre diagnostiske kriterier for fremtiden": "- **Adjust** = Change diagnostic criteria for the future",
    "#### Kjerneprinsippet: Kjerneregelen": "#### Core Principle: The Chain Rule",
    "Backpropagation bruker **kjerneregelen** fra kalkulus for å beregne gradienter:": "Backpropagation uses the **chain rule** from calculus to calculate gradients:",
    "##### Hva Betyr Dette?": "##### What Does This Mean?",
    "- **∂L/∂w** = Hvor mye feilen endres når vi endrer vekten w": "- **∂L/∂w** = How much the error changes when we change weight w",
    "- **∂L/∂y** = Hvor mye feilen endres når output endres": "- **∂L/∂y** = How much the error changes when output changes",
    "- **∂y/∂z** = Hvor mye output endres når aktivering endres": "- **∂y/∂z** = How much output changes when activation changes",
    "- **∂z/∂w** = Hvor mye aktivering endres når vekt endres": "- **∂z/∂w** = How much activation changes when weight changes",
    "##### Medisinsk Eksempel": "##### Medical Example",
    "Hvis en AI-modell feilklassifiserer en pasient:": "If an AI model misclassifies a patient:",
    "- **∂L/∂w** = Hvor mye feilen reduseres hvis vi endrer diagnostiske kriterier": "- **∂L/∂w** = How much the error decreases if we change diagnostic criteria",
    "- **∂L/∂y** = Hvor mye feilen endres hvis vi endrer sannsynlighet for sykdom": "- **∂L/∂y** = How much the error changes if we change probability of disease",
    "- **∂y/∂z** = Hvor mye sannsynlighet endres hvis vi endrer nevron-aktivering": "- **∂y/∂z** = How much probability changes if we change neuron activation",
    "- **∂z/∂w** = Hvor mye aktivering endres hvis vi endrer vekter": "- **∂z/∂w** = How much activation changes if we change weights",
    "#### Detaljert Trinn-for-Trinn": "#### Detailed Step-by-Step",
    "##### 1. **Fremover-pass**: Beregn alle mellomverdier": "##### 1. **Forward pass**: Calculate all intermediate values",
    "- **Input** → **Skjult lag 1** → **Skjult lag 2** → **Output**": "- **Input** → **Hidden layer 1** → **Hidden layer 2** → **Output**",
    "- Hver nevron beregner: `aktivering = f(vekter × input + bias)`": "- Each neuron calculates: `activation = f(weights × input + bias)`",
    "- **Medisinsk**: Hver diagnostisk faktor vurderes og kombineres": "- **Medical**: Each diagnostic factor is evaluated and combined",
    "##### 2. **Beregn output-feil**: ∂L/∂y": "##### 2. **Calculate output error**: ∂L/∂y",
    "- Sammenlign prediksjon med sann verdi": "- Compare prediction with true value",
    "- **Medisinsk**: Sammenlign AI-diagnose med faktisk diagnose": "- **Medical**: Compare AI diagnosis with actual diagnosis",
    "- **Eksempel**: Hvis AI sa 80% sannsynlighet for sykdom, men pasienten var frisk": "- **Example**: If AI said 80% probability of disease, but the patient was healthy",
    "##### 3. **Bakover gjennom hvert lag**: Bruk kjerneregelen": "##### 3. **Backward through each layer**: Use the chain rule",
    "- **Fra output til skjult lag 2**: Hvor mye påvirket hver nevron i lag 2 feilen?": "- **From output to hidden layer 2**: How much did each neuron in layer 2 affect the error?",
    "- **Fra skjult lag 2 til skjult lag 1**: Hvor mye påvirket hver nevron i lag 1 feilen?": "- **From hidden layer 2 to hidden layer 1**: How much did each neuron in layer 1 affect the error?",
    "- **Fra skjult lag 1 til input**: Hvor mye påvirket hver input-feature feilen?": "- **From hidden layer 1 to input**: How much did each input feature affect the error?",
    "##### 4. **Oppdater vekter**: Bruk gradientene": "##### 4. **Update weights**: Use the gradients",
    "- **Ny vekt = Gammel vekt - læringsrate × gradient**": "- **New weight = Old weight - learning rate × gradient**",
    "- **Medisinsk**: Juster diagnostiske kriterier basert på feilanalyse": "- **Medical**: Adjust diagnostic criteria based on error analysis",
    "#### Biologisk Inspirasjon": "#### Biological Inspiration",
    "**Hvordan Hjernen Gjør Det**": "**How the Brain Does It**",
    "1. **Synaptisk Plastisitet**: Synapser endres basert på aktivitet": "1. **Synaptic Plasticity**: Synapses change based on activity",
    "2. **Error Signal**: Feil-signaler sendes bakover gjennom nevrale kretser (*)": "2. **Error Signal**: Error signals are sent backward through neural circuits (*)",
    "3. **LTP/LTD**: Synapser forsterkes eller svekkes basert på feil": "3. **LTP/LTD**: Synapses strengthen or weaken based on error",
    "4. **Konsolidering**: Endringer lagres i langtidsminne": "4. **Consolidation**: Changes are stored in long-term memory",
    "##### (*) Konkrete Eksempler på Feil-signaler i Hjernen": "##### (*) Concrete Examples of Error Signals in the Brain",
    "##### 1. **Lillehjernen (Cerebellum) - Motorisk Læring**": "##### 1. **Cerebellum - Motor Learning**",
    "**Hvordan det fungerer:**": "**How it works:**",
    "- **Input**: Planlagt bevegelse fra motorcortex": "- **Input**: Planned movement from motor cortex",
    "- **Sammenligning**: Faktisk bevegelse fra proprioceptive sensorer": "- **Comparison**: Actual movement from proprioceptive sensors",
    "- **Feil-signal**: Forskjell mellom planlagt og faktisk bevegelse": "- **Error signal**: Difference between planned and actual movement",
    "- **Korreksjon**: Justerer bevegelsen for neste gang": "- **Correction**: Adjusts the movement for next time",
    "**Medisinsk eksempel:**": "**Medical example:**",
    "- **Ataksi**: Skade på lillehjernen → dårlig koordinering": "- **Ataxia**: Damage to cerebellum → poor coordination",
    "- **Rehabilitering**: Repetitiv trening → lillehjernen lærer nye bevegelser": "- **Rehabilitation**: Repetitive training → cerebellum learns new movements",
    "- **Parkinson**: Dopamin-mangel → dårlige feil-signaler": "- **Parkinson's**: Dopamine deficiency → poor error signals",
    "**Klinisk relevans:**": "**Clinical relevance:**",
    "- **Fysioterapi**: Bruker lillehjernens læringsmekanisme": "- **Physiotherapy**: Uses the cerebellum's learning mechanism",
    "- **Prostetikk**: Hjernen må lære nye bevegelsesmønstre": "- **Prosthetics**: The brain must learn new movement patterns",
    "- **Medikamenter**: Dopamin-agonister forbedrer feil-signaler": "- **Medications**: Dopamine agonists improve error signals",
    "##### 2. **Basal Ganglia - Belønning og Straff**": "##### 2. **Basal Ganglia - Reward and Punishment**",
    '- **Dopamin**: "Belønning" når handlingen er riktig': '- **Dopamine**: "Reward" when the action is correct',
    "- **Feil-signal**: Redusert dopamin når handlingen er feil": "- **Error signal**: Reduced dopamine when the action is wrong",
    "- **Læring**: Sterkere forbindelser for belønnede handlinger": "- **Learning**: Stronger connections for rewarded actions",
    "- **Parkinson**: Redusert dopamin → dårlig læring": "- **Parkinson's**: Reduced dopamine → poor learning",
    "- **Tourette**: Forstyrret dopamin → uønskede bevegelser": "- **Tourette's**: Disturbed dopamine → unwanted movements",
    "- **Avhengighet**: Overaktive belønningskretser": "- **Addiction**: Overactive reward circuits",
    "- **Atferdsterapi**: Bruker belønningsmekanismer": "- **Behavioral therapy**: Uses reward mechanisms",
    "- **Medikamenter**: Dopamin-modulerende stoffer": "- **Medications**: Dopamine-modulating substances",
    "- **Stimulering**: DBS for å forbedre signaler": "- **Stimulation**: DBS to improve signals",
    "##### 3. **Hippocampus - Episodisk Minne**": "##### 3. **Hippocampus - Episodic Memory**",
    "- **Input**: Sensorisk informasjon fra neocortex": "- **Input**: Sensory information from neocortex",
    "- **Sammenligning**: Eksisterende minner": "- **Comparison**: Existing memories",
    "- **Feil-signal**: Ny informasjon som ikke matcher": "- **Error signal**: New information that doesn't match",
    "- **Konsolidering**: Lagrer nye minner": "- **Consolidation**: Stores new memories",
    "- **Alzheimer**: Skade på hippocampus → dårlig minne": "- **Alzheimer's**: Damage to hippocampus → poor memory",
    "- **PTSD**: Forstyrret konsolidering av traumatiske minner": "- **PTSD**: Disturbed consolidation of traumatic memories",
    "- **Epilepsi**: Temporal lobe-epilepsi påvirker minne": "- **Epilepsy**: Temporal lobe epilepsy affects memory",
    "- **Minnetrening**: Stimulerer hippocampus": "- **Memory training**: Stimulates hippocampus",
    "- **Medikamenter**: Acetylcholin-esterase-hemmere": "- **Medications**: Acetylcholinesterase inhibitors",
    "- **Terapi**: Eksponeringsterapi for PTSD": "- **Therapy**: Exposure therapy for PTSD",
    "##### 4. **Prefrontal Cortex - Kognitiv Kontroll**": "##### 4. **Prefrontal Cortex - Cognitive Control**",
    "- **Monitoring**: Overvåker pågående oppgaver": "- **Monitoring**: Monitors ongoing tasks",
    "- **Feil-signal**: Oppdager når noe går galt": "- **Error signal**: Detects when something goes wrong",
    "- **Korreksjon**: Justerer oppmerksomhet og strategi": "- **Correction**: Adjusts attention and strategy",
    "- **ADHD**: Dårlig feil-deteksjon → impulsivitet": "- **ADHD**: Poor error detection → impulsivity",
    "- **Schizofreni**: Forstyrret monitoring → vrangforestillinger": "- **Schizophrenia**: Disturbed monitoring → delusions",
    "- **Depresjon**: Negativ feil-bias → pessimisme": "- **Depression**: Negative error bias → pessimism",
    "- **Kognitiv trening**: Forbedrer monitoring": "- **Cognitive training**: Improves monitoring",
    "- **Medikamenter**: Stimulanter for ADHD": "- **Medications**: Stimulants for ADHD",
    "- **Terapi**: CBT for å endre feil-tolkning": "- **Therapy**: CBT to change error interpretation",
    "##### Sammenligning: Biologisk vs Kunstig Feil-signal": "##### Comparison: Biological vs Artificial Error Signal",
    "| **Kilde** | Sensorer, minne, belønning | Sann verdi vs prediksjon |": "| **Source** | Sensors, memory, reward | True value vs prediction |",
    "| **Transport** | Kjemiske signaler | Matematiske beregninger |": "| **Transport** | Chemical signals | Mathematical calculations |",
    "| **Tidsskala** | Millisekunder til sekunder | Mikrosekunder |": "| **Time scale** | Milliseconds to seconds | Microseconds |",
    "| **Adaptabilitet** | Høy (plastisitet) | Varierende |": "| **Adaptability** | High (plasticity) | Varying |",
    "| **Robusthet** | Høy (tolererer feil) | Kan være følsom |": "| **Robustness** | High (tolerates errors) | Can be sensitive |",
    "##### Klinisk Betydning": "##### Clinical Significance",
    "**For medisinere:**": "**For physicians:**",
    "- **Forståelse**: Hvordan hjernen lærer og tilpasser seg": "- **Understanding**: How the brain learns and adapts",
    "- **Diagnostikk**: Feil i feil-signaler kan indikere sykdom": "- **Diagnostics**: Errors in error signals can indicate disease",
    "- **Behandling**: Målrettede intervensjoner for å forbedre læring": "- **Treatment**: Targeted interventions to improve learning",
    "- **Rehabilitering**: Bruk av hjernens læringsmekanismer": "- **Rehabilitation**: Use of the brain's learning mechanisms",
    "##### Praktiske Eksempler": "##### Practical Examples",
    "##### Medisinsk Diagnose": "##### Medical Diagnosis",
    "- **Input**: Symptomer, laboratorieverdier, bilder": "- **Input**: Symptoms, laboratory values, images",
    "- **Skjulte lag**: Kombinasjoner av symptomer, risikofaktorer": "- **Hidden layers**: Combinations of symptoms, risk factors",
    "- **Output**: Sannsynlighet for sykdom": "- **Output**: Probability of disease",
    "- **Backpropagation**: Hvilke symptomer var viktigst for riktig diagnose?": "- **Backpropagation**: Which symptoms were most important for correct diagnosis?",
    "##### Behandlingsanbefaling": "##### Treatment Recommendation",
    "- **Input**: Diagnose, pasienthistorie, kontraindikasjoner": "- **Input**: Diagnosis, patient history, contraindications",
    "- **Skjulte lag**: Behandlingskombinasjoner, doseringsregler": "- **Hidden layers**: Treatment combinations, dosing rules",
    "- **Output**: Anbefalt behandling": "- **Output**: Recommended treatment",
    "- **Backpropagation**: Hvilke faktorer førte til best behandlingsresultat?": "- **Backpropagation**: Which factors led to the best treatment outcome?",
    "#### PyTorch Gjør Dette Automatisk!": "#### PyTorch Does This Automatically!",
    "Med `autograd` beregner PyTorch gradienter automatisk når vi kaller `.backward()`.": "With `autograd`, PyTorch calculates gradients automatically when we call `.backward()`.",
    "##### Hvorfor Dette er Viktig": "##### Why This is Important",
    "- **Automatisk differensiering**: Ingen manuell beregning av derivater": "- **Automatic differentiation**: No manual calculation of derivatives",
    "- **Effektivitet**: Optimalisert for moderne hardware": "- **Efficiency**: Optimized for modern hardware",
    "- **Fleksibilitet**: Fungerer med komplekse nettverksarkitekturer": "- **Flexibility**: Works with complex network architectures",
    "- **Feilsikkerhet**: Reduserer risiko for feil i gradientberegninger": "- **Error safety**: Reduces risk of errors in gradient calculations",
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

print("Translation part 3 complete!")

