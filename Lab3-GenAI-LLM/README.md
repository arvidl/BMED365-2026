# Lab 3: Generative AI and Large Language Models (LLM)

This lab introduces generative AI and large language models (LLM) with a focus on biomedical applications. We cover everything from basic concepts to ethical issues and future directions such as neurosymbolic AI.

## Learning Objectives

After completing this lab, you should be able to:

- Understand the basic principles behind generative AI and the transformer architecture
- Explain how large language models (LLM) work
- Apply prompt engineering techniques for medical tasks
- Evaluate explainability (XAI) and trustworthiness in AI systems
- Reflect on ethical aspects of AI in healthcare
- Know about neurosymbolic approaches and their potential

---

## Prioritization Guide

### Core (Required) - Approx. 4-5 hours
These notebooks cover the essentials and should be reviewed by everyone:

| # | Notebook | Description | Time |
|---|----------|-------------|------|
| 01 | [Introduction to Generative AI](notebooks/01-introduction-genai.ipynb) | Overview, history, and medical relevance | ~45 min |
| 02 | [Transformer Architecture](notebooks/02-transformer-architecture.ipynb) | Self-attention and the foundation of modern AI | ~60 min |
| 03 | [LLM Fundamentals](notebooks/03-llm-fundamentals.ipynb) | Tokens, temperature, and context window | ~45 min |
| 04 | [Prompt Engineering](notebooks/04-prompt-engineering.ipynb) | Techniques for effective communication with AI | ~90 min |

### Important (Recommended) - Approx. 2-3 hours
These notebooks provide important context for responsible use of AI in healthcare:

| # | Notebook | Description | Time |
|---|----------|-------------|------|
| 05 | [Explainable AI (XAI)](notebooks/05-xai-explainable-ai.ipynb) | SHAP, LIME, and clinical interpretability | ~60 min |
| 06 | [AI Ethics in Medicine](notebooks/06-ai-ethics-medicine.ipynb) | Bias, privacy, and regulation | ~60 min |

### In-Depth (Optional) - Approx. 2-3 hours
For those who want to go deeper into special topics:

| # | Notebook | Description | Time |
|---|----------|-------------|------|
| 07 | [Trustworthy AI](notebooks/07-trustworthy-ai.ipynb) | Reliability, robustness, and human-in-the-loop | ~60 min |
| 08 | [Neurosymbolic AI](notebooks/08-neurosymbolic-ai.ipynb) | Hybrid AI and knowledge graphs | ~60 min |
| 09 | [ChatGPT/Claude API](notebooks/09-chatgpt-claude-api.ipynb) | Programmatic use of LLM APIs | ~60 min |

### Technical Supplement
| # | Notebook | Description |
|---|----------|-------------|
| 00 | [Test LLM Locally](00-test-llm.ipynb) | Running local models with Ollama |

---

## Prerequisites

- Completed Lab 0 (Python basics)
- Familiarity with basic machine learning (Lab 1-2)
- Google account for Colab (recommended)

## Folder Structure

```
Lab3-GenAI-LLM/
├── README.md                 # This file
├── notebooks/                # All notebooks (01-09)
├── prompts/                  # Example prompts for healthcare tasks
│   ├── clinical_notes.txt
│   ├── patient_conversation.txt
│   └── journal_summary.txt
├── resources/               # Figures and references
└── 00-test-llm.ipynb        # Technical supplement
```

## Resources and Tools

### AI Assistants
- [Medical AI Assistant (GPT)](https://chatgpt.com/g/g-d90dfN17H-medical-ai-assistant-uibmed-elmed219-bmed365) - Customized for ELMED219/BMED365
- [NotebookLM](https://notebooklm.google.com/) - Google's AI for document analysis
- [Claude](https://claude.ai/) - Anthropic's AI assistant
- [ChatGPT](https://chat.openai.com/) - OpenAI's AI assistant
    - [Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-2_prompting_guide) - GPT-5.2 Prompting Guide

### Development Tools
- [Google Colab](https://colab.research.google.com/) - Run notebooks in the browser
- [Cursor AI](https://cursor.sh/) - AI-powered code editor
   - [Tips & Tricks](https://github.com/murataslan1/cursor-ai-tips) - "The ultimate guide to mastering Cursor AI IDE"
   - [browser-visual-editor](https://cursor.com/blog/browser-visual-editor) - A visual editor for Cursor [Browser](https://cursor.com/docs/agent/browser)

### Further Reading
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer paper
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [EU AI Act](https://artificialintelligenceact.eu/) - European AI regulation

---

## Reflection Exercise

After reviewing the material, write a short reflection (300-500 words) addressing:

1. **Opportunities**: How can generative AI improve clinical practice or biomedical research?
2. **Limitations**: In which situations are AI assistants NOT suitable?
3. **Responsibility**: Who is responsible when AI gives incorrect recommendations?
4. **Future**: How do you think AI will affect your future professional practice?

---

## Important Reminders

> **AI does not replace clinical judgment.** All AI-generated suggestions must be validated by qualified healthcare professionals.

> **Privacy first.** Never share real patient data with AI services without an approved data processing agreement.

> **Critical thinking.** AI can "hallucinate" - always be critical of output and verify facts.

---

*Last updated: December 2025*

