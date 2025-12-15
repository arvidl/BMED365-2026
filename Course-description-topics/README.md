# Course Description and Topic List

This folder contains detailed course descriptions and topic-specific Beamer presentations for BMED365.

## Main Document

- [course-description-and-topics.pdf](./course-description-and-topics.pdf) - Comprehensive course description with topic list

## Topic Presentations (Beamer)

| Topic | Folder | Description |
|-------|--------|-------------|
| **A - Ethics** | [A-Ethics](./Beamer/A-Ethics/) | Ethical considerations in AI and medicine |
| **B - Image Analysis** | [B-ImageAnalysis](./Beamer/B-ImageAnalysis/) | Medical image analysis fundamentals |
| **D - Deep Learning** | [D-DeepLearning](./Beamer/D-DeepLearning/) | Deep learning concepts and architectures |
| **E - Evaluation** | [E-Evaluation](./Beamer/E-Evaluation/) | Model evaluation metrics and methods |
| **F - Skills** | [F-Skills](./Beamer/F-Skills/) | Technical skills and tools |
| **G - Generative AI** | [G-GenerativeAI](./Beamer/G-GenerativeAI/) | Generative AI and LLMs |
| **M - Machine Learning** | [M-MachineLearning](./Beamer/M-MachineLearning/) | Machine learning fundamentals |
| **N - Graph Theory** | [N-GraphTheory](./Beamer/N-GraphTheory/) | Graph theory and network science |
| **P - PSN** | [P-PSN](./Beamer/P-PSN/) | Patient Similarity Networks |
| **S - Neurosymbolic** | [S-Neurosymbolic](./Beamer/S-Neurosymbolic/) | Neurosymbolic AI approaches |
| **T - Trustworthy** | [T-Trustworthy](./Beamer/T-Trustworthy/) | Trustworthy AI principles |
| **X - XAI** | [X-XAI](./Beamer/X-XAI/) | Explainable AI (XAI) |

## Building the Documents

To compile the LaTeX documents:

```bash
pdflatex course-description-and-topics.tex
bibtex course-description-and-topics
pdflatex course-description-and-topics.tex
pdflatex course-description-and-topics.tex
```

Each Beamer presentation in the subfolders can be compiled with:

```bash
cd Beamer/[folder]
pdflatex main.tex
```

---

*Note: These materials are provided for educational purposes as part of BMED365.*
