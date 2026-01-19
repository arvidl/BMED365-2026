# Lab 3: Generative AI and Large Language Models (LLM)

This lab provides a comprehensive introduction to generative AI and large language models (LLM) with a focus on biomedical applications. We cover everything from foundational concepts and the transformer architecture to ethical considerations, trustworthy AI, and emerging approaches like neurosymbolic AI.

> **Connection to Team Project:** This lab provides essential background for your Team Project on *Precision Medicine and Quantitative Imaging in Glioblastoma*. Notebook 08 (Neurosymbolic AI) includes a dedicated case study on brain tumor classification that directly relates to your project work.

---

## Learning Objectives

After completing this lab, you will be able to:

| Objective | Core Notebooks | Advanced Notebooks |
|-----------|----------------|-------------------|
| **Understand generative AI fundamentals** | 01, 02, 03 | - |
| **Explain transformer architecture and attention mechanism** | 02 | - |
| **Apply prompt engineering techniques for medical tasks** | 04 | 09 |
| **Evaluate explainability (XAI) in clinical AI systems** | 05 | - |
| **Analyze ethical and regulatory aspects of AI in healthcare** | 06 | 07 |
| **Assess trustworthiness and robustness of medical AI** | - | 07 |
| **Understand neurosymbolic approaches and knowledge graphs** | - | 08 |
| **Integrate LLM APIs programmatically (optional)** | - | 09 |

### Detailed Learning Outcomes by Notebook

<details>
<summary><b>Click to expand: Notebook-by-notebook learning objectives</b></summary>

#### 01 - Introduction to Generative AI
| Objective | Description |
|-----------|-------------|
| Explain generative AI | Define GenAI and contrast with discriminative AI |
| Trace historical development | Identify key milestones from ELIZA to GPT-4o and beyond |
| Understand LLM mechanics | Explain token prediction and core concepts |
| Identify medical applications | List clinical use cases with practical examples |
| Recognize limitations | Describe hallucination, bias, privacy risks, and liability issues |

#### 02 - Transformer Architecture
| Objective | Description |
|-----------|-------------|
| Understand self-attention | Explain how attention allows models to focus on relevant input |
| Visualize transformers | Create and interpret attention weight visualizations |
| Identify components | Recognize key building blocks (Q, K, V, multi-head attention) |
| Implement basic attention | Code a simplified attention mechanism from scratch |

#### 03 - LLM Fundamentals
| Objective | Description |
|-----------|-------------|
| Understand tokenization | Explain how LLMs break text into tokens |
| Apply temperature settings | Choose appropriate values for different clinical NLP tasks |
| Evaluate context windows | Assess whether medical documents fit within context limits |
| Design strategies for long documents | Apply chunking, summarization, or RAG |

#### 04 - Prompt Engineering
| Objective | Description |
|-----------|-------------|
| Distinguish prompt vs. context engineering | Understand when to craft prompts vs. compose rich context |
| Master basic prompt techniques | Apply clarity, specificity, persona, and format control |
| Use zero-shot and few-shot learning | Leverage LLMs without fine-tuning |
| Implement chain-of-thought reasoning | Guide LLMs through step-by-step clinical reasoning |
| Design safe medical prompts | Include appropriate guardrails and disclaimers |

#### 05 - Explainable AI (XAI)
| Objective | Description |
|-----------|-------------|
| Understand XAI importance | Explain why explainability is critical for trust and regulation |
| Distinguish XAI types | Differentiate global vs. local, ante-hoc vs. post-hoc |
| Apply SHAP analysis | Understand how Shapley values explain feature contributions |
| Apply LIME analysis | Explain how local surrogate models create interpretations |
| Meet clinical requirements | Discuss what clinicians need from AI explanations |

#### 06 - AI Ethics in Medicine
| Objective | Description |
|-----------|-------------|
| Identify ethical challenges | Recognize key dilemmas when AI is applied clinically |
| Understand bias types | Explain historical, representation, measurement, aggregation bias |
| Evaluate privacy risks | Assess implications of cloud vs. local AI deployments |
| Apply EU AI Act | Classify medical AI systems by risk level |
| Analyze responsibility | Determine accountability among doctors, hospitals, vendors |

#### 07 - Trustworthy AI
| Objective | Description |
|-----------|-------------|
| Define trustworthy AI | Understand the EU's seven requirements for trustworthy AI |
| Assess robustness | Identify vulnerabilities including distributional shift and adversarial attacks |
| Quantify uncertainty | Distinguish epistemic vs. aleatoric uncertainty |
| Design HITL workflows | Implement human-in-the-loop systems for safe deployment |
| Validate medical AI | Apply appropriate testing strategies |

#### 08 - Neurosymbolic AI
| Objective | Description |
|-----------|-------------|
| Distinguish AI paradigms | Explain difference between neural and symbolic approaches |
| Define neurosymbolic AI | Describe how hybrid systems combine pattern recognition with reasoning |
| Understand knowledge graphs | Explain the role of ontologies in medical AI |
| Apply to clinical domains | Analyze how neurosymbolic AI improves explainability |
| **Connect to glioma classification** | Relate concepts to neuro-oncology and the Team Project |

#### 09 - ChatGPT/Claude API
| Objective | Description |
|-----------|-------------|
| Configure API access | Set up and securely manage API keys |
| Make API calls | Communicate with ChatGPT and Claude programmatically |
| Handle errors robustly | Implement retry logic and rate limiting |
| Build medical assistants | Create LLM-based functions with safety constraints |
| Apply security best practices | Implement logging, privacy protection, human oversight |

</details>

---

## Prioritization Guide

### Core (Required) - Approx. 4-5 hours
These notebooks cover the essentials and should be reviewed by everyone:

| # | Notebook | Description | Time | 1-Click Colab |
|---|----------|-------------|------|---------------|
| 01 | [Introduction to Generative AI](notebooks/01-introduction-genai.ipynb) | Overview, history, and medical relevance | ~45 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/01-introduction-genai.ipynb) |
| 02 | [Transformer Architecture](notebooks/02-transformer-architecture.ipynb) | Self-attention and the foundation of modern AI | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/02-transformer-architecture.ipynb) |
| 03 | [LLM Fundamentals](notebooks/03-llm-fundamentals.ipynb) | Tokens, temperature, and context window | ~45 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/03-llm-fundamentals.ipynb) |
| 04 | [Prompt Engineering](notebooks/04-prompt-engineering.ipynb) | Techniques for effective communication with AI | ~90 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/04-prompt-engineering.ipynb) |

### Important (Recommended) - Approx. 2-3 hours
These notebooks provide important context for responsible use of AI in healthcare:

| # | Notebook | Description | Time | 1-Click Colab |
|---|----------|-------------|------|---------------|
| 05 | [Explainable AI (XAI)](notebooks/05-xai-explainable-ai.ipynb) | SHAP, LIME, and clinical interpretability | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/05-xai-explainable-ai.ipynb) |
| 06 | [AI Ethics in Medicine](notebooks/06-ai-ethics-medicine.ipynb) | Bias, privacy, and regulation | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/06-ai-ethics-medicine.ipynb) |

### In-Depth (Optional) - Approx. 2-3 hours
For those who want to go deeper into special topics:

| # | Notebook | Description | Time | 1-Click Colab |
|---|----------|-------------|------|---------------|
| 07 | [Trustworthy AI](notebooks/07-trustworthy-ai.ipynb) | Reliability, robustness, human-in-the-loop | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/07-trustworthy-ai.ipynb) |
| 08 | [Neurosymbolic AI](notebooks/08-neurosymbolic-ai.ipynb) | Hybrid AI, knowledge graphs, **glioma case study** | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/08-neurosymbolic-ai.ipynb) |
| 09 | [ChatGPT/Claude API](notebooks/09-chatgpt-claude-api.ipynb) | Programmatic use of LLM APIs | ~60 min | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/notebooks/09-chatgpt-claude-api.ipynb) |

### Technical Supplement
| # | Notebook | Description | 1-Click Colab |
|---|----------|-------------|---------------|
| 00 | [Test LLM Locally](00-test-llm.ipynb) | Running local models with Ollama | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab3-GenAI-LLM/00-test-llm.ipynb) |

---

## Self-Check Questions Summary

Each notebook includes interactive self-check questions to reinforce learning. Here are example topics:

| Notebook | Sample Question Topics |
|----------|----------------------|
| **01** | Discriminative vs. generative AI; Why 2017 was a breakthrough; Hallucination dangers |
| **02** | Why attention matters; Query-Key-Value intuition; Multi-head attention benefits |
| **03** | Tokenization of medical terms; Temperature selection for clinical tasks |
| **04** | Zero-shot vs. few-shot learning; Chain-of-thought for diagnosis |
| **05** | Global vs. local explainability; When to use SHAP vs. LIME |
| **06** | Four principles of medical ethics applied to AI; GDPR implications |
| **07** | EU's seven requirements for trustworthy AI; Epistemic vs. aleatoric uncertainty |
| **08** | Neural vs. symbolic AI; How knowledge graphs improve medical AI |
| **09** | API security best practices; Token economics and cost calculation |

---

## Key Concepts Glossary (Preview)

Each notebook includes a comprehensive glossary. Here are the most important terms across the lab:

| Term | Definition | First Appears |
|------|------------|---------------|
| **Attention Mechanism** | Technique allowing models to focus on relevant parts of input | 02 |
| **Chain-of-Thought (CoT)** | Prompting technique asking models to show step-by-step reasoning | 04 |
| **Context Window** | Maximum text length a model can process at once | 03 |
| **Hallucination** | When AI generates plausible but factually incorrect information | 01 |
| **Human-in-the-Loop (HITL)** | System design requiring human oversight of AI decisions | 07 |
| **Knowledge Graph** | Structured representation of entities and their relationships | 08 |
| **LIME** | Local Interpretable Model-agnostic Explanations | 05 |
| **Neurosymbolic AI** | Hybrid approach combining neural networks with symbolic reasoning | 08 |
| **RAG** | Retrieval-Augmented Generation - combining LLM with database search | 01, 03 |
| **SHAP** | SHapley Additive exPlanations - game theory-based feature attribution | 05 |
| **Temperature** | Parameter controlling randomness/creativity of LLM output | 03 |
| **Token** | Basic unit of text processing in LLMs | 03 |
| **Transformer** | Neural architecture using attention, foundation of modern LLMs | 02 |

---

## Reproducibility

All notebooks in this lab follow best practices for scientific reproducibility:

| Practice | Implementation |
|----------|---------------|
| **Random seeds** | Set at the beginning of each notebook (typically `RANDOM_SEED = 42`) |
| **Environment detection** | Automatic handling of Google Colab vs. local environments |
| **Version documentation** | Python and package versions printed at setup |
| **Timestamp logging** | Execution time recorded for traceability |
| **Deterministic operations** | PyTorch deterministic flags enabled where applicable |

> **Note:** LLM API outputs (notebooks 04, 09) are inherently stochastic. We use `temperature=0` where possible and document model versions for maximum reproducibility.

---

## Prerequisites

- Completed Lab 0 (Python basics)
- Familiarity with basic machine learning concepts (Lab 1-2)
- Google account for Colab (recommended)
- For notebook 09: API keys from OpenAI and/or Anthropic (optional)

---

## Folder Structure

```
Lab3-GenAI-LLM/
├── README.md                 # This file
├── notebooks/                # All notebooks (01-09)
│   ├── 01-introduction-genai.ipynb
│   ├── 02-transformer-architecture.ipynb
│   ├── 03-llm-fundamentals.ipynb
│   ├── 04-prompt-engineering.ipynb
│   ├── 05-xai-explainable-ai.ipynb
│   ├── 06-ai-ethics-medicine.ipynb
│   ├── 07-trustworthy-ai.ipynb
│   ├── 08-neurosymbolic-ai.ipynb      # Glioma case study
│   └── 09-chatgpt-claude-api.ipynb
├── prompts/                  # Example prompts for healthcare tasks
│   ├── clinical_notes.txt
│   ├── patient_conversation.txt
│   └── journal_summary.txt
├── resources/               # Figures and references
└── 00-test-llm.ipynb        # Technical supplement
```

---

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
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer paper (2017)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [EU AI Act](https://artificialintelligenceact.eu/) - European AI regulation
- [WHO Guidance on Large Language Models](https://www.who.int/publications/i/item/9789240084759) - Ethics and governance

---

## Reflection Exercise

After reviewing the material, write a short reflection (300-500 words) addressing:

1. **Opportunities**: How can generative AI improve clinical practice or biomedical research?
2. **Limitations**: In which situations are AI assistants NOT suitable?
3. **Responsibility**: Who is responsible when AI gives incorrect recommendations?
4. **Future**: How do you think AI will affect your future professional practice?

---

## Important Reminders

> **AI does NOT replace clinical judgment.** All AI-generated suggestions must be validated by qualified healthcare professionals.

> **Privacy first.** Never share real patient data with AI services without an approved data processing agreement.

> **Critical thinking.** AI can "hallucinate" - always be critical of output and verify facts against reliable sources.

---

## Lecture Schedule: Tuesday, January 20, 2026

**Time:** 08:15-12:00 (3h 45min)  
**Location:** Hist 1  
**Instructor:** AL

### Overview

This 4-hour lecture provides a comprehensive introduction to Generative AI and Large Language Models with focus on biomedical applications. The schedule balances theory (50%) with hands-on practice (50%), incorporating high-quality videos, live demos, and short breaks to maintain engagement.

> **Looking Ahead:** This lecture prepares you for the **Team Project on Glioblastoma** (presentation: Jan 27, report due: Jan 29). Pay special attention to how AI concepts apply to medical imaging and precision medicine. Notebook 08 includes a dedicated glioma case study.

---

### Detailed Schedule

#### Block 1: Introduction & Foundation (08:15-09:30) - 75 min

**08:15-08:45** (30 min) | **Opening & Introduction to Generative AI**
- Welcome and learning objectives for the day
- Cover [01-introduction-genai.ipynb](notebooks/01-introduction-genai.ipynb)
  - What is Generative AI? (Discriminative vs. Generative)
  - Historical development (from ELIZA to GPT)
  - Medical applications overview
- **Format:** Lecture with interactive discussion

**08:45-09:00** (15 min) | **Video: 3Blue1Brown - "But what is a GPT?"**
- Introduction to core concepts visually by 3Blue1Brown [[Large Language Models explained briefly](https://youtu.be/LPZh9BOjkQs)]
- **Link:** https://www.3blue1brown.com/lessons/gpt
- Sets foundation for transformer architecture

**09:00-09:30** (30 min) | **Hands-on Demo: First Interaction with LLMs**
- Students try basic prompts with ChatGPT/Claude
- Compare outputs from different models
- Observe "hallucinations" in action
- **Materials:** Example prompts from `prompts/` folder

---

#### Block 2: Transformer Architecture (09:30-10:15) - 45 min

**09:30-10:00** (30 min) | **Video + Lecture: Understanding Transformers**
- Show 3Blue1Brown - "Attention in Transformers, visually explained" (15 min)
  - **Link:** https://www.3blue1brown.com/lessons/attention
- Brief lecture expanding on key concepts (15 min):
  - Self-attention mechanism (Query, Key, Value)
  - Positional encoding
  - Multi-head attention
- Cover highlights from [02-transformer-architecture.ipynb](notebooks/02-transformer-architecture.ipynb)

**10:00-10:15** (15 min) | **BREAK**

---

#### Block 3: LLM Fundamentals & Training (10:15-11:00) - 45 min

**10:15-10:40** (25 min) | **Lecture: How LLMs Work**
- Cover [03-llm-fundamentals.ipynb](notebooks/03-llm-fundamentals.ipynb)
  - Tokenization (show live tokenizer demo)
  - Temperature and sampling strategies
  - Context window and memory limitations
  - Pre-training vs. Fine-tuning vs. RLHF
- **Live demo:** OpenAI tokenizer (https://platform.openai.com/tokenizer)

**10:40-11:00** (20 min) | **Hands-on Exercise: Temperature Experiment**
- Students experiment with different temperature settings
- Same prompt, different temperatures (0.0, 0.5, 1.0, 1.5)
- Document how outputs change (deterministic vs. creative)
- **Format:** Individual/pair work with discussion

---

#### Block 4: Prompt Engineering (11:00-11:45) - 45 min

**11:00-11:25** (25 min) | **Lecture: From Prompts to Context Engineering**
- Cover [04-prompt-engineering.ipynb](notebooks/04-prompt-engineering.ipynb)
  - Basic principles: Clear, Specific, Contextual, Iterative
  - Zero-shot vs. Few-shot learning
  - Chain-of-Thought (CoT) reasoning
  - Context engineering for medical applications
  - Safety considerations in medical prompts

**11:25-11:45** (20 min) | **Hands-on: Medical Prompt Engineering**
- Work with real clinical scenarios from `prompts/` folder:
  - Clinical notes summarization (`kliniske_notater.txt`)
  - Patient conversation analysis (`pasientsamtale.txt`)
  - Journal abstract summary (`journalsammendrag.txt`)
- Students practice zero-shot, few-shot, and CoT techniques
- **Format:** Small groups (2-3 students), share results

---

#### Block 5: Ethics, Advanced Topics & Team Project Preview (11:45-12:00) - 15 min

**11:45-11:52** (7 min) | **Lecture: AI Ethics in Healthcare**
- Cover key points from [06-ai-ethics-medicine.ipynb](notebooks/06-ai-ethics-medicine.ipynb)
  - Four principles of medical ethics applied to AI
  - Bias and fairness in medical AI
  - Privacy and GDPR considerations
  - EU AI Act and medical device regulation

**11:52-11:58** (6 min) | **Preview: Advanced Topics & Team Project Connection**
- Quick overview of [07-trustworthy-ai.ipynb](notebooks/07-trustworthy-ai.ipynb)
  - Reliability, robustness, human-in-the-loop systems
- **Spotlight on [08-neurosymbolic-ai.ipynb](notebooks/08-neurosymbolic-ai.ipynb)**
  - Combining neural networks with knowledge graphs
  - **Glioma case study**: Direct connection to your Team Project
  - How ontologies (WHO Classification, SNOMED CT) improve medical AI
  - Agentic AI for clinical decision support
- Future of reasoning in medical AI

**11:58-12:00** (2 min) | **Closing & Next Steps**
- Reminder about reflection exercise (300-500 words)
- **Team Project timeline:**
  - Presentations: Tuesday, January 27, 2026
  - Report deadline: Thursday, January 29, 2026
- Encourage students to explore remaining notebooks independently, especially:
  - Notebook 08 for glioma/neuro-oncology context
  - Notebook 05 (XAI) for understanding how to interpret AI predictions
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
- **Theory/Lecture:** ~100 min (44%)
- **Videos:** ~30 min (13%)
- **Hands-on/Demos:** ~65 min (29%)
- **Breaks:** ~15 min (7%)
- **Ethics & Closing:** ~15 min (7%)

---

### Teaching Tips

**Engagement Strategies:**
1. **Start strong:** Begin with a provocative question about AI in healthcare
2. **Interactive demos:** Have students call out prompts during live demos
3. **Real examples:** Use actual medical cases (anonymized) throughout
4. **Pause for questions:** Build in 2-3 min Q&A after each major concept
5. **Connect to practice:** Relate every concept to future clinical work
6. **Team Project connection:** Reference glioblastoma/imaging when discussing applications

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
- [ ] **Especially 08** for Team Project preparation (glioma case study)
- [ ] Notebook 09 (API usage) - for those interested in programming
- [ ] Reflection exercise (300-500 words)
- [ ] Explore Medical AI Assistant GPT (link in Resources section above)

---

## Connection to Team Project: Glioblastoma

Your **Team Project on Precision Medicine and Quantitative Imaging in Glioblastoma** directly connects to several concepts in this lab:

| Lab 3 Topic | Team Project Relevance |
|-------------|----------------------|
| **LLM fundamentals** (03) | AI-assisted literature review and synthesis |
| **Prompt engineering** (04) | Effectively querying AI for research insights |
| **Explainable AI** (05) | Interpreting deep learning segmentation results |
| **AI Ethics** (06) | Privacy, bias, and fairness in medical imaging AI |
| **Trustworthy AI** (07) | Validation strategies for brain tumor segmentation |
| **Neurosymbolic AI** (08) | **WHO Classification, knowledge graphs, hybrid AI for glioma** |

### Key Section in Notebook 08

Notebook 08 includes a dedicated section: **"Case Study: Neurosymbolic AI for Brain Tumors (Glioma)"** covering:
- How WHO 2021 CNS tumor classification can be encoded as ontology
- Integration of imaging features with molecular markers (IDH, MGMT)
- Agentic AI for clinical decision support in neuro-oncology
- Knowledge graphs linking patient data, imaging, and outcomes

> **Recommendation:** Teams should review Notebook 08 before finalizing their research plan to understand how AI approaches can enhance glioblastoma diagnosis and treatment planning.

---

*Last updated: January 2026*

---

<details>
<summary><b>Version History</b></summary>

| Date | Changes |
|------|---------|
| January 2026 | Major enhancement: Added detailed learning objectives from all notebooks; Self-check questions summary; Glossary preview; Reproducibility section; Team Project connection emphasized; Lecture schedule updated with glioma focus; Notebook 08 spotlighted for Team Project relevance |
| January 2026 | Initial version with basic structure |

</details>
