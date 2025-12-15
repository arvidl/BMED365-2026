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
    "Lynkurs i AI-assistert Python-programmering": "Quick Start: AI-Assisted Python Programming",
    "Velkommen til ditt første møte med Python-programmering!": "Welcome to your first encounter with Python programming!",
    "I dette lynkurset skal du lære:": "In this quick start course, you will learn:",
    "Hvordan du bruker **Google Colab** til å skrive og kjøre Python-kode": "How to use **Google Colab** to write and run Python code",
    "Grunnleggende **Python-syntaks** og konsepter": "Basic **Python syntax** and concepts",
    "Hvordan du bruker **AI-verktøy** som programmeringspartner": "How to use **AI tools** as a programming partner",
    "Praktiske eksempler fra **medisin og helsefag**": "Practical examples from **medicine and health sciences**",
    "**Målgruppe:** Medisinstudenter uten tidligere programmeringserfaring": "**Target audience:** Medical students with no prior programming experience",
    "**Tid:**": "**Time:**",
    "Modul 1: Velkommen og oppsett": "Module 1: Welcome and Setup",
    "Modul 2: Python-grunnlag": "Module 2: Python Basics",
    "Modul 3: AI som programmeringspartner": "Module 3: AI as Programming Partner",
    "Modul 4: Medisinsk eksempel fra Lab 0": "Module 4: Medical Example from Lab 0",
    "Modul 5: Nettverkseksempel fra Lab 1": "Module 5: Network Example from Lab 1",
    "Modul 6: Oppsummering": "Module 6: Summary",
    
    # Programming explanations
    "Hva er programmering?": "What is Programming?",
    "**Programmering** er å gi datamaskinen instruksjoner for å løse oppgaver.": "**Programming** is giving the computer instructions to solve tasks.",
    "Tenk på det som en oppskrift": "Think of it as a recipe",
    "du forteller datamaskinen nøyaktig hva den skal gjøre, steg for steg": "you tell the computer exactly what to do, step by step",
    "Hvorfor Python?": "Why Python?",
    "Python er et av de mest populære programmeringsspråkene i verden, spesielt innen:": "Python is one of the most popular programming languages in the world, especially in:",
    "**Medisinsk forskning** og analyse av helsedata": "**Medical research** and health data analysis",
    "**Bioinformatikk** og genetisk analyse": "**Bioinformatics** and genetic analysis",
    "**Kunstig intelligens** og maskinlæring": "**Artificial intelligence** and machine learning",
    "**Datavitenskap** og statistikk": "**Data science** and statistics",
    "Python er designet for å være **lesbart**": "Python is designed to be **readable**",
    "koden ligner nesten vanlig engelsk!": "the code almost resembles plain English!",
    
    # Google Colab section
    "Hva er Google Colab?": "What is Google Colab?",
    "**Google Colab** (Colaboratory) er en gratis tjeneste som lar deg:": "**Google Colab** (Colaboratory) is a free service that allows you to:",
    "Skrive og kjøre Python-kode direkte i nettleseren": "Write and run Python code directly in the browser",
    "Lagre arbeidet ditt i Google Drive": "Save your work in Google Drive",
    "Dele notebooks med andre": "Share notebooks with others",
    "Bruke AI-assistanse til å skrive kode": "Use AI assistance to write code",
    "Du trenger **ingen installasjon**": "You need **no installation**",
    "bare en nettleser og en Google-konto!": "just a browser and a Google account!",
    "Jupyter Notebook-formatet": "The Jupyter Notebook Format",
    "Denne filen er en **Jupyter Notebook** (.ipynb).": "This file is a **Jupyter Notebook** (.ipynb).",
    "Den består av **celler** som kan inneholde:": "It consists of **cells** that can contain:",
    "**Kode** – Python-kode som kan kjøres": "**Code** – Python code that can be executed",
    "**Tekst** – Forklaringer og dokumentasjon (som denne cellen)": "**Text** – Explanations and documentation (like this cell)",
    "For å kjøre en kodecelle: **Shift + Enter**": "To run a code cell: **Shift + Enter**",
    "(eller klikk på ▶-knappen)": "(or click the ▶ button)",
    
    # First code section
    "DIN FØRSTE KODELINJE!": "YOUR FIRST LINE OF CODE!",
    "Linjer som starter med # er \"kommentarer\"": "Lines starting with # are \"comments\"",
    "de kjøres ikke, men forklarer koden": "they do not run, but explain the code",
    "Trykk Shift+Enter for å kjøre denne cellen:": "Press Shift+Enter to run this cell:",
    "Hei, verden!": "Hello, World!",
    "Gratulerer! 🎉": "Congratulations! 🎉",
    "Du har nettopp kjørt din første Python-kode!": "You just ran your first Python code!",
    
    # Environment check
    "MILJØSJEKK": "ENVIRONMENT CHECK",
    "Denne cellen sjekker om vi kjører i Google Colab": "This cell checks if we are running in Google Colab",
    "Kjører i Google Colab – perfekt!": "Running in Google Colab – perfect!",
    "Kjører IKKE i Google Colab": "NOT running in Google Colab",
    "det går fint, men noen funksjoner kan variere": "that is fine, but some features may vary",
    
    # Variables section
    "Variabler – lagre informasjon": "Variables – Storing Information",
    "En **variabel** er som en merkelapp på en boks.": "A **variable** is like a label on a box.",
    "Du gir boksen et navn, og legger noe oppi.": "You give the box a name and put something in it.",
    
    # Tips and hints
    "💡 **Tips:**": "💡 **Tip:**",
    "Din tur!": "Your Turn!",
    "🤖 **AI-hint:**": "🤖 **AI hint:**",
    "Når du ser dette symbolet, får du tips om hvordan AI kan hjelpe deg.": "When you see this symbol, you get tips on how AI can help you.",
    
    # BMI section
    "MEDISINSK EKSEMPEL: Beregne BMI": "MEDICAL EXAMPLE: Calculate BMI",
    "Formel:": "Formula:",
    "BMI = vekt (kg) / høyde (m)²": "BMI = weight (kg) / height (m)²",
    
    # AI section
    "Bruke Gemini i Google Colab": "Using Gemini in Google Colab",
    "Google Colab har innebygd AI-assistanse.": "Google Colab has built-in AI assistance.",
    "Be AI lage en funksjon": "Ask AI to Create a Function",
    "Be AI forklare kode": "Ask AI to Explain Code",
    "Be AI hjelpe med feilsøking": "Ask AI to Help with Debugging",
    "Effektive AI-prompts for programmering": "Effective AI Prompts for Programming",
    
    # Machine Learning section
    "Hva er maskinlæring?": "What is Machine Learning?",
    "I vanlig programmering gir vi datamaskinen eksplisitte regler.": "In regular programming, we give the computer explicit rules.",
    "I maskinlæring gir vi den data og lar den lære mønstrene selv!": "In machine learning, we give it data and let it learn the patterns itself!",
    "IMPORTER BIBLIOTEKER": "IMPORT LIBRARIES",
    "Alle biblioteker importert!": "All libraries imported!",
    "Laste og utforske data": "Load and Explore Data",
    "Visualisere data": "Visualize Data",
    "Trene en maskinlæringsmodell": "Train a Machine Learning Model",
    "Modellen er trent!": "The model is trained!",
    
    # Network section
    "Hva er en graf/nettverk?": "What is a Graph/Network?",
    "En graf består av:": "A graph consists of:",
    "**Noder** (punkter) – objektene vi studerer": "**Nodes** (points) – the objects we study",
    "**Kanter** (linjer) – forbindelsene mellom dem": "**Edges** (lines) – the connections between them",
    "LAG EN ENKEL GRAF": "CREATE A SIMPLE GRAPH",
    "VISUALISER NETTVERKET": "VISUALIZE THE NETWORK",
    "Pasient-likhetsnettverk": "Patient Similarity Network",
    
    # Summary section
    "Oppsummering": "Summary",
    "Hva har vi lært i dag?": "What Have We Learned Today?",
    "Hovedpunkter:": "Key Points:",
    "Veien videre": "The Road Ahead",
    "Lykke til videre i ELMED219!": "Good luck in BMED365!",
    "Lykke til videre!": "Good luck going forward!",
    
    # General translations
    "Versjon ": "Version ",
    "ELMED219-2026": "BMED365-2026",
    "ELMED219": "BMED365",
}

# URL path translations
URL_TRANSLATIONS = {
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

