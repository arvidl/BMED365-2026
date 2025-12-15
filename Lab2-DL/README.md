# Lab 2: Deep Learning (DL)

In this lab, we explore concepts and applications of **deep learning** in medicine and biomedical research.

---

## Learning Objectives

After completing this lab, you should be able to:

| Topic | Learning Objective |
|-------|-------------------|
| **Neural networks** | Explain what a neural network is, compare biological and artificial neurons |
| **Learning** | Understand backpropagation, gradient descent, and the training process |
| **MLP** | Build and train a multilayer perceptron for classification |
| **CNN** | Explain how convolutional neural networks work for image analysis |
| **PyTorch** | Use PyTorch to build and train neural networks |
| **Medical AI** | Apply deep learning to medical data (heart disease, ECG, MRI) |
| **Explainable AI** | Use Grad-CAM to understand model decisions |

---

## Prioritization Guide

Notebooks are organized into **6 parts (A-F)** with clear prioritization. **Start with the core material** and continue based on time and interest.

### Recommended Learning Path for Medical Students

```
1. Start with Part B (NN theory) → Fundamental understanding
2. Continue with Part A core → Practical hands-on with MNIST
3. Then Part C and D → CNN in practice and medical image analysis
4. Optional: Part E and F based on interest
```

---

## Notebook Overview

### PART A: MNIST Foundation

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| **1** | [A1-CNN-intro](notebooks/A1-CNN-intro.ipynb) | Conceptual intro to CNN with medical analogies | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A1-CNN-intro.ipynb) |
| 3 | [A2-PyTorch-Lightning](notebooks/A2-PyTorch-Lightning.ipynb) | Introduction to PyTorch and Lightning | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A2-PyTorch-Lightning.ipynb) |
| 3 | [A3-MNIST-datacollection](notebooks/A3-MNIST-datacollection.ipynb) | Data collection and organization | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A3-MNIST-datacollection.ipynb) |
| 3 | [A4-MNIST-Random-Forest](notebooks/A4-MNIST-Random-Forest.ipynb) | ML baseline with Random Forest | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A4-MNIST-Random-Forest.ipynb) |
| **1** | [A5-MNIST-MLP](notebooks/A5-MNIST-MLP.ipynb) | Your first deep learning model (MLP) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A5-MNIST-MLP.ipynb) |
| **1** | [A6-MNIST-CNN](notebooks/A6-MNIST-CNN.ipynb) | MNIST with CNN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/A6-MNIST-CNN.ipynb) |

### PART B: Neural Networks – Theory and Medical Application

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| **1** | [B1-nn-intro](notebooks/B1-nn-intro.ipynb) | Neural networks in humans and machines | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/B1-nn-intro.ipynb) |
| **1** | [B2-learning-in-nn](notebooks/B2-learning-in-nn.ipynb) | How neural networks learn | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/B2-learning-in-nn.ipynb) |
| **1** | [B3-heart-disease-classification](notebooks/B3-heart-disease-classification.ipynb) | Heart disease classification (UCI) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/B3-heart-disease-classification.ipynb) |
| **1** | [B4-ECG-arrhythmia-CNN](notebooks/B4-ECG-arrhythmia-CNN.ipynb) | ECG arrhythmia classification with CNN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/B4-ECG-arrhythmia-CNN.ipynb) |

### PART C: CNN Image Classification

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| **2** | [C1-cnn-environment-architecture](notebooks/C1-cnn-environment-architecture.ipynb) | Environment setup and CNN architecture | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/C1-cnn-environment-architecture.ipynb) |
| **2** | [C2-cnn-training](notebooks/C2-cnn-training.ipynb) | Training and saving model | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/C2-cnn-training.ipynb) |
| **2** | [C3-cnn-testing-gradcam](notebooks/C3-cnn-testing-gradcam.ipynb) | Testing, evaluation, and Grad-CAM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/C3-cnn-testing-gradcam.ipynb) |
| **2** | [C4-cnn-conclusion](notebooks/C4-cnn-conclusion.ipynb) | Summary and the way forward | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/C4-cnn-conclusion.ipynb) |
| 📝 | [C4a-cnn-conclusion-solutions](notebooks/C4a-cnn-conclusion-solutions.ipynb) | **Solution suggestions** with MedMNIST, ViT, and ethics | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/C4a-cnn-conclusion-solutions.ipynb) |

### PART D: Medical Image Analysis

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| **2** | [D1-MRI-dementia-classification](notebooks/D1-MRI-dementia-classification.ipynb) | MRI image analysis for dementia detection | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/D1-MRI-dementia-classification.ipynb) |

### PART E: Emotion Analysis

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| 3 | [E1-emotions-building](notebooks/E1-emotions-building.ipynb) | Emotion classification part 1 (building) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/E1-emotions-building.ipynb) |
| 3 | [E2-emotions-training](notebooks/E2-emotions-training.ipynb) | Emotion classification part 2 (training) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/E2-emotions-training.ipynb) |
| 3 | [E3-emotions-evaluation](notebooks/E3-emotions-evaluation.ipynb) | Emotion classification part 3 (evaluation) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/E3-emotions-evaluation.ipynb) |

### PART F: TabPFN – Deep Learning on Tabular Data (Advanced)

| Priority | Notebook | Description | Colab |
|:--------:|:---------|:------------|:------|
| 4 | [F1-TabPFN-intro](notebooks/F1-TabPFN-intro.ipynb) | Exploring TabPFN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/F1-TabPFN-intro.ipynb) |
| 4 | [F2-TabPFN-neuro](notebooks/F2-TabPFN-neuro.ipynb) | TabPFN in neuroscience | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab2-DL/notebooks/F2-TabPFN-neuro.ipynb) |

---

## Priority Levels

| Priority | Description | Estimated Time |
|:--------:|:------------|:--------------:|
| **1 (core)** | Essential for learning objectives – everyone should complete | 4-5 hours |
| **2 (recommended)** | Important elaboration, especially CNN and medical image analysis | 3-4 hours |
| **3 (optional)** | Supplementary material based on interest | 2-3 hours |
| **4 (advanced)** | For those who want to go deeper into modern methods | 1-2 hours |

---

## Getting Started

### Google Colab (Recommended)

1. Click the Colab badge for the notebook you want to run
2. Log in with Google account
3. Run cells with `Shift+Enter`

**Note:** Data is downloaded automatically when running notebooks.

### Local Execution

```bash
conda env create -f environment.yml
conda activate bmed365-2026
jupyter notebook
```

---

## Learning Resources

### Videos (Sorted by Duration)

| Video | Author | Duration |
|:------|:-------|:--------:|
| [What is Deep Learning?](https://youtu.be/6M5VXKLf4D4) | Simplilearn | 6 min |
| [But what is a neural network?](https://youtu.be/aircAruvnKk) | 3Blue1Brown | 19 min |
| [What is backpropagation?](https://youtu.be/Ilg3gGewQ5U) | 3Blue1Brown | 13 min |
| [Building micrograd](https://youtu.be/VMj-3S1tku0) | Andrej Karpathy | 2.5 h |

### Courses and Resources

- [MIT 6.S191: Introduction to Deep Learning](http://introtodeeplearning.com)
- [Stanford CS231n: CNNs for Visual Recognition](http://vision.stanford.edu/teaching/cs231n)
- [Learn PyTorch](https://learnpytorch.io)
- [fastMONAI](https://fastmonai.no) – Bergen-based medical AI

---

## Structure

```
Lab2-DL/
├── README.md
├── assets/           # Slides and illustrations
├── data/             # Example images
├── resources/        # Figures and illustrations
└── notebooks/
    ├── A1-A6         # MNIST foundation
    ├── B1-B4         # NN theory and medical application
    ├── C1-C4(a)      # CNN image classification + solutions
    ├── D1            # Medical MRI analysis
    ├── E1-E3         # Emotion analysis
    └── F1-F2         # TabPFN (advanced)
```

---

Developed by Arvid Lundervold, University of Bergen.

