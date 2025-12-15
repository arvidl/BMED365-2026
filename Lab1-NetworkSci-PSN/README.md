# Lab 1: Network Science and Patient Similarity Networks (PSN)

This lab provides a practical, example-based introduction to **graph theory**, **network science**, and the concept of **Patient Similarity Networks** (PSN). We use *NetworkX* – a Python library for creating, manipulating, and analyzing complex networks.

---

## Learning Objectives

After completing this lab, you should be able to:

| Topic | Learning Objective |
|-------|-------------------|
| **Graph theory** | Understand what a graph is (nodes, edges) and distinguish between undirected/directed and weighted/unweighted graphs |
| **Adjacency matrices** | Represent graphs as matrices and understand the relationship between graph and matrix |
| **Network science** | Calculate and interpret central network metrics (centrality, clustering coefficient, density) |
| **NetworkX** | Build, manipulate, and visualize networks in Python with NetworkX |
| **Similarity calculation** | Calculate similarity between data points using distance measures (Euclidean, Manhattan, Gower) |
| **Patient similarity networks** | Construct PSN from clinical data and interpret the network structure medically |
| **Community detection** | Apply algorithms (Louvain) to identify natural groupings in networks |
| **Clinical application** | Understand how PSN can be used to discover patient subgroups and support precision medicine |

---

## New to Python?

If you have little or no experience with Python programming, we recommend that you first complete the [**Quick Start: AI-Assisted Python Programming**](../Lab-QuickStart/README.md). This quick start course gives you:

- Practical introduction to Python and Google Colab
- Basic Python syntax (variables, data types, lists)
- Experience using AI tools (Gemini/ChatGPT) as a programming partner
- Previews of both Lab 0 (machine learning) and Lab 1 (networks)

The quick start is specially designed for medical students without programming experience.

---

## AI-Assisted Learning

<img src="../assets/GPT-MedAI.png" width="500"><br>

If you have access to [ChatGPT Plus](https://openai.com/blog/chatgpt-plus), you can try [**Medical AI Assistant (UiBmed - ELMED219 & BMED365)**](https://chat.openai.com/g/g-d90dfN17H-medical-ai-assistant-uibmed-elmed219-bmed365) for help with questions related to graph theory, network science, and patient similarity networks (see also [this document](./assets/ELMED219_BMED365_2024_PSN.pdf)).

Examples of questions you can ask:
- _What is graph theory and how is a graph defined?_
- _What is meant by "network science"?_
- _What characterizes a "patient similarity network" and what can it be used for?_
- _Explain the difference between centrality measures such as degree, betweenness, and eigenvector centrality_

(Feel free to compare answers with responses from UiB-internal **https://chat.uib.no**)

---

## Slides

<a href="https://docs.google.com/presentation/d/e/2PACX-1vRvl54T7fBoOQaKCHOUcDDxuB4jDWyjw5tQMv3x5LYL7XVfB2hKGJZar1k3jrEUupYmQYOaMqyJ6MmF/pub?start=false&loop=false&delayms=3000"><img src="assets/Lab1-slide0.png"></a>

---

## Notebooks

All notebooks can be run in Google Colab or locally with the conda environment `bmed365-2026`.

### Main Notebooks

| Notebook | Description | Colab |
|:---------|:------------|:-----:|
| [00-introduction.ipynb](./notebooks/00-introduction.ipynb) | **Introduction to graph theory, network science, and PSN** – Basic concepts, graph types, adjacency matrices, centrality measures, and interactive learning module | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/00-introduction.ipynb) |
| [01-networkx_tutorial.ipynb](./notebooks/01-networkx_tutorial.ipynb) | **NetworkX tutorial** – Practical introduction to NetworkX: creating graphs, manipulating nodes/edges, using attributes, analyzing structures, and visualizing networks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/01-networkx_tutorial.ipynb) |
| [02-patient_similarity_network_iris.ipynb](./notebooks/02-patient_similarity_network_iris.ipynb) | **PSN with IRIS data** – Build your first similarity network with the classic IRIS dataset. Covers similarity calculation, visualization, network analysis, and community detection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/02-patient_similarity_network_iris.ipynb) |
| [03-patient_similarity_network_ibs_brain_cognition.ipynb](./notebooks/03-patient_similarity_network_ibs_brain_cognition.ipynb) | **PSN with clinical data (IBS)** – Application of PSN to real patient data: brain morphometry and cognition in irritable bowel syndrome, based on [Lundervold et al. (2025)](https://doi.org/10.3390/diagnostics15040470) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/03-patient_similarity_network_ibs_brain_cognition.ipynb) |
| [04-patient_similarity_network_IQ.ipynb](./notebooks/04-patient_similarity_network_IQ.ipynb) | **PSN based on IQ testing (WAIS-IV)** – Construct similarity networks from intelligence test data to identify cognitive profiles and subgroups | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/04-patient_similarity_network_IQ.ipynb) |

### Solution Notebooks

| Notebook | Description | Colab |
|:---------|:------------|:-----:|
| [02a-patient_similarity_network_iris_solutions.ipynb](./notebooks/02a-patient_similarity_network_iris_solutions.ipynb) | Solutions for exercises in notebook 02 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/02a-patient_similarity_network_iris_solutions.ipynb) |
| [02b-patient_similarity_network_iris_extended.ipynb](./notebooks/02b-patient_similarity_network_iris_extended.ipynb) | Extended version of IRIS PSN analysis with more advanced techniques | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/02b-patient_similarity_network_iris_extended.ipynb) |
| [04-patient_similarity_network_IQ_solutions.ipynb](./notebooks/04-patient_similarity_network_IQ_solutions.ipynb) | Solutions for exercises in notebook 04 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/notebooks/04-patient_similarity_network_IQ_solutions.ipynb) |

---

## Additional Resources: Graph Theory and Complex Networks

See also the [GraphTheory-and-ComplexNetworks](./GraphTheory-and-ComplexNetworks/README.md) folder for more in-depth notebooks on graph theory:

| Notebook | Topic | Colab |
|:---------|:------|:-----:|
| [1-Introduction.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/1-Introduction.ipynb) | Introduction to graphs and networks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/1-Introduction.ipynb) |
| [2-Fundamentals.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/2-Fundamentals.ipynb) | Fundamental graph theory | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/2-Fundamentals.ipynb) |
| [3-Extensions.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/3-Extensions.ipynb) | Extensions and special graph types | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/3-Extensions.ipynb) |
| [4-Network-topology.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/4-Network-topology.ipynb) | Network topology | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/4-Network-topology.ipynb) |
| [5-Network-analysis-centrality.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/5-Network-analysis-centrality.ipynb) | Centrality analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/5-Network-analysis-centrality.ipynb) |
| [6-Network-analysis-across-time.ipynb](./GraphTheory-and-ComplexNetworks/notebooks/6-Network-analysis-across-time.ipynb) | Dynamic network analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab1-NetworkSci-PSN/GraphTheory-and-ComplexNetworks/notebooks/6-Network-analysis-across-time.ipynb) |

---

## Other Resources

### Graph Theory and Network Science
- A. Lundervold & Medical AI Assistant: _Elements of graph theory and patient similarity networks (PSN) - A short introduction for ELMED219+BMED365_ [[PDF](./assets/ELMED219_BMED365_2024_PSN.pdf)] [[$\LaTeX$](https://www.overleaf.com/read/pccnktqbnswg#4f47e2)]

- **Khan Academy Graph Theory:** A beginner-friendly series on fundamental concepts and applications. [Khan Academy Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/describing-graphs)
    
- **Graph Theory Tutorials by Sarada Herke:** A YouTube playlist with visual and intuitive explanations of graph theory concepts. [Sarada Herke's graph theory tutorials](https://www.youtube.com/playlist?list=PLoJC20gNfC2gmT_5WgwYwGMvgCjYVsIQg)
    
- **Introduction to Graph Theory for Medical Students:** [Notes](https://docs.google.com/document/d/1Hy68-fjs1EJV3LL03qYusYydyXP7IAwsUnIYlaC9MdE/edit?usp=sharing) generated by Gemini Advanced 1.5 Pro with [Deep Research](https://blog.google/products/gemini/google-gemini-deep-research)

- **Barabási, A.-L.** (2016). *Network Science*. Cambridge University Press. [Free online](http://networksciencebook.com/)

### Jupyter Notebook
If Jupyter Notebook is new to you, these tutorials may be helpful:
* https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html
* https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook

---

## Your Turn!

Take time to experiment with the examples in the notebooks. You will find questions and exercises along the way that you can explore. If you are already familiar with graphs and networks, you can try more advanced examples – or even better, help others in the group who have less experience.

### Recommended Order:

1. **Start with `00-introduction.ipynb`** to get an overview of graph theory and the PSN concept
2. **Go through `01-networkx_tutorial.ipynb`** to learn the NetworkX tool
3. **Build your first PSN with `02-patient_similarity_network_iris.ipynb`**
4. **Apply the knowledge to clinical data** with notebook 03 or 04

Good luck! 🚀

