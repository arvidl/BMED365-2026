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

## Lecture Schedule: Tuesday, January 20, 2026

**Time:** 08:15–12:00 (3h 45min)  
**Location:** Hist 1  
**Instructor:** AL

### Overview

This 4-hour lecture provides a comprehensive introduction to Generative AI and Large Language Models with focus on biomedical applications. The schedule balances theory (50%) with hands-on practice (50%), incorporating high-quality videos, live demos, and short breaks to maintain engagement.

---

### Detailed Schedule

#### Block 1: Introduction & Foundation (08:15–09:30) - 75 min

**08:15–08:45** (30 min) | **Opening & Introduction to Generative AI**
- Welcome and learning objectives for the day
- Cover [01-introduction-genai.ipynb](notebooks/01-introduction-genai.ipynb)
  - What is Generative AI? (Discriminative vs. Generative)
  - Historical development (from ELIZA to GPT)
  - Medical applications overview
- **Format:** Lecture with interactive discussion

**08:45–09:00** (15 min) | **Video: 3Blue1Brown - "But what is a GPT?"**
- Introduction to the core concepts visually by 3Blue1Brown [[Large Language Models explained briefly](https://youtu.be/LPZh9BOjkQs)]
- **Link:** https://www.3blue1brown.com/lessons/gpt
- Sets foundation for transformer architecture

**09:00–09:30** (30 min) | **Hands-on Demo: First Interaction with LLMs**
- Students try basic prompts with ChatGPT/Claude
- Compare outputs from different models
- Observe "hallucinations" in action
- **Materials:** Example prompts from `prompts/` folder

---

#### Block 2: Transformer Architecture (09:30–10:15) - 45 min

**09:30–10:00** (30 min) | **Video + Lecture: Understanding Transformers**
- Show 3Blue1Brown - "Attention in Transformers, visually explained" (15 min)
  - **Link:** https://www.3blue1brown.com/lessons/attention
- Brief lecture expanding on key concepts (15 min):
  - Self-attention mechanism (Query, Key, Value)
  - Positional encoding
  - Multi-head attention
- Cover highlights from [02-transformer-architecture.ipynb](notebooks/02-transformer-architecture.ipynb)

**10:00–10:15** (15 min) | **☕ BREAK**

---

#### Block 3: LLM Fundamentals & Training (10:15–11:00) - 45 min

**10:15–10:40** (25 min) | **Lecture: How LLMs Work**
- Cover [03-llm-fundamentals.ipynb](notebooks/03-llm-fundamentals.ipynb)
  - Tokenization (show live tokenizer demo)
  - Temperature and sampling strategies
  - Context window and memory limitations
  - Pre-training vs. Fine-tuning vs. RLHF
- **Live demo:** OpenAI tokenizer (https://platform.openai.com/tokenizer)

**10:40–11:00** (20 min) | **Hands-on Exercise: Temperature Experiment**
- Students experiment with different temperature settings
- Same prompt, different temperatures (0.0, 0.5, 1.0, 1.5)
- Document how outputs change (deterministic vs. creative)
- **Format:** Individual/pair work with discussion

---

#### Block 4: Prompt Engineering (11:00–11:45) - 45 min

**11:00–11:25** (25 min) | **Lecture: From Prompts to Context Engineering**
- Cover [04-prompt-engineering.ipynb](notebooks/04-prompt-engineering.ipynb)
  - Basic principles: Clear, Specific, Contextual, Iterative
  - Zero-shot vs. Few-shot learning
  - Chain-of-Thought (CoT) reasoning
  - Context engineering for medical applications
  - Safety considerations in medical prompts

**11:25–11:45** (20 min) | **Hands-on: Medical Prompt Engineering**
- Work with real clinical scenarios from `prompts/` folder:
  - Clinical notes summarization (`kliniske_notater.txt`)
  - Patient conversation analysis (`pasientsamtale.txt`)
  - Journal abstract summary (`journalsammendrag.txt`)
- Students practice zero-shot, few-shot, and CoT techniques
- **Format:** Small groups (2-3 students), share results

---

#### Block 5: Ethics & Future Directions (11:45–12:00) - 15 min

**11:45–11:55** (10 min) | **Lecture: AI Ethics in Healthcare**
- Cover key points from [06-ai-ethics-medicine.ipynb](notebooks/06-ai-ethics-medicine.ipynb)
  - Bias and fairness in medical AI
  - Privacy and GDPR considerations
  - Clinical responsibility (who is accountable?)
  - EU AI Act and medical device regulation

**11:55–11:58** (3 min) | **Brief Introduction: Advanced Topics**
- Quick overview of [07-trustworthy-ai.ipynb](notebooks/07-trustworthy-ai.ipynb)
  - Reliability, robustness, human-in-the-loop systems
- Quick overview of [08-neurosymbolic-ai.ipynb](notebooks/08-neurosymbolic-ai.ipynb)
  - Combining neural networks with knowledge graphs
  - Future of reasoning in medical AI

**11:58–12:00** (2 min) | **Closing & Next Steps**
- Reminder about reflection exercise (300-500 words)
- Encourage students to explore remaining notebooks independently
- Q&A preview for next session

---

### Materials Checklist

**For Instructor:**
- [ ] Slides covering all core topics (can extract from notebooks)
- [ ] Links to 3Blue1Brown videos ready
- [ ] Access to ChatGPT/Claude for live demos
- [ ] Tokenizer demo ready (https://platform.openai.com/tokenizer)
- [ ] Clinical prompt examples from `prompts/` folder

**For Students:**
- [ ] Google Colab access (or local Jupyter setup)
- [ ] Access to at least one LLM (ChatGPT free tier, Claude, etc.)
- [ ] Notebooks 01-04, 06 open and ready
- [ ] Copy of example prompts from `prompts/` folder

---

### Videos to Include

1. **3Blue1Brown - "But what is a GPT?"** (~15 min)
   - https://www.3blue1brown.com/lessons/gpt
   - Covers: LLM basics, next-word prediction, training process, RLHF
   
2. **3Blue1Brown - "Attention in Transformers, visually explained"** (~15 min)
   - https://www.3blue1brown.com/lessons/attention
   - Covers: Query/Key/Value, self-attention, multi-head attention

**Total video time:** ~30 minutes (13% of lecture time)

---

### Time Distribution

**Breakdown:**
- 🎤 **Theory/Lecture:** ~100 min (44%)
- 🎥 **Videos:** ~30 min (13%)
- 💻 **Hands-on/Demos:** ~65 min (29%)
- ☕ **Breaks:** ~15 min (7%)
- 🤔 **Ethics & Closing:** ~15 min (7%)

---

### Teaching Tips

**Engagement Strategies:**
1. **Start strong:** Begin with a provocative question about AI in healthcare
2. **Interactive demos:** Have students call out prompts during live demos
3. **Real examples:** Use actual medical cases (anonymized) throughout
4. **Pause for questions:** Build in 2-3 min Q&A after each major concept
5. **Connect to practice:** Relate every concept to future clinical work

**Common Pitfalls to Address:**
- **Hallucinations:** Show examples early and often
- **Over-reliance:** Emphasize AI as assistant, not replacement
- **Privacy:** Stress NEVER using real patient data in public LLMs
- **Critical thinking:** Encourage skepticism and verification

**Backup Plans:**
- If technical issues: Have pre-recorded demo screenshots ready
- If ahead of schedule: Expand hands-on time for prompt engineering
- If behind schedule: Shorten introduction, combine some hands-on exercises

---

### Post-Lecture Materials

Students should complete independently:
- [ ] Notebooks 05 (XAI), 07 (Trustworthy AI), 08 (Neurosymbolic AI)
- [ ] Notebook 09 (API usage) - for those interested in programming
- [ ] Reflection exercise (300-500 words)
- [ ] Explore Medical AI Assistant GPT (link in Resources section above)

---

*Last updated: January 2026*

Can you perform a similar brush-up and "didactification" of notebook 01- in Lab3-GenAI-LLM as done in Lab2-DL for the notebooks A1, ...., E3 , e.g., Learning Objectives (at the start); Enhanced Code Comments; Self-Check Questions; Glossary of Key Terms; Further Reading & Key Takeaways; Ensuring reproducibility of the notebook.
