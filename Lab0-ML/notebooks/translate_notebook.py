#!/usr/bin/env python3
"""
Translate Norwegian text in Jupyter notebooks to English.
Handles only full phrases to avoid corrupting code and URLs.
"""
import json
import sys
import re

# Translation dictionary - full phrases only
TRANSLATIONS = {
    # Headers and titles
    "Et første eksempel på maskinlæring": "A First Example of Machine Learning",
    "Velkommen til ditt første praktiske møte med maskinlæring!": "Welcome to your first practical encounter with machine learning!",
    "Hva er maskinlæring?": "What is Machine Learning?",
    "Hvorfor er dette viktig i medisin?": "Why is This Important in Medicine?",
    "Vårt første datasett: Iris-blomster": "Our First Dataset: Iris Flowers",
    "Hvorfor akkurat Iris-datasettet?": "Why the Iris Dataset?",
    "Enkelt og oversiktlig": "Simple and clear",
    "Godt forstått": "Well understood",
    "Tydelig demonstrasjon": "Clear demonstration",
    "Visuelt intuitivt": "Visually intuitive",
    
    # Environment check
    "MILJØSJEKK": "ENVIRONMENT CHECK",
    "Denne cellen sjekker om vi kjører i Google Colab eller Kaggle.": "This cell checks if we are running in Google Colab or Kaggle.",
    "Dette er viktig fordi noen deler av koden må tilpasses ulike miljøer.": "This is important because some parts of the code need to be adapted for different environments.",
    "Vi gjør denne sjekken i starten av alle notebooks i kurset.": "We do this check at the beginning of all notebooks in the course.",
    "Kjører i Google Colab": "Running in Google Colab",
    "Kjører IKKE i Google Colab": "NOT running in Google Colab",
    "Kjører i Kaggle": "Running in Kaggle",
    "Kjører IKKE i Kaggle": "NOT running in Kaggle",
    
    # Tips and hints
    "Tips:": "Tip:",
    "Din tur!": "Your Turn!",
    "Råd:": "Advice:",
    "Merk:": "Note:",
    "Viktig:": "Important:",
    
    # Common phrases in explanations
    "Tradisjonelt programmerer vi datamaskiner ved å gi dem eksplisitte instruksjoner": "Traditionally we program computers by giving them explicit instructions",
    "I maskinlæring gjør vi noe fundamentalt annerledes": "In machine learning we do something fundamentally different",
    "vi gir datamaskinen data og lar den lære mønstre fra disse dataene": "we give the computer data and let it learn patterns from this data",
    "Algoritmen finner selv ut hvordan den skal løse oppgaven basert på eksemplene vi gir den": "The algorithm figures out how to solve the task based on the examples we give it",
    "Tenk deg at du skal lage et program som kan gjenkjenne kreftceller i mikroskopbilder": "Imagine you want to create a program that can recognize cancer cells in microscope images",
    "Det ville være ekstremt vanskelig å skrive eksplisitte regler": "It would be extremely difficult to write explicit rules",
    "Med maskinlæring kan vi vise algoritmen tusenvis av eksempler": "With machine learning we can show the algorithm thousands of examples",
    "og la den lære å skille mellom dem selv": "and let it learn to distinguish between them",
    
    # Data exploration
    "La oss laste inn datasettet": "Let's load the dataset",
    "La oss utforske datasettet": "Let's explore the dataset",
    "Utforsk datasettet": "Explore the dataset",
    "Visualiser dataene": "Visualize the data",
    "Tren en modell": "Train a model",
    "Evaluer modellen": "Evaluate the model",
    "Sammenlign modeller": "Compare models",
    
    # Section headers
    "Oppsummering": "Summary",
    "Konklusjon": "Conclusion",
    "Neste steg": "Next Steps",
    "Ekstra oppgaver": "Extra Exercises",
    "Løsningsforslag": "Suggested Solution",
    "Forklaring": "Explanation",
    
    # Exercise instructions
    "Kjør denne cellen": "Run this cell",
    "Prøv selv": "Try it yourself",
    "Eksperimenter": "Experiment",
    "Endre verdiene": "Change the values",
    "Se hva som skjer": "See what happens",
    "Sammenlign resultatene": "Compare the results",
    
    # Data terms (full phrases)
    "rader og": "rows and",
    "kolonner": "columns",
    "Egenskaper:": "Features:",
    "Målvariabel:": "Target variable:",
    
    # Import and setup sections
    "Importer biblioteker": "Import libraries",
    "Numeriske beregninger": "Numerical calculations",
    "Datahåndtering": "Data handling",
    "Visualisering": "Visualization",
    "Maskinlæringsmodeller": "Machine learning models",
    
    # PyCaret specific
    "Hurtigguide": "Quick Guide",
    "Automatisert maskinlæring": "Automated Machine Learning",
    "Sammenlign mange modeller samtidig": "Compare many models at once",
    
    # Binary classification
    "Binær klassifikasjon": "Binary Classification",
    "Syk/Frisk": "Sick/Healthy",
    "Positiv/Negativ": "Positive/Negative",
    "Sant Positiv": "True Positive",
    "Sant Negativ": "True Negative",
    "Falskt Positiv": "False Positive",
    "Falskt Negativ": "False Negative",
    
    # Model evaluation
    "Forvirringsmatrise": "Confusion Matrix",
    "Klassifiseringsrapport": "Classification Report",
    "Treningssett": "Training set",
    "Testsett": "Test set",
    "Kryssvalidering": "Cross-validation",
    
    # General Norwegian words that appear in complete contexts
    "Versjon ": "Version ",
    "observasjoner": "observations",
    "observasjoner med": "observations with",
    "egenskaper hver": "features each",
    "Brukt i maskinlæring siden": "Used in machine learning since",
    "Viser klassifiseringsteknikker på en forståelig måte": "Shows classification techniques in an understandable way",
    "Vi kan faktisk se forskjellene mellom klassene": "We can actually see the differences between the classes",
    "Senere i kurset skal vi se på mer kompliserte": "Later in the course we will look at more complex",
    "og interessante datasett": "and interesting datasets",
    "inkludert medisinske data": "including medical data",
    
    # Course references
    "ELMED219-2026": "BMED365-2026",
    "ELMED219": "BMED365",
    
    # Code comments - these should be translated carefully
    "# Importer nødvendige biblioteker": "# Import necessary libraries",
    "# Last inn data": "# Load data",
    "# Utforsk data": "# Explore data",
    "# Tren modellen": "# Train the model",
    "# Evaluer modellen": "# Evaluate the model",
    "# Visualiser resultater": "# Visualize results",
}

# URL path translations (notebook names)
URL_TRANSLATIONS = {
    "01-Enkle_eksempler.ipynb": "01-Simple_examples.ipynb",
    "01a-Enkle_eksempler_losninger.ipynb": "01a-Simple_examples_solutions.ipynb",
    "02-Binaer_klassifikasjon.ipynb": "02-Binary_classification.ipynb",
    "02a-Binaer_klassifikasjon_losninger.ipynb": "02a-Binary_classification_solutions.ipynb",
    "03-PyCaret_hurtigguide.ipynb": "03-PyCaret_quickguide.ipynb",
    "03a-PyCaret_hurtigguide_losninger.ipynb": "03a-PyCaret_quickguide_solutions.ipynb",
    "Lab-Lynkurs": "Lab-QuickStart",
    "lynkurs-ai-python.ipynb": "quickstart-ai-python.ipynb",
    "arvidl/ELMED219-2026": "arvidl/BMED365-2026",
}


def translate_text(text):
    """Translate Norwegian text to English using the translation dictionary."""
    result = text
    
    # First do URL translations
    for nor, eng in URL_TRANSLATIONS.items():
        result = result.replace(nor, eng)
    
    # Then do phrase translations (longest first to avoid partial matches)
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    for nor, eng in sorted_translations:
        result = result.replace(nor, eng)
    
    return result


def translate_notebook(input_path, output_path=None):
    """Translate a Jupyter notebook from Norwegian to English."""
    if output_path is None:
        output_path = input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Translate all cells
    for cell in nb.get('cells', []):
        if 'source' in cell:
            # Source can be a list of strings or a single string
            if isinstance(cell['source'], list):
                cell['source'] = [translate_text(line) for line in cell['source']]
            else:
                cell['source'] = translate_text(cell['source'])
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    
    print(f"Translated: {input_path} -> {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python translate_notebook.py <notebook.ipynb> [output.ipynb]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    translate_notebook(input_path, output_path)

