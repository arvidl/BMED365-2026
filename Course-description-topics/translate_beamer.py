#!/usr/bin/env python3
"""
Translate Norwegian Beamer presentations to English.
This script performs common translations for LaTeX Beamer files.
"""
import os
import re
import sys

# Translation mappings for common Norwegian LaTeX patterns
TRANSLATIONS = {
    # Language settings
    r'\[norsk\]': '[english]',
    
    # Course info
    'ELMED219': 'BMED365',
    'Vår 2026': 'Spring 2026',
    
    # Section headers
    'Oversikt': 'Overview',
    'Oppsummering': 'Summary',
    'Innholdsfortegnelse': 'Table of Contents',
    'Tittelside': 'Title page',
    
    # Common words/phrases
    'Hva er': 'What is',
    'Hvorfor': 'Why',
    'Hvordan': 'How',
    'Eksempel': 'Example',
    'Eksempler': 'Examples',
    'Definisjon': 'Definition',
    'Definisjoner': 'Definitions',
    'Nøkkelkonsepter': 'Key concepts',
    'Nøkkelpunkt': 'Key point',
    'Nøkkelpunkter': 'Key points',
    'Viktig': 'Important',
    'Tips': 'Tip',
    'Merk': 'Note',
    'Advarsel': 'Warning',
    'Fordeler': 'Advantages',
    'Ulemper': 'Disadvantages',
    'Begrensninger': 'Limitations',
    'Anvendelse': 'Application',
    'Anvendelser': 'Applications',
    'Medisinsk': 'Medical',
    'Klinisk': 'Clinical',
    
    # Technical terms
    'maskinlæring': 'machine learning',
    'Maskinlæring': 'Machine Learning',
    'dyplæring': 'deep learning',
    'Dyplæring': 'Deep Learning',
    'nevrale nettverk': 'neural networks',
    'Nevrale nettverk': 'Neural Networks',
    'kunstig intelligens': 'artificial intelligence',
    'Kunstig intelligens': 'Artificial Intelligence',
    'språkmodell': 'language model',
    'Språkmodell': 'Language Model',
    'språkmodeller': 'language models',
    'Språkmodeller': 'Language Models',
    'nettverksvitenskap': 'network science',
    'Nettverksvitenskap': 'Network Science',
    'grafteori': 'graph theory',
    'Grafteori': 'Graph Theory',
    'bildeanalyse': 'image analysis',
    'Bildeanalyse': 'Image Analysis',
    'segmentering': 'segmentation',
    'Segmentering': 'Segmentation',
    'klassifisering': 'classification',
    'Klassifisering': 'Classification',
    'regresjon': 'regression',
    'Regresjon': 'Regression',
    'evaluering': 'evaluation',
    'Evaluering': 'Evaluation',
    'validering': 'validation',
    'Validering': 'Validation',
    'trening': 'training',
    'Trening': 'Training',
    'testing': 'testing',
    'Testing': 'Testing',
    
    # Presentation-specific
    'Praktiske ferdigheter': 'Practical Skills',
    'Praktiske Ferdigheter': 'Practical Skills',
    'Grunnleggende konsepter': 'Fundamental Concepts',
    'Grunnleggende': 'Fundamental',
    'grunnleggende': 'fundamental',
    'Avanserte': 'Advanced',
    'avanserte': 'advanced',
    'Introduksjon': 'Introduction',
    'introduksjon': 'introduction',
    
    # Ethics and regulation
    'AI-etikk': 'AI Ethics',
    'Etikk': 'Ethics',
    'etikk': 'ethics',
    'Regulering': 'Regulation',
    'regulering': 'regulation',
    'Ansvar': 'Responsibility',
    'ansvar': 'responsibility',
    'Rettferdighet': 'Fairness',
    'rettferdighet': 'fairness',
    'Personvern': 'Privacy',
    'personvern': 'privacy',
    'Bioetikk': 'Bioethics',
    'bioetikk': 'bioethics',
    
    # XAI and trustworthy
    'Forklarbar AI': 'Explainable AI',
    'forklarbar AI': 'explainable AI',
    'Forklarbarhet': 'Explainability',
    'forklarbarhet': 'explainability',
    'Pålitelig AI': 'Trustworthy AI',
    'pålitelig AI': 'trustworthy AI',
    'Robusthet': 'Robustness',
    'robusthet': 'robustness',
    
    # Generative AI
    'Generativ AI': 'Generative AI',
    'generativ AI': 'generative AI',
    'Store Språkmodeller': 'Large Language Models',
    'store språkmodeller': 'large language models',
    
    # Neurosymbolic
    'Nevrosymbolsk': 'Neurosymbolic',
    'nevrosymbolsk': 'neurosymbolic',
    'Agentisk AI': 'Agentic AI',
    'agentisk AI': 'agentic AI',
    'Kunnskapsgraf': 'Knowledge Graph',
    'kunnskapsgraf': 'knowledge graph',
    
    # PSN
    'Pasient-likhetsnettverk': 'Patient Similarity Networks',
    'pasient-likhetsnettverk': 'patient similarity networks',
    
    # Common verbs/phrases in descriptions
    'Forklare': 'Explain',
    'forklare': 'explain',
    'Beskrive': 'Describe',
    'beskrive': 'describe',
    'Definere': 'Define',
    'definere': 'define',
    'Forstå': 'Understand',
    'forstå': 'understand',
    'Kjenne til': 'Know about',
    'kjenne til': 'know about',
    'Anvende': 'Apply',
    'anvende': 'apply',
    'Diskutere': 'Discuss',
    'diskutere': 'discuss',
    'Vurdere': 'Evaluate',
    'vurdere': 'evaluate',
    'Sammenligne': 'Compare',
    'sammenligne': 'compare',
    'Tolke': 'Interpret',
    'tolke': 'interpret',
    'Beregne': 'Calculate',
    'beregne': 'calculate',
    
    # Data terms
    'treningssett': 'training set',
    'Treningssett': 'Training set',
    'testsett': 'test set',
    'Testsett': 'Test set',
    'valideringssett': 'validation set',
    'Valideringssett': 'Validation set',
    'datasett': 'dataset',
    'Datasett': 'Dataset',
    'kryssvalidering': 'cross-validation',
    'Kryssvalidering': 'Cross-validation',
    
    # Model terms
    'overtilpasning': 'overfitting',
    'Overtilpasning': 'Overfitting',
    'undertilpasning': 'underfitting',
    'Undertilpasning': 'Underfitting',
    'baseline-modell': 'baseline model',
    'Baseline-modell': 'Baseline model',
    
    # Evaluation metrics
    'forvirringsmatrise': 'confusion matrix',
    'Forvirringsmatrise': 'Confusion Matrix',
    'nøyaktighet': 'accuracy',
    'Nøyaktighet': 'Accuracy',
    'presisjon': 'precision',
    'Presisjon': 'Precision',
    'sensitivitet': 'sensitivity',
    'Sensitivitet': 'Sensitivity',
    'spesifisitet': 'specificity',
    'Spesifisitet': 'Specificity',
    
    # Common words
    'og': 'and',  # Be careful with this one
    'eller': 'or',
    'med': 'with',
    'for': 'for',
    'av': 'of',
    'til': 'to',
    'i': 'in',
    'på': 'on',
    'som': 'that',
    'kan': 'can',
    'må': 'must',
    'skal': 'shall',
    'vil': 'will',
    'har': 'has',
    'er': 'is',
    
    # Titles
    'Momentliste': 'Topic List',
    
    # Specific slide titles - will translate these as whole strings
}

# Longer phrase translations (applied first)
PHRASE_TRANSLATIONS = {
    # Title translations
    'AI-etikk og Regulering': 'AI Ethics and Regulation',
    'Medisinsk Bildeanalyse': 'Medical Image Analysis',
    'Nevrale nettverk og Dyplæring': 'Neural Networks and Deep Learning',
    'Evaluering av ML-modeller': 'Evaluation of ML Models',
    'Praktiske Ferdigheter': 'Practical Skills',
    'Generativ AI og Store Språkmodeller': 'Generative AI and Large Language Models',
    'Maskinlæring -- Grunnleggende konsepter': 'Machine Learning -- Fundamental Concepts',
    'Grafteori og Nettverksanalyse': 'Graph Theory and Network Analysis',
    'Pasient-likhetsnettverk (PSN)': 'Patient Similarity Networks (PSN)',
    'Nevrosymbolsk AI og Agentisk AI': 'Neurosymbolic AI and Agentic AI',
    'Pålitelig AI og Robusthet': 'Trustworthy AI and Robustness',
    'Forklarbar AI (XAI)': 'Explainable AI (XAI)',
    
    # Section headers
    'Biologiske vs. kunstige nevroner': 'Biological vs. Artificial Neurons',
    'Trening av nevrale nettverk': 'Training Neural Networks',
    'Konvolusjonelle nevrale nettverk': 'Convolutional Neural Networks',
    'Regularisering og avanserte teknikker': 'Regularization and Advanced Techniques',
    'Grunnleggende nevrale nettverk': 'Basic Neural Networks',
    'Introduksjon til Generativ AI': 'Introduction to Generative AI',
    'Transformer-arkitekturen': 'Transformer Architecture',
    'LLM-grunnleggende': 'LLM Fundamentals',
    'Prompt Engineering': 'Prompt Engineering',
    'Context Engineering': 'Context Engineering',
    'Utfordringer med LLM': 'Challenges with LLM',
    'Modeller og avanserte konsepter': 'Models and Advanced Concepts',
    'Jupyter Notebooks og Google Colab': 'Jupyter Notebooks and Google Colab',
    'Python-grunnleggende': 'Python Fundamentals',
    'Maskinlæring med scikit-learn': 'Machine Learning with scikit-learn',
    'Nettverksanalyse med NetworkX': 'Network Analysis with NetworkX',
    'Dyplæring med PyTorch': 'Deep Learning with PyTorch',
    'AI-verktøy og LaTeX': 'AI Tools and LaTeX',
    'Context Engineering for LLM': 'Context Engineering for LLM',
    'MRI-grunnleggende': 'MRI Fundamentals',
    'Kvantitativ avbildning': 'Quantitative Imaging',
    'Verktøy for medisinsk bildeanalyse': 'Tools for Medical Image Analysis',
    'Ansvar og rettferdighet': 'Responsibility and Fairness',
    
    # Common explanatory phrases
    'Hva er det?': 'What is it?',
    'Hvordan fungerer det?': 'How does it work?',
    'Hvorfor er det viktig?': 'Why is it important?',
    'Nyttige bruksområder': 'Useful applications',
    'Tips for effektiv bruk': 'Tips for effective use',
    'I medisin': 'In medicine',
    'Medisinsk anvendelse': 'Medical application',
    'Medisinsk eksempel': 'Medical example',
    'Klinisk anvendelse': 'Clinical application',
    'Relevans for AI': 'Relevance for AI',
    'For AI-analyse': 'For AI analysis',
    'Teamprosjekt-relevans': 'Team project relevance',
    'Praktisk i Lab': 'Practical in Lab',
    
    # Block titles
    'Viktig regel': 'Important rule',
    'Hovedprinsipp': 'Main principle',
    'Viktig om': 'Important about',
    'Kritisk spørsmål': 'Critical question',
    'Andre verktøy': 'Other tools',
    'Huskeregel': 'Rule of thumb',
    'Praktisk anbefaling': 'Practical recommendation',
    'Anbefaling for medisin': 'Recommendation for medicine',
    'Innebygd CoT': 'Built-in CoT',
    'Anti-hallusinasjons': 'Anti-hallucination',
    
    # Slide-specific phrases that should be translated as units
    'ELMED219: Momentliste': 'BMED365: Topic List',
    
    # Common frame/block titles
    'Beauchamp \\& Childress\' fire prinsipper': 'Beauchamp \\& Childress\' Four Principles',
    'Typer hallusinasjoner': 'Types of Hallucinations',
    'Hvorfor tokens?': 'Why tokens?',
    'Nøkkelforskjell': 'Key difference',
    'Nøkkellikhet': 'Key similarity',
    'Viktig forskjell': 'Important difference',
    
    # Medical/Clinical phrases
    'Syk/Frisk': 'Sick/Healthy',
    'Positiv/Negativ': 'Positive/Negative',
    'Sant Positiv': 'True Positive',
    'Sant Negativ': 'True Negative',
    'Falskt Positiv': 'False Positive',
    'Falskt Negativ': 'False Negative',
}


def translate_latex_file(input_path, output_path=None):
    """Translate a LaTeX file from Norwegian to English."""
    if output_path is None:
        output_path = input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # First apply phrase translations (longer phrases first)
    sorted_phrases = sorted(PHRASE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    for nor, eng in sorted_phrases:
        content = content.replace(nor, eng)
    
    # Then apply word translations (longer first to avoid partial matches)
    sorted_words = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    for nor, eng in sorted_words:
        # For very short words, only replace if they're surrounded by word boundaries
        if len(nor) <= 3:
            # Skip these very short words as they cause too many issues
            continue
        content = content.replace(nor, eng)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated: {input_path}")


def main():
    """Process all Beamer files in the directory."""
    beamer_dir = "/Users/arvid/GitHub/BMED365-2026/Course-description-topics/Beamer"
    
    # Find all main.tex files in immediate subdirectories (English-named folders)
    for folder in os.listdir(beamer_dir):
        folder_path = os.path.join(beamer_dir, folder)
        if os.path.isdir(folder_path) and not folder.endswith('-old'):
            main_tex = os.path.join(folder_path, 'main.tex')
            if os.path.exists(main_tex):
                translate_latex_file(main_tex)


if __name__ == '__main__':
    main()

