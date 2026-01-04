
# Individual Project (BMED365): Digital Poster and Speed-Poster Presentation

*Last updated: 4 January 2026*

## Summary

The Individual Project is a **mandatory component** of BMED365 that provides students with an opportunity to independently explore a topic within computational imaging, modeling, and AI in biomedicine. During Weeks 5–7 (2026), you will develop a digital poster and deliver a speed-poster presentation, demonstrating your ability to communicate scientific concepts effectively to a multidisciplinary audience.

**Key Dates:**
- **Project period:** Weeks 5–7 (Monday 26 January – Saturday 14 February 2026)
- **Poster submission deadline:** Tuesday 10 February 2026, 23:59 via Mitt UiB
- **Speed-poster presentation session:** Wednesday 11 February 2026, 08:15–12:00, Hist 1

**Two Distinct Deliverables:**
1. **Digital Poster** — A static visual artifact submitted for review
2. **Speed-Poster Presentation** — An oral presentation that elaborates on your poster, including mandatory AI reflection in the discussion

---

## 1. Project Context and Learning Objectives

### 1.1 Position in the Course

The Individual Project bridges Block 1 (joint with ELMED219, covering foundational AI and computational medicine) and the advanced topics of Block 2 (computational imaging and modeling). This project allows you to:

- Consolidate knowledge from Block 1 while preparing for Block 2 content
- Develop independent research and communication skills
- Explore a topic aligned with your academic or professional interests

### 1.2 Learning Objectives

Upon completion of this project, you should be able to:

1. **Select and scope** an appropriate research topic within the BMED365 curriculum
2. **Critically evaluate** the role of AI in your chosen topic, including both opportunities and limitations
3. **Synthesize** information from course material, literature, and/or your own research
4. **Communicate** complex scientific concepts effectively through visual and oral presentation
5. **Engage** with peer feedback and questions in a professional setting

---

## 2. Topic Selection Guidelines

### 2.1 Thematic Scope

Your topic should engage with one or more themes relevant to BMED365. The following are examples to inspire your selection:

| Theme | Example Topics |
|-------|----------------|
| **Computational Imaging** | MRI analysis, image segmentation, imaging mass cytometry (IMC), quantitative imaging biomarkers, PET/CT reconstruction |
| **Computational Modeling** | Physiological modeling, tumor growth models, cardiovascular flow simulation, pharmacokinetic models, neural network architectures |
| **Reasoning and Data Analysis** | Machine learning for diagnosis, patient similarity networks (PSN), explainable AI (XAI), clinical decision support, natural language processing in healthcare |

**Note:** These examples are illustrative, not exhaustive. Topics from outside these specific areas are welcome, provided they connect meaningfully to the broader themes of computational biomedicine and AI in healthcare. If you are uncertain whether your topic fits, consult with the course coordinator.

### 2.2 Project Origins

Your project may originate from any of the following sources:

- **Your own research:** A topic from your master's thesis, ongoing research project, or planned future work
- **Research group context:** A question or problem relevant to your supervisor's research group
- **Literature-based:** Analysis or critique of a published scientific article
- **Future-oriented:** A research question you wish to explore in your future career in biomedical AI

### 2.3 Faculty Support

Faculty guidance is available during the project period. You may:
- Consult with the course coordinator 
- Post questions in the bmed365-channel on Discord
- Request feedback on your topic selection during Week 5

---

## 3. Deliverable 1: Digital Poster

The digital poster is a **static visual artifact** that presents your topic in a structured, visually appealing format. It should stand alone as a summary of your work, understandable without oral explanation.

### 3.1 Format Specifications

| Specification | Requirement |
|--------------|-------------|
| **Dimensions** | 70 cm × 120 cm (portrait orientation) |
| **File format** | PDF |
| **Submission** | Mitt UiB |
| **Deadline** | Tuesday 10 February 2026, 23:59 |
| **Filename** | `BMED365_Poster_[YourLastName].pdf` |

### 3.2 Template Options

You may create your poster using either of the following approaches:

#### Option A: PowerPoint/Keynote (Recommended for most students)
- **Template:** [BMED365_poster_70x120_template.pptx](./assets/BMED365_poster_70x120_template.pptx)
- **Example:** [POSTER_EXAMPLE_2021_MMIV_conf_Tumor_CNR_poster_70x120.pptx](./assets/POSTER_EXAMPLE_2021_MMIV_conf_Tumor_CNR_poster_70x120.pptx)

#### Option B: LaTeX (For students comfortable with LaTeX)
- **Template:** [BMED365_poster_template on Overleaf](./assets/latex/BMED365_poster_template/) *(see Section 3.6 for details)*
- Uses the `tikzposter` document class
- Ideal for posters with equations, algorithms, or code snippets
- Provides precise typographic control

### 3.3 Content Structure

Your poster should include the following sections:

1. **Title and Author Information**
   - Clear, descriptive title
   - Your name and affiliation (UiB, Department of Biomedicine)

2. **Introduction/Background**
   - Context and motivation
   - Research question or objective
   - Relevance to BMED365 themes

3. **Methods/Approach**
   - Methodology or analytical approach
   - Data sources (if applicable)
   - Tools and technologies used

4. **Results/Findings**
   - Key findings, analyses, or insights
   - Visual representation of data (figures, tables, diagrams)

5. **Conclusions**
   - Summary of main points
   - Implications and future directions

6. **References**
   - Key sources cited (use a consistent citation style)

**Note on AI Reflection:** The mandatory AI reflection component (see Section 4.4) is addressed during the **oral presentation and discussion**, not on the poster itself. This allows the poster to focus on core scientific content while enabling richer, interactive exploration of AI considerations during your presentation.

### 3.4 Design Principles

**Visual Hierarchy:**
- Use clear headings and consistent typography
- Maintain adequate white space for readability
- Ensure text is readable from 1–2 meters distance (e.g. 24pt body text)

**Figure Quality:**
- Use high-resolution images (e.g. 300 DPI for print)
- Include figure labels and legends
- Ensure figures are self-explanatory

**Balance:**
- Aim for approximately 40% text, 40% figures, 20% white space
- Avoid overcrowding; a poster is not a manuscript

### 3.5 Submission Checklist

- [ ] Dimensions: 70 cm × 120 cm (portrait)
- [ ] File format: PDF
- [ ] Filename: `BMED365_Poster_[YourLastName].pdf`
- [ ] All required sections included
- [ ] Figures are high resolution and labeled
- [ ] Text is readable (minimum 24pt body text)
- [ ] References included
- [ ] Submitted to Mitt UiB before deadline

### 3.6 LaTeX Poster Template Details

For students who prefer LaTeX, we provide a template using the `tikzposter` document class. This is particularly suitable if your poster includes:
- Mathematical equations or formal notation
- Algorithm pseudocode
- Code snippets
- Complex diagrams created with TikZ

**Template location:** `./assets/latex/BMED365_poster_template/`

**Overleaf:** The template is also available on Overleaf for collaborative editing and easy compilation. *(Link to be provided on Mitt UiB)*

**Key features of the LaTeX template:**
- Pre-configured 70×120 cm dimensions
- BMED365/UiB color scheme
- Example blocks for each required section
- Bibliography support via BibLaTeX
- Sample figures and equations

**Compilation:** The template compiles with `pdflatex` or `lualatex`. If using Overleaf, compilation is handled automatically.

---

## 4. Deliverable 2: Speed-Poster Presentation

The speed-poster presentation is a **dynamic oral presentation** where you elaborate on your poster, engage with your audience, and critically reflect on the role of AI in your topic. The poster itself will **not** be displayed during your presentatio - you will use separate slides.

### 4.1 Format

| Specification | Requirement |
|--------------|-------------|
| **Total duration** | Maximum 10 minutes (presentation + discussion) |
| **Suggested split** | 6–7 minutes presentation, 3–4 minutes discussion |
| **Platform** | Google Slides, PowerPoint, Keynote, or Beamer (LaTeX) |
| **Slide sharing** | Post presentation link in the bmed365-channel on Discord before the session |

### 4.2 Distinction from the Poster

The speed-poster presentation is **not** simply a reading of your poster. It serves a different purpose:

| Poster | Speed-Poster Presentation |
|--------|---------------------------|
| Static, self-contained artifact | Dynamic, interactive communication |
| Emphasizes visual summary | Emphasizes narrative and explanation |
| Designed for asynchronous viewing | Designed for live audience engagement |
| Focuses on scientific content | Includes mandatory AI reflection in discussion |
| Submitted for review | Delivered in person with Q&A |

Your presentation should **elaborate on** and **extend** your poster content, not duplicate it. Use the oral format to:
- Provide context and motivation that would not fit on the poster
- Walk through your reasoning and methodology
- Highlight key insights and their significance
- Engage with the AI reflection during discussion

### 4.3 Presentation Structure

Suggested structure for the 6–7 minute presentation portion:

| Time | Section | Content |
|------|---------|---------|
| 0:00–1:00 | **Opening** | Hook, introduce yourself and your topic |
| 1:00–2:30 | **Background** | Context, motivation, research question |
| 2:30–5:00 | **Main Content** | Methods, findings, key insights |
| 5:00–6:00 | **Conclusions** | Summary, implications, open questions |
| 6:00–7:00 | **Transition to Discussion** | Briefly frame the AI reflection themes |

### 4.4 Mandatory AI Reflection (Discussion Component)

The 3–4 minute discussion period must include explicit reflection on AI's role in your topic. This is a **critical component** of the assessment. Be prepared to address:

**A. AI Applicability**
> *"AI will be/is used for this task/topic."*
- **Why?** What specific problems can AI help solve?
- **How?** Which AI methods are most suitable (deep learning, LLMs, generative AI, etc.)?
- What are the potential benefits?

**B. AI Limitations**
> *"AI is not (fully) suitable for this task/topic."*
- **Technical limitations:** Data availability, model interpretability, computational requirements, validation challenges
- **Ethical concerns:** Bias, fairness, patient autonomy, informed consent, transparency
- **Regulatory constraints:** EU AI Act compliance, medical device regulations (MDR), GDPR considerations
- **Clinical limitations:** Need for human oversight, integration into clinical workflows, liability

The discussion format allows you to engage with these questions more naturally than a poster section would, and enables peers to ask follow-up questions that deepen the conversation.

**Tip:** Anticipate likely questions and prepare thoughtful responses. Consider what a skeptical clinician or a cautious regulator might ask about AI in your topic area.

### 4.5 Audience Considerations

Present as if speaking to **a motivated audience of non-experts**—your fellow students from diverse biomedical backgrounds. This means:

- Define technical terms when first introduced
- Use analogies and examples to explain complex concepts
- Avoid jargon-heavy explanations without context
- Connect technical content to broader biomedical relevance

### 4.6 Presentation Tips

**Preparation:**
- Prepare speaking notes for rehearsal, but avoid reading directly during the presentation
- Practice timing; 6–7 minutes requires prioritization
- Rehearse at least twice, ideally with a peer
- Prepare for the AI reflection discussion - anticipate questions

**Delivery:**
- Maintain eye contact with the audience
- Speak clearly and at a measured pace
- Show enthusiasm for your topic
- Use body language to engage the audience

**Slides:**
- Use visuals to support, not replace, your narrative
- Limit text on slides (rule of thumb: ≤6 words per line, ≤6 lines per slide)
- Ensure slides are readable from the back of the room
- Consider including a "Discussion" slide that prompts AI reflection themes

### 4.7 Presentation Checklist

- [ ] Total duration: ≤10 minutes (including discussion)
- [ ] Slides shared in Discord before session
- [ ] Content elaborates on (not duplicates) poster
- [ ] Terminology explained for non-expert audience
- [ ] Practiced at least twice with timing
- [ ] AI reflection prepared for discussion portion
- [ ] Anticipated likely questions about AI applicability/limitations

---

## 5. Assessment Criteria

This is a **mandatory pass/fail assignment**. You must complete both deliverables to pass. The following criteria will be used for formative feedback:

### 5.1 Poster Assessment

| Criterion | Indicators of Quality |
|-----------|----------------------|
| **Scientific Rigor** | Clear research question; appropriate methodology; accurate interpretation of results |
| **Visual Design** | Professional layout; effective use of figures; readable typography; appropriate balance |
| **Content Structure** | Logical organization; clear sections; concise writing |
| **Relevance** | Clear connection to BMED365 themes |

### 5.2 Presentation Assessment

| Criterion | Indicators of Quality |
|-----------|----------------------|
| **Scientific Communication** | Clear explanation of concepts; appropriate terminology; logical flow |
| **Engagement** | Eye contact; enthusiasm; connection with audience |
| **Visual Aids** | Slides support narrative; clear and readable |
| **Time Management** | Stays within 10-minute limit; balanced pacing |
| **AI Reflection** | Thoughtful analysis of AI applicability and limitations; consideration of technical, ethical, and regulatory factors; responsive to questions |

### 5.3 What Constitutes a Pass

To pass, you must:
1. Submit a poster meeting the format requirements by the deadline
2. Deliver a presentation during the scheduled session
3. Demonstrate engagement with BMED365 themes
4. Participate meaningfully in the AI reflection discussion

---

## 6. Practical Information

### 6.1 Timeline

| Week | Dates | Milestones |
|------|-------|------------|
| **5** | 26 Jan – 1 Feb | Topic selection; begin poster development; Mon 26 Jan: Motivation and demonstration session |
| **6** | 2–8 Feb | Poster development; presentation preparation |
| **7** | 9–14 Feb | **Mon 9 Feb:** Lab 4 (Computational Imaging); **Tue 10 Feb 23:59:** Poster submission deadline; **Wed 11 Feb 08:15–12:00:** Speed-poster presentation session |

### 6.2 Resources

**Templates:**
- PowerPoint: [BMED365_poster_70x120_template.pptx](./assets/BMED365_poster_70x120_template.pptx)
- LaTeX: [BMED365_poster_template/](./assets/latex/BMED365_poster_template/) *(also on Overleaf)*

**Examples:**
- [POSTER_EXAMPLE_2021_MMIV_conf_Tumor_CNR_poster_70x120.pptx](./assets/POSTER_EXAMPLE_2021_MMIV_conf_Tumor_CNR_poster_70x120.pptx)

**Communication:**
- Course Discord: bmed365-channel
- Mitt UiB: Course page for submission and additional resources

### 6.3 Contact

- **Academic questions:** Course coordinator Arvid Lundervold
- **Administrative inquiries:** studie.biomed@uib.no

---

## 7. Connection to Final Exam

The Individual Project prepares you for the **final digital home exam in Inspera**:

- **Date:** Friday 6 March 2026, 09:00–11:00
- **Duration:** 2 hours
- **Format:** Multiple choice questions and essays
- **AI Policy:** Explicit and transparent use of AI is encouraged
- **Grading:** Pass/Fail

The skills developed in your Individual Project, particularly the critical evaluation of AI applications practiced in the discussion component, are directly relevant to the exam. The exam will assess your ability to analyze AI's role in biomedical contexts, weighing technical capabilities against ethical and regulatory constraints.

---

## Appendix A: AI Tools for Project Development

You are encouraged to use AI tools appropriately during project development. Consider the following:

| Tool | Suggested Use |
|------|---------------|
| **ChatGPT / Claude / Gemini** | Literature review support, concept explanation, draft feedback |
| **DALL-E / Midjourney** | Conceptual illustrations (with disclosure) |
| **Grammarly / LanguageTool** | Writing polish and grammar checking |
| **NotebookLM** | Document analysis and synthesis |
| **Cursor AI** | Code assistance (if your project involves programming) |

**Important:** When using AI tools, maintain academic integrity by:
- Using AI as a collaborator, not a replacement for your thinking
- Critically evaluating AI-generated content
- Disclosing AI use when relevant
- Ensuring the final work represents your understanding

---

## Appendix B: LaTeX Poster Quick Start

If you choose the LaTeX option, here is a minimal example to get started:

```latex
\documentclass[25pt, a0paper, portrait]{tikzposter}

\title{Your Poster Title Here}
\author{Your Name}
\institute{Department of Biomedicine, University of Bergen}

% BMED365 color theme
\definecolorpalette{BMEDpalette}{
    \definecolor{colorOne}{HTML}{003A70}   % UiB dark blue
    \definecolor{colorTwo}{HTML}{0077B6}   % Accent blue
    \definecolor{colorThree}{HTML}{F5F5F5} % Light background
}
\usetheme{Default}
\usecolorpalette{BMEDpalette}

\begin{document}
\maketitle

\begin{columns}
\column{0.5}

\block{Introduction}{
    Your introduction text here...
}

\block{Methods}{
    Your methods description here...
}

\column{0.5}

\block{Results}{
    Your results here...
    
    % Example figure
    % \includegraphics[width=\linewidth]{figure.pdf}
}

\block{Conclusions}{
    Your conclusions here...
}

\end{columns}

\block{References}{
    \small
    Your references here...
}

\end{document}
```

**Compilation:** Use `pdflatex` or compile via Overleaf.

**Full template:** The complete template with all sections, example figures, and bibliography setup is available in `./assets/latex/BMED365_poster_template/`.







-----


## BMED365 LaTeX Poster Template

This directory contains a LaTeX template for creating scientific posters for the BMED365 Individual Project.

### Template Overview

- **Document class:** `tikzposter`
- **Dimensions:** 70cm × 120cm (portrait orientation)
- **Color scheme:** UiB/BMED365 institutional colors

### Files

| File | Description |
|------|-------------|
| `BMED365_poster_template.tex` | Main template file |
| `README.md` | This file |

### Requirements

#### For local compilation

You need a LaTeX distribution with the following packages:
- `tikzposter` (the main poster class)
- `amsmath`, `amssymb` (mathematics)
- `graphicx` (images)
- `booktabs` (tables)
- `algorithm2e` (algorithms)
- `listings` (code)
- `hyperref` (links)
- `qrcode` (optional, for QR codes)

Most TeX distributions (TeX Live, MiKTeX) include these packages.

#### Compilation

```bash
pdflatex BMED365_poster_template.tex
```

Or use `lualatex` for better font support:

```bash
lualatex BMED365_poster_template.tex
```

#### Using Overleaf

1. Create a new project on [Overleaf](https://www.overleaf.com)
2. Upload `BMED365_poster_template.tex`
3. Compile automatically

The template is designed to compile without errors on Overleaf with default settings.

### Customization

#### Title and Author

Edit the metadata section near the top of the file:

```latex
\title{Your Poster Title Here}
\author{Your Name}
\institute{Department of Biomedicine, University of Bergen}
```

#### Adding Figures

Place your figure files in the same directory (or a `figures/` subdirectory) and include them:

```latex
\includegraphics[width=0.8\linewidth]{figures/your-figure.pdf}
```

**Tip:** Use PDF or PNG format for figures. PDF is preferred for diagrams and plots; PNG for photographs.

#### Adding Equations

```latex
\begin{equation}
    y = f(x; \theta) = \sigma(W^{(L)} \cdots \sigma(W^{(1)} x + b^{(1)}) \cdots + b^{(L)})
\end{equation}
```

#### Adding Code

```latex
\begin{lstlisting}[language=Python]
import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
\end{lstlisting}
```

#### Adding Tables

```latex
\begin{tabular}{lcc}
    \toprule
    \textbf{Model} & \textbf{Accuracy} & \textbf{F1 Score} \\
    \midrule
    Baseline CNN & 0.82 & 0.79 \\
    ResNet-50 & 0.91 & 0.88 \\
    Our Method & \textbf{0.94} & \textbf{0.92} \\
    \bottomrule
\end{tabular}
```

#### Color Customization

The template defines several colors you can use:

| Color | Hex | Usage |
|-------|-----|-------|
| `colorOne` | #003A70 | UiB dark blue (headers) |
| `colorTwo` | #0077B6 | Accent blue |
| `colorThree` | #F8F9FA | Light background |
| `uibRed` | #C8102E | UiB red |
| `successGreen` | #198754 | Positive highlights |
| `warningOrange` | #FD7E14 | Cautions |

Use in text: `\textcolor{colorTwo}{highlighted text}`

### Tips for a Good Poster

1. **Visual hierarchy:** Use clear headings and consistent formatting
2. **White space:** Don't overcrowd—aim for ~40% text, 40% figures, 20% space
3. **Readable fonts:** The template uses 25pt base size; don't go smaller than 20pt
4. **High-quality figures:** Use vector graphics (PDF) when possible
5. **Concise text:** A poster is not a paper—be brief and clear

### Troubleshooting

#### "File not found" errors
- Ensure figure files are in the correct path
- Check for typos in filenames (LaTeX is case-sensitive on Linux)

#### Compilation timeout on Overleaf
- Reduce image file sizes
- Use PDF instead of high-resolution PNG

#### Package not found
- Install the missing package via your TeX distribution's package manager
- On Overleaf, packages are usually available automatically

### Support

- **Course questions:** Contact the course coordinator
- **LaTeX questions:** Post in the bmed365-channel on Discord

---

*BMED365: Computational Imaging, Modeling and AI in Biomedicine*  
*University of Bergen, Spring 2026*


