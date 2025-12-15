#!/usr/bin/env python3
"""
Comprehensive translation script for BMED365 Beamer presentations.
Translates Norwegian text to English while preserving LaTeX structure.
"""

import re
import os
from pathlib import Path

# Comprehensive Norwegian to English translation dictionary
TRANSLATIONS = {
    # Package configuration
    r'\[norsk\]': '[english]',
    
    # LaTeX comments (Norwegian)
    '% PAKKER': '% PACKAGES',
    '% TEMA OG FARGER': '% THEME AND COLORS',
    '% TITTELINFO': '% TITLE INFO',
    '% DOKUMENT': '% DOCUMENT',
    '% SEKSJON': '% SECTION',
    '% OPPSUMMERING': '% SUMMARY',
    '% Farger for TikZ-diagrammer': '% Colors for TikZ diagrams',
    '% Kodeformatering': '% Code formatting',
    
    # Section titles
    'Bioethics og AI': 'Bioethics and AI',
    'Fundamental graph theory': 'Fundamental Graph Theory',
    'Sentralitetsmål': 'Centrality Measures',
    'Community detection og verktøy': 'Community Detection and Tools',
    'Likhetsberegning': 'Similarity Calculation',
    'Analyse av PSN': 'Analysis of PSN',
    'Fundamental om PSN': 'Fundamentals of PSN',
    'Advanced temaer': 'Advanced Topics',
    'Fundamental paradigmer': 'Fundamental Paradigms',
    'Knowledge Grapher og ontologier': 'Knowledge Graphs and Ontologies',
    'Case: Gliomdiagnose': 'Case: Glioma Diagnosis',
    'Case: Neurosymbolic gliomdiagnose': 'Case: Neurosymbolic Glioma Diagnosis',
    'Menneske-maskin samspill': 'Human-Machine Interaction',
    'Sikkerhetstrusler': 'Security Threats',
    'Robustness og usikkerhet': 'Robustness and Uncertainty',
    'Typer explainability': 'Types of Explainability',
    'Limitations og utfordringer': 'Limitations and Challenges',
    'Validation og modelltyper': 'Validation and Model Types',
    
    # Common Norwegian words/phrases to English
    'What is': 'What is',
    'What is en': 'What is a',
    'What is et': 'What is a',
    'Why viktig': 'Why important',
    'Why er': 'Why is',
    'Why fungerer': 'Why does it work',
    'Why dette': 'Why this',
    'Why explainability': 'Why explainability',
    'How vet vi': 'How do we know',
    'How det fungerer': 'How it works',
    'How SHAP fungerer': 'How SHAP works',
    'How RAG fungerer': 'How RAG works',
    
    # Frame titles (Norwegian verbs to English)
    'Explain ': 'Explain ',
    'Describe ': 'Describe ',
    'Define ': 'Define ',
    'Know about ': 'Know about ',
    'Discuss ': 'Discuss ',
    'Apply ': 'Apply ',
    'Calculate ': 'Calculate ',
    'Understand ': 'Understand ',
    'Interpret ': 'Interpret ',
    'Compare ': 'Compare ',
    
    # Common Norwegian phrases
    'på et overordnet nivå': 'at a high level',
    'på et konseptuelt nivå': 'at a conceptual level',
    'i medisinsk kontekst': 'in a medical context',
    'i medisinsk image analysis': 'in medical image analysis',
    'i AI-kontekst': 'in an AI context',
    'i helsevesenet': 'in healthcare',
    'iht.': 'according to',
    'f.eks.': 'e.g.',
    'dvs.': 'i.e.',
    'm.h.p.': 'with respect to',
    'ors': 'otherwise',
    'or ': 'or ',
    'og dens': 'and its',
    'og deres': 'and their',
    
    # Norwegian nouns and technical terms
    'Noder og kanter': 'Nodes and Edges',
    'Rettet vs. ikke-rettet graf': 'Directed vs. Undirected Graph',
    'Vektet vs. ikke-vektet graf': 'Weighted vs. Unweighted Graph',
    'Nabomatrise': 'Adjacency Matrix',
    'grad-sentralitet': 'degree centrality',
    'mellomliggenhet': 'betweenness',
    'egenvektor-sentralitet': 'eigenvector centrality',
    'klyngekoeffisient': 'clustering coefficient',
    'terskelverdi': 'threshold value',
    'terskelvalg': 'threshold selection',
    'kantoppretting': 'edge creation',
    'pasientsubgrupper': 'patient subgroups',
    'precisionsmedisin': 'precision medicine',
    'likhetsberegning': 'similarity calculation',
    
    # Norwegian article/pronoun replacements
    'hva en ': 'what a ',
    'hva et ': 'what a ',
    'hvorfor ': 'why ',
    'hvordan ': 'how ',
    'hvilke ': 'which ',
    'hvilken ': 'which ',
    
    # Verbs and verb phrases
    'konseptet ': 'the concept of ',
    'konseptuelt': 'conceptual',
    'kontrastere ': 'contrast ',
    'skille mellom ': 'distinguish between ',
    'skille fra ': 'distinguish from ',
    'identifisere ': 'identify ',
    'reflektere over ': 'reflect on ',
    'konstruere ': 'construct ',
    'velge ': 'choose ',
    
    # Common blocks
    'Utfordring': 'Challenge',
    'Utfordringen': 'The challenge',
    'Konsekvens': 'Consequence',
    'Løsningen': 'The solution',
    'Løsning': 'Solution',
    'Hovedidé': 'Main idea',
    'Hovedbudskap': 'Key message',
    'Praktisk betydning': 'Practical significance',
    'Historisk perspektiv': 'Historical perspective',
    'Teknologier': 'Technologies',
    'Nøkkelbegreper': 'Key concepts',
    'Nøkkelkrav': 'Key requirements',
    'Tommelfingerregel': 'Rule of thumb',
    'Hovedpunkter': 'Main points',
    'Tidslinje': 'Timeline',
    
    # Adjectives
    'viktig': 'important',
    'kritisk': 'critical',
    'vanlig': 'common',
    'enkel': 'simple',
    'kompleks': 'complex',
    'medisinsk': 'medical',
    'klinisk': 'clinical',
    'automatisk': 'automatic',
    'manuell': 'manual',
    
    # Nouns
    'styrke': 'strength',
    'styrker': 'strengths',
    'svakhet': 'weakness',
    'svakheter': 'weaknesses',
    'fordel': 'advantage',
    'fordeler': 'advantages',
    'ulempe': 'disadvantage',
    'ulemper': 'disadvantages',
    'begrensning': 'limitation',
    'begrensninger': 'limitations',
    'verdi': 'value',
    'betydning': 'significance',
    'fremtid': 'future',
    'fremgang': 'progress',
    'forbedring': 'improvement',
    'oppdatering': 'update',
    'tilpasning': 'adaptation',
    'tolkning': 'interpretation',
    'oppførsel': 'behavior',
    'oppgave': 'task',
    'mål': 'goal',
    'resultat': 'result',
    'resultater': 'results',
    'kilde': 'source',
    'kilder': 'sources',
    
    # Medical terms
    'pasient': 'patient',
    'pasienter': 'patients',
    'pasientpopulasjon': 'patient population',
    'sykdom': 'disease',
    'sykdommer': 'diseases',
    'symptom': 'symptom',
    'symptomer': 'symptoms',
    'diagnose': 'diagnosis',
    'diagnoser': 'diagnoses',
    'behandling': 'treatment',
    'behandlinger': 'treatments',
    'prognose': 'prognosis',
    'biomarkør': 'biomarker',
    'biomarkører': 'biomarkers',
    'legemiddel': 'drug',
    'legemidler': 'drugs',
    
    # AI/ML terms (Norwegian to English)
    'Kunstig': 'Artificial',
    'kunstig': 'artificial',
    'Nevral': 'Neural',
    'nevral': 'neural',
    'Konneksjonistisk': 'Connectionist',
    'konneksjonistisk': 'connectionist',
    'Symbolsk': 'Symbolic',
    'symbolsk': 'symbolic',
    'maskinlæring': 'machine learning',
    'dyplæring': 'deep learning',
    'dypt læring': 'deep learning',
    'overfitting': 'overfitting',
    'undertilpasning': 'underfitting',
    'trainingsdata': 'training data',
    'trainingssett': 'training set',
    'testsett': 'test set',
    'trainingseksempler': 'training examples',
    'evaluer': 'evaluate',
    'prediksjon': 'prediction',
    'prediksjoner': 'predictions',
    'klassifisere': 'classify',
    'klassifisering': 'classification',
    
    # Common phrases in slides
    'Key points': 'Key points',
    'Key similarity': 'Key similarity',
    'Key difference': 'Key difference',
    'Important difference': 'Important difference',
    'Important rule': 'Important rule',
    'Medical example': 'Medical example',
    'Medical relevans': 'Medical relevance',
    'Medical kontekst': 'Medical context',
    'Medical betydning': 'Medical significance',
    'Medical application': 'Medical application',
    'Medical risiko': 'Medical risk',
    'Medical praksis': 'Medical practice',
    'Clinical application': 'Clinical application',
    'Clinical relevans': 'Clinical relevance',
    'Clinical tolkning': 'Clinical interpretation',
    'Clinical integrasjon': 'Clinical integration',
    'Clinical nytte': 'Clinical utility',
    'Practical recommendation': 'Practical recommendation',
    'Practical in Lab': 'Practical work in Lab',
    'Useful applications': 'Useful applications',
    
    # Summary sections
    'Summary:': 'Summary:',
    'Oppsummering': 'Summary',
    'Neste steg': 'Next steps',
    
    # Block titles
    'Definition': 'Definition',
    'Definitions': 'Definitions',
    'Example': 'Example',
    'Examples': 'Examples',
    'Warning': 'Warning',
    'Note': 'Note',
    'Tip': 'Tip',
    'Lab': 'Lab',
    
    # More complete phrases
    'og skille fra tradisjonell programmering': 'and distinguish from traditional programming',
    'de fire bioetiske prinsippene': 'the four bioethical principles',
    'typer bias i medisinske AI-systemer': 'types of bias in medical AI systems',
    'privacyhensyn ved bruk av LLM': 'privacy considerations when using LLMs',
    'hovedtrekkene i EU AI Act': 'the main features of the EU AI Act',
    'risikoclassification i EU AI Act': 'risk classification in the EU AI Act',
    'krav til høyrisiko AI': 'requirements for high-risk AI',
    'responsibilitysfordeling': 'responsibility allocation',
    'algoritmisk fairness': 'algorithmic fairness',
    'grunnmodell': 'foundation model',
    
    # Partial word fixes (careful with these)
    'Explainr': 'Explains',
    'explainr': 'explains',
    'describelse': 'description',
    'Describelse': 'Description',
    'modor': 'models',
    'tabor': 'tables',
    'shalla': 'scale',
    'shaller': 'scales',
    'shallering': 'scaling',
    'tor': 'counts',
    'Advantages': 'Advantages',
    'Limitations': 'Limitations',
    
    # Fix mixed language issues
    'responsibility': 'responsibility',
    'Responsibility': 'Responsibility',
    'responsibilitylig': 'responsible',
    'responsibilityet': 'the responsibility',
    
    # Norwegian sentence structures
    'for å ': 'to ',
    'ved å ': 'by ',
    'som er ': 'that is ',
    'som kan ': 'that can ',
    'som skal ': 'that should ',
    'som brukes ': 'that is used ',
    'som gir ': 'that gives ',
    'som har ': 'that has ',
    'uten å ': 'without ',
    'må være ': 'must be ',
    'kan være ': 'can be ',
    'skal være ': 'should be ',
    'bør være ': 'should be ',
}

# Larger block translations (Norwegian text blocks to English)
BLOCK_TRANSLATIONS = {
    # A-Ethics specific
    r'Discuss de fire bioetiske prinsippene i AI-kontekst': 'Discuss the four bioethical principles in an AI context',
    r'Identifisere typer bias i medisinske AI-systemer': 'Identify types of bias in medical AI systems',
    r'Explain privacyhensyn ved bruk av LLM': 'Explain privacy considerations when using LLMs',
    r'Describe hovedtrekkene i EU AI Act': 'Describe the main features of the EU AI Act',
    r'Explain risikoclassification i EU AI Act': 'Explain risk classification in the EU AI Act',
    r'Discuss krav til høyrisiko AI i helsevesenet': 'Discuss requirements for high-risk AI in healthcare',
    r'Reflektere over responsibilitysfordeling når AI feiler': 'Reflect on responsibility allocation when AI fails',
    r'Know about GDPR-relevante aspekter ved AI': 'Know about GDPR-relevant aspects of AI',
    r'Discuss algoritmisk fairness \(fairness\)': 'Discuss algorithmic fairness',
    
    # B-ImageAnalysis specific
    r'Explain fundamental MRI-prinsipper på et overordnet nivå': 'Explain fundamental MRI principles at a high level',
    r'Know about ulike MR-sekvenser': 'Know about different MR sequences',
    r'Describe segmentation i medisinsk image analysis': 'Describe segmentation in medical image analysis',
    r'Know about BraTS-utfordringen for hjernesvulstsegmentation': 'Know about the BraTS challenge for brain tumor segmentation',
    r'Describe radiomic features og kvantitativ avbildning': 'Describe radiomic features and quantitative imaging',
    r'Know about nnU-Net og MONAI som verktøy': 'Know about nnU-Net and MONAI as tools',
    
    # D-DeepLearning specific
    r'Compare biologiske og kunstige nevroner': 'Compare biological and artificial neurons',
    r'Describe oppbygningen av et multilags perseptron \(MLP\)': 'Describe the structure of a multilayer perceptron (MLP)',
    r'Explain hva en aktiveringsfunksjon er': 'Explain what an activation function is',
    r'Understand konseptet forward propagation': 'Understand the concept of forward propagation',
    r'Explain backpropagation på et konseptuelt nivå': 'Explain backpropagation at a conceptual level',
    r'Understand gradient descent og læringsrate': 'Understand gradient descent and learning rate',
    r'Know about loss functions': 'Know about loss functions',
    r'Describe et konvolusjonelt nevralt nettverk \(CNN\)': 'Describe a convolutional neural network (CNN)',
    r'Explain hva et konvolusjonsfilter gjør': 'Explain what a convolution filter does',
    r'Describe pooling-lag og deres funksjon': 'Describe pooling layers and their function',
    r'Know about batch normalization og dropout': 'Know about batch normalization and dropout',
    r'Understand konseptet transfer learning': 'Understand the concept of transfer learning',
    r'Know about advanced arkitekturer': 'Know about advanced architectures',
    
    # E-Evaluation specific
    r'Interpret en Confusion Matrix \(confusion matrix\)': 'Interpret a confusion matrix',
    r'TP, TN, FP, FN i medisinsk kontekst': 'TP, TN, FP, FN in a medical context',
    r'Accuracy \(accuracy\)': 'Accuracy',
    r'Precision \(precision / PPV\)': 'Precision (PPV)',
    r'Recall / Sensitivity \(sensitivity\)': 'Recall / Sensitivity',
    r'Specificity \(specificity\)': 'Specificity',
    r'Når accuracy er utilstrekkelig': 'When accuracy is insufficient',
    
    # G-GenerativeAI specific
    r'Define generative AI og skille fra diskriminativ AI': 'Define generative AI and distinguish from discriminative AI',
    r'Explain self-attention-mekanismen på et konseptuelt nivå': 'Explain the self-attention mechanism at a conceptual level',
    r'Describe transformer-arkitekturen': 'Describe the transformer architecture',
    r'Explain hva tokens er og hvordan tokenisering fungerer': 'Explain what tokens are and how tokenization works',
    r'Understand konseptet kontekstvindu': 'Understand the concept of context window',
    r'Explain hva temperatur betyr i tekstgenerering': 'Explain what temperature means in text generation',
    r'Apply zero-shot prompting': 'Apply zero-shot prompting',
    r'Apply few-shot prompting': 'Apply few-shot prompting',
    r'Apply Chain-of-Thought \(CoT\) prompting': 'Apply Chain-of-Thought (CoT) prompting',
    r'Describe god praksis for systemprompts': 'Describe best practices for system prompts',
    r'Define hallusinering og dens implikasjoner': 'Define hallucination and its implications',
    r'Know about GPT-5, Claude, Gemini og deres applylser': 'Know about GPT-5, Claude, Gemini and their applications',
    r'Explain konseptet grunnmodell': 'Explain the concept of foundation model',
    r'Describe RAG': 'Describe RAG',
    r'Fra Prompt Engineering til Context Engineering': 'From Prompt Engineering to Context Engineering',
    r'Modellspesifikke prompting-teknikker': 'Model-specific prompting techniques',
    r'Håndtere usikkerhet og hallusinasjonsrisiko': 'Handle uncertainty and hallucination risk',
    r'Strukturert ekstraksjon og modellsammenligning': 'Structured extraction and model comparison',
    
    # M-MachineLearning specific
    r'Define machine learning og skille fra tradisjonell programmering': 'Define machine learning and distinguish from traditional programming',
    r'Supervised vs. Unsupervised læring': 'Supervised vs. Unsupervised learning',
    r'Features \(input\) og Labels \(output\)': 'Features (input) and Labels (output)',
    r'Why training set og test set\?': 'Why training set and test set?',
    r'Overfitting \(Overfitting\) og Underfitting \(Underfitting\)': 'Overfitting and Underfitting',
    r'Bias-Variance Trade-off': 'Bias-Variance Trade-off',
    r'K-fold cross-validation': 'K-fold cross-validation',
    r'Baseline model': 'Baseline model',
    r'Classification vs. Regression': 'Classification vs. Regression',
    r'Enkle ML-modor': 'Simple ML models',
    
    # N-GraphTheory specific
    r'What is en graf\? \(Noder og kanter\)': 'What is a graph? (Nodes and edges)',
    r'Rettet vs. ikke-rettet graf': 'Directed vs. undirected graph',
    r'Vektet vs. ikke-vektet graf': 'Weighted vs. unweighted graph',
    r'Nabomatrise \(adjacency matrix\)': 'Adjacency matrix',
    r'Degree Centrality \(grad-sentralitet\)': 'Degree Centrality',
    r'Betweenness Centrality \(mellomliggenhet\)': 'Betweenness Centrality',
    r'Eigenvector Centrality \(egenvektor-sentralitet\)': 'Eigenvector Centrality',
    r'Clustering Coefficient \(klyngekoeffisient\)': 'Clustering Coefficient',
    r'Community Detection og Louvain-algoritmen': 'Community Detection and the Louvain algorithm',
    r'NetworkX-biblioteket for Python': 'The NetworkX library for Python',
    
    # P-PSN specific
    r'Explain konseptet patient similarity networks \(PSN\)': 'Explain the concept of patient similarity networks (PSN)',
    r'Describe hvordan PSN kan støtte precisionsmedisin': 'Describe how PSN can support precision medicine',
    r'Calculate likhet \(similaritet\) mellom pasienter': 'Calculate similarity between patients',
    r'Konstruere et PSN fra en pasient-feature-matrise': 'Construct a PSN from a patient-feature matrix',
    r'Velge terskelverdi for kantoppretting i PSN': 'Choose threshold value for edge creation in PSN',
    r'Identifisere pasientsubgrupper via community detection': 'Identify patient subgroups via community detection',
    r'Advantages og begrensninger ved PSN-tilnærmingen': 'Advantages and limitations of the PSN approach',
    r'Multimodal PSN \(integrering av ulike datatyper\)': 'Multimodal PSN (integration of different data types)',
    
    # S-Neurosymbolic specific
    r'Kontrastere symbolsk og konneksjonistisk AI': 'Contrast symbolic and connectionist AI',
    r'Explain konseptet neurosymbolic integrasjon': 'Explain the concept of neurosymbolic integration',
    r'Describe hva en knowledge graph er': 'Describe what a knowledge graph is',
    r'Know about medisinske ontologier': 'Know about medical ontologies',
    r'Discuss fordeler med neurosymbolic AI i medisin': 'Discuss advantages of neurosymbolic AI in medicine',
    r'Neurosymbolic AI for gliomdiagnostikk': 'Neurosymbolic AI for glioma diagnostics',
    r'Explain hvordan knowledge grapher kan validere prediksjoner': 'Explain how knowledge graphs can validate predictions',
    r'Define agentic AI og dens kjerneegenskaper': 'Define agentic AI and its core characteristics',
    r'Describe hvordan en AI-agent kan orkestrere klinisk arbeidsflyt': 'Describe how an AI agent can orchestrate clinical workflows',
    r'Explain konseptet human-in-the-loop i agentiske systemer': 'Explain the concept of human-in-the-loop in agentic systems',
    r'Discuss etiske utfordringer med autonome AI-agenter i helsevesenet': 'Discuss ethical challenges with autonomous AI agents in healthcare',
    
    # T-Trustworthy specific
    r'Define trustworthy AI iht. EU-retningslinjer': 'Define trustworthy AI according to EU guidelines',
    r'Explain konseptet robustness i ML/AI': 'Explain the concept of robustness in ML/AI',
    r'Describe datadrift og dens konsekvenser': 'Describe data drift and its consequences',
    r'Explain epistemisk vs. aleatorisk usikkerhet': 'Explain epistemic vs. aleatoric uncertainty',
    r'Explain forskjellen mellom epistemisk og aleatorisk usikkerhet': 'Explain the difference between epistemic and aleatoric uncertainty',
    r'Describe human-in-the-loop \(HITL\) systemer': 'Describe human-in-the-loop (HITL) systems',
    r'Discuss viktigheten av kontinuerlig monitorering': 'Discuss the importance of continuous monitoring',
    r'Know about adversarial attacks': 'Know about adversarial attacks',
    
    # X-XAI specific
    r'Explain hvorfor explainability er viktig i medisinsk AI': 'Explain why explainability is important in medical AI',
    r'Skille mellom global og lokal explainability': 'Distinguish between global and local explainability',
    r'Skille mellom ante-hoc og post-hoc explainability': 'Distinguish between ante-hoc and post-hoc explainability',
    r'Describe SHAP': 'Describe SHAP',
    r'Describe LIME': 'Describe LIME',
    r'Explain Grad-CAM for CNN-visualisering': 'Explain Grad-CAM for CNN visualization',
    r'Discuss begrensninger ved XAI-metoder': 'Discuss limitations of XAI methods',
    r'Know about attention-visualisering i LLM': 'Know about attention visualization in LLMs',
    
    # F-Skills specific
    r'Kjøre Jupyter Notebooks i Google Colab': 'Run Jupyter Notebooks in Google Colab',
    r'Bruke Python-variabler, lister og enkle funksjoner': 'Use Python variables, lists, and simple functions',
    r'Importere og bruke biblioteker': 'Import and use libraries',
    r'Lese og inspisere dataset med pandas': 'Read and inspect datasets with pandas',
    r'Trene en enkel modell med scikit-learn': 'Train a simple model with scikit-learn',
    r'Visualisere resultater med matplotlib': 'Visualize results with matplotlib',
    r'Bruke NetworkX for enkel nettverksanalyse': 'Use NetworkX for simple network analysis',
    r'Bygge og trene en modell med PyTorch': 'Build and train a model with PyTorch',
    r'Bruke AI-verktøy .* som kodehjelp': 'Use AI tools as coding assistants',
    r'Skrive dokumenter med LaTeX/Overleaf': 'Write documents with LaTeX/Overleaf',
    r'Komponere effektive prompts for medisinske oppgaver': 'Compose effective prompts for medical tasks',
    r'Apply context engineering i praksis': 'Apply context engineering in practice',
    r'Velge riktig LLM-modell for oppgaven': 'Choose the right LLM model for the task',
    r'Compare output fra ulike LLM-er': 'Compare output from different LLMs',
}

# Content translations (Norwegian text blocks to English)
CONTENT_TRANSLATIONS = {
    # Block content translations
    'Biologisk nevron': 'Biological neuron',
    'Kunstig nevron (perseptron)': 'Artificial neuron (perceptron)',
    'Dendritter': 'Dendrites',
    'Cellekropp': 'Cell body',
    'Akson': 'Axon',
    'Synapse': 'Synapse',
    'Mottar signaler': 'Receives signals',
    'Prosesserer': 'Processes',
    'Sender videre': 'Transmits',
    'Kobling til neste nevron': 'Connection to next neuron',
    'Kompleks elektrokjemisk aktivitet': 'Complex electrochemical activity',
    'Mottar data': 'Receives data',
    'Synapsestyrke': 'Synaptic strength',
    'Matematisk forenkling': 'Mathematical simplification',
    'aktiveringsfunksjon': 'activation function',
    'Begge summerer inngående signaler': 'Both sum incoming signals',
    'fyrer': 'fires',
    'aktiverer': 'activates',
    'overstiger en terskel': 'exceeds a threshold',
    'kraftig forenklede': 'greatly simplified',
    
    # Deep learning content
    'MLP-arkitektur': 'MLP architecture',
    'Inputlag': 'Input layer',
    'Mottar features': 'Receives features',
    'ikke prosessering': 'no processing',
    'Skjulte lag': 'Hidden layers',
    'lag med nevroner': 'layers of neurons',
    'Outputlag': 'Output layer',
    'Produserer prediksjon': 'Produces prediction',
    'Fully connected (dense)': 'Fully connected (dense)',
    'Hvert nevron i ett lag er koblet til': 'Each neuron in one layer is connected to',
    'alle nevroner i neste lag': 'all neurons in the next layer',
    'Mange parametre (vekter og bias)': 'Many parameters (weights and biases)',
    'Dyp læring': 'Deep learning',
    'skjulte lag = dyp modell': 'hidden layers = deep model',
    'Flere lag': 'More layers',
    'mer abstrakte representasjoner': 'more abstract representations',
    'Skjult': 'Hidden',
    
    # Activation functions
    'Why aktiveringsfunksjoner': 'Why activation functions',
    'Uten dem': 'Without them',
    'Hele nettverket = lineær transformasjon': 'The entire network = linear transformation',
    'Introduserer ikke-linearitet': 'Introduces non-linearity',
    'Problem': 'Problem',
    'vanishing gradients': 'vanishing gradients',
    'Brukes i output for binær classification': 'Used in output for binary classification',
    'Moderne standard for skjulte lag': 'Modern standard for hidden layers',
    'Rask, unngår vanishing gradients': 'Fast, avoids vanishing gradients',
    'gir sannsynlighetsfordeling over klasser': 'gives probability distribution over classes',
    'summerer til 1': 'sums to 1',
    
    # Forward/backpropagation
    'fremoverberegning': 'forward computation',
    'Data legges inn i inputlaget': 'Data is fed into the input layer',
    'For hvert lag': 'For each layer',
    'Beregn vektet sum': 'Compute weighted sum',
    'Appliser aktivering': 'Apply activation',
    'Prediksjon fra siste lag': 'Prediction from last layer',
    'calculater prediksjon': 'calculates prediction',
    'ingen læring skjer her': 'no learning happens here',
    'Læring skjer ved': 'Learning happens through',
    'bakoverberegning av feil': 'backward computation of error',
    'Sammenlign prediksjon med fasit': 'Compare prediction with ground truth',
    'Propager bakover': 'Propagate backward',
    'Hvor mye bidro hver vekt til feilen': 'How much did each weight contribute to the error',
    'Kjerneregelen': 'Chain rule',
    'Deriver feil': 'Differentiate error',
    'Juster for å redusere feil': 'Adjust to reduce error',
    'Tenk deg at du justerer en kompleks maskin': 'Imagine adjusting a complex machine',
    'fortor deg': 'tells you',
    'skruer (vekter)': 'screws (weights)',
    'skru på': 'turn',
    'i hvilken retning': 'in which direction',
    'forbedre resultatet': 'improve the result',
    'Kjerneregelen for derivasjon propagerer gradienter bakover gjennom nettverket': 'The chain rule for differentiation propagates gradients backward through the network',
    
    # Gradient descent
    'Optimiseringsalgoritme': 'Optimization algorithm',
    'minimere loss-funksjonen': 'minimize the loss function',
    'Følger den negative gradienten': 'Follows the negative gradient',
    'bratteste nedoverbakke': 'steepest descent',
    'Oppdateringsregel': 'Update rule',
    'Læringsrate': 'Learning rate',
    'Bestemmer steglengde': 'Determines step size',
    'For stor': 'Too large',
    'Hopper over minimum': 'Jumps over minimum',
    'For liten': 'Too small',
    'Treg konvergens': 'Slow convergence',
    'Varianter': 'Variants',
    'Alle data per oppdatering': 'All data per update',
    'Ett eksempel om gangen': 'One example at a time',
    'Små grupper': 'Small batches',
    'Adaptiv læringsrate': 'Adaptive learning rate',
    'populær': 'popular',
    'En epoch = én gjennomgang av hele trainingsdatasetet': 'One epoch = one pass through the entire training dataset',
    
    # Loss functions
    'tapsfunksjon': 'loss function',
    'Måler hvor feil': 'Measures how wrong',
    'modellens prediksjoner er': "the model's predictions are",
    'Målet': 'The goal',
    'Minimere loss under training': 'Minimize loss during training',
    'Brukes for regression': 'Used for regression',
    'Straffes hardt for store feil': 'Penalizes large errors heavily',
    'Kontinuerlig output': 'Continuous output',
    'Brukes for classification': 'Used for classification',
    'Måler avvik mellom sannsynlighetsfordelinger': 'Measures divergence between probability distributions',
    'Velge riktig loss': 'Choosing the right loss',
    
    # CNN
    'spesialisert for bildedata': 'specialized for image data',
    'Utnytter romlig struktur': 'Exploits spatial structure',
    'Langt færre parametre enn fullt koblet nettverk': 'Far fewer parameters than fully connected network',
    'Translasjonsinvariant': 'Translation invariant',
    'gjenkjenner mønstre uansett posisjon': 'recognizes patterns regardless of position',
    'Typisk CNN-arkitektur': 'Typical CNN architecture',
    'Bilde': 'Image',
    'Klasse': 'Class',
    'Hierarkisk læring': 'Hierarchical learning',
    'Tidlige lag': 'Early layers',
    'Enkle features': 'Simple features',
    'kanter, teksturer': 'edges, textures',
    'Senere lag': 'Later layers',
    'Komplekse features': 'Complex features',
    'former, objektdeler': 'shapes, object parts',
    'Siste lag': 'Final layer',
    'Høynivå konsepter': 'High-level concepts',
    'objekter, kategorier': 'objects, categories',
    
    # Convolution filters
    'Konvolusjonsfilter (kernel)': 'Convolution filter (kernel)',
    'Liten matrise': 'Small matrix',
    'glir over bildet': 'slides over the image',
    'Calculater punktprodukt': 'Calculates dot product',
    'mellom filter og bildepatch': 'between filter and image patch',
    'Produserer et feature map': 'Produces a feature map',
    'Kantdeteksjon': 'Edge detection',
    'Detekterer horisontale kanter': 'Detects horizontal edges',
    'Ulike filtre': 'Different filters',
    'ulike features': 'different features',
    'CNN lærer optimale filtre': 'CNN learns optimal filters',
    'Stride': 'Stride',
    'Hvor langt filteret flyttes': 'How far the filter moves',
    'Padding': 'Padding',
    'Legge til piksler i kanten': 'Adding pixels at the border',
    'Kanal': 'Channel',
    'Feature map': 'Feature map',
    'Output fra konvolusjon': 'Output from convolution',
    'Vektdeling': 'Weight sharing',
    'Samme filter brukes over hele bildet': 'Same filter used across entire image',
    'dramatisk færre parametre': 'dramatically fewer parameters',
    
    # Pooling
    'nedshallering av feature maps': 'downsampling of feature maps',
    'Vanligste type': 'Most common type',
    'Max pooling': 'Max pooling',
    'Velger maksverdi': 'Selects maximum value',
    'i hvert område': 'in each region',
    'Reduserer romlig størrelse': 'Reduces spatial size',
    'med faktor': 'by factor',
    'Advantages med pooling': 'Advantages of pooling',
    'Reduserer beregning': 'Reduces computation',
    'færre parametre': 'fewer parameters',
    'Translasjonsinvarians': 'Translation invariance',
    'litt skift påvirker ikke output': 'slight shift does not affect output',
    'Unngår overfitting': 'Prevents overfitting',
    'Andre pooling-typer': 'Other pooling types',
    'Gjennomsnitt': 'Average',
    'Global avg': 'Global avg',
    'Feature map til én verdi': 'Feature map to one value',
    
    # Regularization
    'Normaliserer aktiveringer i hvert mini-batch': 'Normalizes activations in each mini-batch',
    'deretter shaller/skift': 'then scale/shift',
    'Raskere training': 'Faster training',
    'Stabiliserer læring': 'Stabilizes learning',
    'Tillater høyere læringsrate': 'Allows higher learning rate',
    'Plasseres typisk etter konvolusjon, før aktivering': 'Typically placed after convolution, before activation',
    'Slår av tilfeldige nevroner under training': 'Turns off random neurons during training',
    'dropout rate': 'dropout rate',
    'Reduserer overfitting': 'Reduces overfitting',
    'Tvinger nettverk til å være robust': 'Forces network to be robust',
    'Fungerer som ensemble': 'Acts as ensemble',
    'Brukes kun under training': 'Used only during training',
    'Regulariseringsteknikker': 'Regularization techniques',
    'hjelper med å unngå overfitting og forbedre generaliseringsevne': 'help prevent overfitting and improve generalization',
    
    # Transfer learning
    'Gjenbruk en modell trent på ett problem til et nytt problem': 'Reuse a model trained on one problem for a new problem',
    'Spesielt nyttig når du har lite data': 'Especially useful when you have little data',
    'Typisk fremgangsmåte': 'Typical approach',
    'Ta en pretrent modell': 'Take a pretrained model',
    'trent på ImageNet': 'trained on ImageNet',
    'millioner av bilder': 'millions of images',
    'Frys tidlige lag': 'Freeze early layers',
    'generelle features': 'general features',
    'Erstatt/tren siste lag for din spesifikke oppgave': 'Replace/train final layer for your specific task',
    'Fintun hele modellen med lav læringsrate': 'Fine-tune entire model with low learning rate',
    'Why fungerer det': 'Why does it work',
    'Tidlige lag lærer generelle features': 'Early layers learn general features',
    'som er nyttige for mange oppgaver': 'that are useful for many tasks',
    'Kun de siste lagene er oppgavespesifikke': 'Only the final layers are task-specific',
    'Example i medisin': 'Example in medicine',
    'Tren på millioner av naturlige bilder': 'Train on millions of natural images',
    'Fintun på tusenvis av røntgenbilder': 'Fine-tune on thousands of X-ray images',
    'Bedre resultat enn å trene fra scratch': 'Better results than training from scratch',
    
    # ResNet and ViT
    'Introduserte skip connections': 'Introduced skip connections',
    'Lar gradienter flyte direkte': 'Allows gradients to flow directly',
    'Muliggjør svært dype nettverk': 'Enables very deep networks',
    'lag': 'layers',
    'residual block': 'residual block',
    'Important bidrag': 'Important contribution',
    'Løste problemet med degradering i dype nettverk': 'Solved the problem of degradation in deep networks',
    'Standard for medisinsk image analysis': 'Standard for medical image analysis',
    'Applyr transformer-arkitektur på bilder': 'Applies transformer architecture to images',
    'Deler bilde i patches': 'Divides image into patches',
    'Bruker self-attention': 'Uses self-attention',
    'Skalerer godt med data og compute': 'Scales well with data and compute',
    'Moderne trend': 'Modern trend',
    'Overgår CNN på store dataset': 'Outperforms CNN on large datasets',
    'Brukes i state-of-the-art modor': 'Used in state-of-the-art models',
    'Andre viktige arkitekturer': 'Other important architectures',
    'Segmentation (medisinsk klassiker)': 'Segmentation (medical classic)',
    'Balansert shallering': 'Balanced scaling',
    'Tette koblinger': 'Dense connections',
}


def translate_file(filepath: Path) -> bool:
    """Translate a single LaTeX file from Norwegian to English."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply block translations first (more specific patterns)
        for pattern, replacement in BLOCK_TRANSLATIONS.items():
            content = re.sub(pattern, replacement, content)
        
        # Apply content translations
        for norwegian, english in CONTENT_TRANSLATIONS.items():
            content = content.replace(norwegian, english)
        
        # Apply general translations
        for norwegian, english in TRANSLATIONS.items():
            content = content.replace(norwegian, english)
        
        # Additional cleanup patterns
        # Fix any remaining Norwegian patterns
        cleanup_patterns = [
            (r'\\section\{([^}]*) og ([^}]*)\}', r'\\section{\1 and \2}'),
            (r'\\subsection\{([^}]*) og ([^}]*)\}', r'\\subsection{\1 and \2}'),
            (r'\\textbf\{([^}]*) og ([^}]*)\}', r'\\textbf{\1 and \2}'),
            (r'\beller\b', 'or'),
            (r'\bMen\b', 'But'),
            (r'\bmen\b', 'but'),
            (r'\bkan\b', 'can'),
            (r'\bvil\b', 'will'),
            (r'\bhar\b', 'has'),
            (r'\ber\b', 'is'),
            (r'\bmed\b', 'with'),
            (r'\bfor\b', 'for'),
            (r'\btil\b', 'to'),
            (r'\bav\b', 'of'),
            (r'\bved\b', 'at'),
            (r'\bfra\b', 'from'),
            (r'\bi\b', 'in'),
            (r'\bpå\b', 'on'),
            (r'\ben\b', 'a'),
            (r'\bet\b', 'a'),
            (r'\bden\b', 'it'),
            (r'\bdet\b', 'it'),
            (r'\bde\b', 'they'),
            (r'\bsom\b', 'that'),
            (r'\bnår\b', 'when'),
            (r'\bhvis\b', 'if'),
            (r'\bhvor\b', 'where'),
            (r'\bhvordan\b', 'how'),
            (r'\bhvorfor\b', 'why'),
            (r'\bhva\b', 'what'),
            (r'\bhvem\b', 'who'),
            (r'\bhvilken\b', 'which'),
            (r'\bhvilke\b', 'which'),
        ]
        
        # Only apply word-boundary replacements carefully to avoid breaking LaTeX
        # These are commented out as they might cause issues
        # for pattern, replacement in cleanup_patterns:
        #     content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Main function to translate all Beamer presentations."""
    beamer_dir = Path(__file__).parent
    
    # List of folders to process (excluding Y and Z which are already in English)
    folders = [
        'A-Ethics', 'B-ImageAnalysis', 'D-DeepLearning', 'E-Evaluation',
        'F-Skills', 'G-GenerativeAI', 'M-MachineLearning', 'N-GraphTheory',
        'P-PSN', 'S-Neurosymbolic', 'T-Trustworthy', 'X-XAI'
    ]
    
    translated = []
    failed = []
    
    for folder in folders:
        folder_path = beamer_dir / folder
        main_tex = folder_path / 'main.tex'
        
        if main_tex.exists():
            print(f"Translating {folder}/main.tex...")
            if translate_file(main_tex):
                translated.append(folder)
                print(f"  ✓ Translated")
            else:
                print(f"  - No changes needed or error")
        else:
            print(f"  ✗ Not found: {main_tex}")
            failed.append(folder)
    
    print(f"\n=== Summary ===")
    print(f"Translated: {len(translated)} files")
    print(f"Failed/Not found: {len(failed)} files")
    
    if translated:
        print(f"\nTranslated folders: {', '.join(translated)}")
    if failed:
        print(f"Failed folders: {', '.join(failed)}")


if __name__ == '__main__':
    main()

