# Quick Reference Guide: Generative AI for Healthcare

**BMED365 / ELMED219 - Lab 3**

A one-page summary of key concepts, techniques, and safety principles.

---

## Essential Vocabulary

| Term | Definition | Example |
|------|------------|---------|
| **LLM** | Large Language Model - AI trained on text | GPT-4, Claude, Gemini |
| **Token** | Basic unit of text (~0.75 words) | "healthcare" = 1-2 tokens |
| **Prompt** | Your instruction to the AI | "Summarize this note" |
| **Context Window** | Max text AI can process | GPT-4: ~128K tokens |
| **Temperature** | Creativity control (0=focused, 1=creative) | Use 0 for medical facts |
| **Hallucination** | AI-generated false information | Made-up drug dosages |
| **RAG** | Retrieval-Augmented Generation | AI + database lookup |

---

## Prompt Engineering Cheat Sheet

### Basic Principles

| Principle | Bad Example | Good Example |
|-----------|-------------|--------------|
| **Be specific** | "Tell me about diabetes" | "List 5 first-line medications for Type 2 diabetes with typical starting doses" |
| **Set a role** | - | "You are a clinical pharmacist helping a medical student understand..." |
| **Specify format** | - | "Format your response as a numbered list" |
| **Provide context** | - | "The patient is a 65-year-old with renal impairment" |

### Prompting Techniques

```
ZERO-SHOT:        "What is the mechanism of action of metformin?"

FEW-SHOT:         "Classify these findings:
                   Example 1: Fever, cough, infiltrate → Pneumonia
                   Example 2: Chest pain, ST elevation → STEMI
                   Now classify: Headache, stiff neck, photophobia → ?"

CHAIN-OF-THOUGHT: "Let's think step by step:
                   1. What are the key symptoms?
                   2. What organ systems are involved?
                   3. What diagnoses fit this pattern?"
```

### Temperature Guide

| Task | Temperature | Rationale |
|------|-------------|-----------|
| Drug information | 0.0 | Need accuracy |
| Clinical documentation | 0.2-0.3 | Mostly factual |
| Patient education | 0.3-0.5 | Some flexibility |
| Brainstorming | 0.7-0.9 | Need creativity |

---

## Safety Checklist

### Before Using AI with Patient Information

- [ ] Is there a data processing agreement (DPA)?
- [ ] Is the data anonymized or synthetic?
- [ ] Is this tool approved by your institution?
- [ ] Would I be comfortable if the patient knew?

### Before Acting on AI Output

- [ ] Have I verified factual claims?
- [ ] Is this within my competence to assess?
- [ ] Have I considered alternatives?
- [ ] Would I make this decision without AI?

### Red Flags - Stop and Verify

- Drug dosages (especially pediatric)
- Specific diagnostic criteria
- Treatment protocols
- Citation references
- Statistics and percentages

---

## Common Hallucination Types

| Type | Example | How to Detect |
|------|---------|---------------|
| **Fabricated citations** | Non-existent journal articles | Search Google Scholar |
| **Wrong dosages** | "Paracetamol 100mg/kg/day" | Check BNF/Felleskatalogen |
| **Confident errors** | Stating rare condition as common | Cross-reference |
| **Plausible nonsense** | Made-up medical terms | Verify terminology |

---

## AI Ethics Quick Reference

### Four Principles Applied to AI

| Principle | Key Question | AI Consideration |
|-----------|--------------|------------------|
| **Autonomy** | Does the patient know AI is used? | Consent and transparency |
| **Beneficence** | Does AI improve care? | Evidence of benefit |
| **Non-maleficence** | Could AI cause harm? | Error modes, safety |
| **Justice** | Is AI fair for all groups? | Bias testing |

### EU AI Act - Medical AI is "High Risk"

Requirements:
- Human oversight mandatory
- Quality and risk management
- Transparency to users
- Documentation and logging
- Accuracy, robustness, cybersecurity

---

## XAI Methods at a Glance

| Method | What it Does | Best For |
|--------|--------------|----------|
| **SHAP** | Shows feature contributions | Tabular data, global understanding |
| **LIME** | Local explanations via simple models | Individual predictions |
| **Attention** | Shows what model "looks at" | Text, understanding focus |
| **GradCAM** | Visual heatmaps for images | Medical imaging |

---

## Quick Model Comparison

| Model | Strengths | Considerations |
|-------|-----------|----------------|
| **GPT-4/4o** | Multimodal, versatile | OpenAI, cloud-based |
| **Claude 3.5** | Long context, safety-focused | Anthropic, cloud-based |
| **Gemini** | Google integration | Google, cloud-based |
| **Llama 3** | Open source, local possible | Meta, can run locally |
| **Specialized Medical LLMs** | Domain-trained | May need validation |

---

## For the Team Project

### Key Concepts for Glioblastoma Project

| Topic | Notebook | Key Takeaway |
|-------|----------|--------------|
| Prompt engineering | 04 | Structure prompts for literature review |
| XAI | 05 | Explain segmentation decisions |
| AI Ethics | 06 | Consider bias in imaging datasets |
| Trustworthy AI | 07 | Validation strategies for medical AI |
| Neurosymbolic AI | 08 | WHO classification as knowledge graph |

### Useful Prompts for Research

```
"Summarize the BraTS challenge and key winning methods"
"What are the WHO 2021 criteria for glioblastoma diagnosis?"
"Compare U-Net and Transformer approaches for tumor segmentation"
"What ethical considerations apply to AI in neuro-oncology?"
```

---

## Emergency Reference

### When AI Gives Medical Advice

**NEVER** rely solely on AI for:
- Emergency decisions
- Drug prescribing
- Diagnostic conclusions
- Treatment plans

**ALWAYS**:
1. Verify against trusted sources
2. Consult with qualified professionals
3. Consider individual patient factors
4. Document your reasoning

### Trusted Verification Sources

| Resource | Use For |
|----------|---------|
| UpToDate | Clinical guidelines |
| BNF/Felleskatalogen | Drug information |
| PubMed | Research evidence |
| WHO Guidelines | Global standards |
| Specialist societies | Specialty guidelines |

---

## Quick Links

- **OpenAI Tokenizer**: https://platform.openai.com/tokenizer
- **Medical AI Assistant GPT**: [Course-specific GPT link]
- **EU AI Act**: https://artificialintelligenceact.eu/
- **Datatilsynet (Norway)**: https://www.datatilsynet.no/

---

*Print this page and keep it handy during the course!*

*Last updated: January 2026*
