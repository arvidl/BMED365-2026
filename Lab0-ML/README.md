# Lab 0: Introduction to Theory and Tools for Machine Learning

In this first lab, we get an introduction to **machine learning**: what it is and what it's used for. Our approach will be practical, using Python and the scikit-learn library.

---

## Learning Objectives

After completing this lab, you should be able to:

| Topic | Learning Objective |
|-------|-------------------|
| **ML concepts** | Define central machine learning concepts (features, labels, training, testing) and distinguish between supervised and unsupervised learning |
| **Classification** | Understand the classification task and how it differs from regression |
| **Data splitting** | Explain why we split data into training and test sets, and use `train_test_split` |
| **Model training** | Train simple classification models (decision tree, logistic regression, k-NN) with scikit-learn |
| **Evaluation** | Calculate and interpret evaluation metrics such as accuracy, precision, recall, and F1-score |
| **Confusion matrix** | Read and interpret a confusion matrix to understand model errors |
| **ROC curve** | Understand the ROC curve and AUC as measures of model quality |
| **Cross-validation** | Use cross-validation for more robust model evaluation |
| **AutoML** | Use PyCaret for rapid prototyping and model comparison |
| **Medical context** | Understand special considerations when using ML in medicine (TRIPOD, overfitting, generalizability) |

---

## New to Python?

If you have little or no experience with Python programming, we recommend that you first complete the [**Quick Start: AI-Assisted Python Programming**](../Lab-QuickStart/README.md). This quick start course gives you:

- Practical introduction to Python and Google Colab
- Basic Python syntax (variables, data types, lists)
- Experience using AI tools (Gemini/ChatGPT) as a programming partner
- Previews of both Lab 0 and Lab 1

The quick start is specially designed for medical students without programming experience.

---

## Resources

### Slides:

| File | Description |
|:-----|:------------|
| [01-Simple_examples-slides.pptx](slides/BMED365-2026_Lab0-ML_01-Simple_examples-slides.pptx) | Introduction to machine learning |

### Notebooks:

| Notebook | Description | Colab |
|:---------|:------------|:------|
| [01-Simple_examples.ipynb](notebooks/01-Simple_examples.ipynb) | Build predictive models based on simple datasets. Practical introduction to basic ML. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab0-ML/notebooks/01-Simple_examples.ipynb) |
| [02-Binary_classification.ipynb](notebooks/02-Binary_classification.ipynb) | Central concepts in binary classification: evaluation, metrics, validation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab0-ML/notebooks/02-Binary_classification.ipynb) |
| [03-PyCaret_quickguide.ipynb](notebooks/03-PyCaret_quickguide.ipynb) | AutoML with PyCaret – rapid prototyping with caveats for medical use. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab0-ML/notebooks/03-PyCaret_quickguide.ipynb) |

### Solution Notebooks:

| Notebook | Description |
|:---------|:------------|
| [01a-Simple_examples_solutions.ipynb](notebooks/01a-Simple_examples_solutions.ipynb) | Solutions and discussions for exercises in notebook 01 |
| [02a-Binary_classification_solutions.ipynb](notebooks/02a-Binary_classification_solutions.ipynb) | Solutions for exercises in notebook 02, incl. ROC, model comparison, TRIPOD |
| [03a-PyCaret_quickguide_solutions.ipynb](notebooks/03a-PyCaret_quickguide_solutions.ipynb) | Solutions for exercises in notebook 03, incl. Iris, Breast Cancer, feature selection, hyperparameter tuning, model calibration |


## Machine Learning in Python

We use Python, the most popular programming language for machine learning. The practical content is mainly based on [Jupyter Notebooks](https://jupyter.org/), which allow us to mix code, text, results, and documentation in a single document. We also use standard data science and machine learning libraries in Python, such as [Pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/).

### Conda Environments

**Main environment:** Use `environment.yml` in the root directory for notebooks 01 and 02.

**PyCaret environment:** Notebook 03 requires PyCaret, which has dependencies that may conflict with TensorFlow/PyTorch. We recommend a separate environment:

```bash
# Create PyCaret environment
conda env create -f pycaret-environment.yml
conda activate pycaret-bmed365

# Start Jupyter
jupyter notebook
```

**Alternative: Google Colab** – All notebooks can be run in Colab without local installation. PyCaret is installed automatically when running.


## External Resources

### Machine Learning

* [Introduction to Machine Learning](https://developers.google.com/machine-learning/intro-to-ml) (Beginner, 20 min) - Google's introduction to basic ML concepts.
* [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) (Beginner, 3 hours) - Kaggle's hands-on introduction to machine learning.
* [Supervised Learning with scikit-learn](https://app.datacamp.com/learn/courses/supervised-learning-with-scikit-learn) (Intermediate, 4 hours) - Interactive introduction to ML using scikit-learn.
* [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) (Intermediate, 15 hours) - Google's practical introduction to machine learning.
* [Problem Framing](https://developers.google.com/machine-learning/problem-framing) (Intermediate, 45 min) - How to determine if ML is a good solution and how to outline an ML solution.

### Explainable AI (XAI)

* [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) - Christoph Molnar's comprehensive book on interpretable ML (free online).
* [SHAP Documentation](https://shap.readthedocs.io/) - Official documentation for the SHAP library.

### Python for Data Science

* [Intermediate Python](https://app.datacamp.com/learn/courses/intermediate-python-for-data-science) (Beginner, 4 hours) - DataCamp's data science-oriented introduction to Python.
* [Pandas](https://www.kaggle.com/learn/pandas) (Beginner, 4 hours) - Kaggle's introduction to Pandas.
* [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) - Official documentation with examples and tutorials.

### Jupyter Notebooks

* [Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101) - Jeremy Howard's introduction to Jupyter.
* [How to Use Jupyter Notebooks: The Ultimate Guide](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook) - DataCamp's thorough guide.

### Medical ML

* [Machine Learning for Healthcare](https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/) - MIT OpenCourseWare course on ML in healthcare.
* [TRIPOD Statement](https://www.tripod-statement.org/) - Guidelines for reporting predictive models in medicine.
