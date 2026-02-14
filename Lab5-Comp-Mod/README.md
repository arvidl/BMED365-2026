# Lab 5: Computational modeling

This lab is part of our journey through computational modeling techniques, and the use of AI in biomedical applications. It is designed to give you a comprehensive understanding of how computational modelinhg is transforming society in general and biomedicine in particular and the role it will play in the future of biomedical research.<br>  

Arvid Lundervold, 2026-02-11 


<!-- ![img](../assets/GPT-MedAI.png)<br> -->
<img src="../assets/GPT-MedAI.png" width="600"><br>
If you have a subscription to [ChatGPT Plus](https://openai.com/blog/chatgpt-plus), you can also try out the the [**Medical AI Assistant (UiBmed - ELMED219 & BMED365)**](https://chat.openai.com/g/g-d90dfN17H-medical-ai-assistant-uibmed-elmed219-bmed365) [GPT](https://openai.com/blog/introducing-gpts) and see if you can get it to answer some of your questions.

---------------

## Slides modeling

<a href="https://docs.google.com/presentation/d/e/2PACX-1vTM1NY3r8nyZgdfhkJgsdTZDpANGwPscmXWB49cw5SHZgS20MsI6abjUzog0Ez6h_RR3e6F5qadZutD/pub?start=false&loop=false&delayms=3000"><img src="../assets/Lab5-slide-0.png"></a>


<!--
<img src="assets/Lab3-slide-0.png">
-->

------
## Notebooks

| Notebook    |      1-Click Notebook      |
|:----------|------|
|  [00-test-llm.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/00-test-llm.ipynb)<br> We test and explore a laptop installation of the powerful [**DeepSeek-R1**](https://arxiv.org/html/2501.12948v1) reasoning model <br> - the distilled _deepseek-r1:1.5b_, ..., _deepseek-r1:70b_ models)   | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/00-test-llm.ipynb)|
|  [01-action-potentials.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/01-action-potentials.ipynb)<br> We explore the Hodgkin and Huxley model (HH-model) of action potentials | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/01-action-potentials.ipynb)|
|  [02-tumor-growth.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/02-tumor-growth.ipynb)<br> We explore a tumor growth and angiogenesis model | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/02-tumor-growth.ipynb)|
|  [03-cardiovascular-flow.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/03-cardiovascular-flow.ipynb)<br> We explore a cardiovascular flow model with added ECG and blood pressure waveforms | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/03-cardiovascular-flow.ipynb)|
|  [04-muscle-force.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/04-muscle-force.ipynb)<br> We explore a muscle force generation model (WIP)| [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/04-muscle-force.ipynb)|
|  [05-cell-signaling.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/05-cell-signaling.ipynb)<br> We explore a cell signaling model and gene regulatory networks | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/05-cell-signaling.ipynb)|
|  [06-kidney-filtration.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/06-kidney-filtration.ipynb)<br> We explore a kidney filtration model by prompting a LLM to generate a model | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/06-kidney-filtration.ipynb)|
|  [07-cybernetics-of-wound-healing.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/07-cybernetics-of-wound-healing.ipynb)<br> We explore wound healing as a feedback control system with dynamical population models | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/notebooks/07-cybernetics-of-wound-healing.ipynb)|


---

## MLX-Bio-Qwen: LLM-Assisted Computational Modeling on Apple Silicon

The [`MLX-Bio-Qwen/`](MLX-Bio-Qwen/) subfolder contains notebooks that use **Large Language Models** as a "Senior Computational Colleague" for formulating and implementing computational models. The notebooks support **two backends** that are auto-detected at runtime:

| Platform | Backend | Model | Setup |
|:---|:---|:---|:---|
| **Apple Silicon** (M1–M4) | [MLX](https://github.com/ml-explore/mlx) (local) | [Qwen 2.5 72B Instruct](https://huggingface.co/mlx-community/Qwen2.5-72B-Instruct-4bit) | `mlx-bio` Conda env |
| **Google Colab** (free tier) | [`google.colab.ai`](https://medium.com/google-colab/all-colab-users-now-get-access-to-gemini-and-gemma-models-via-colab-python-library-at-no-cost-a392599977c4) | Gemini 2.5 Flash | No API key, no billing — zero config |

On Apple Silicon the full 72B-parameter model runs locally. On Colab, the notebook seamlessly falls back to Google's free Gemini API — all features (personas, controls, conversation history, LaTeX post-processing) work identically on both backends. Standard Python code (NumPy, SciPy, Matplotlib) always runs regardless of backend.

| Notebook    |      1-Click Notebook      |
|:----------|------|
|  [01-compmod-intro.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/MLX-Bio-Qwen/notebooks/01-compmod-intro.ipynb)<br> Introduction to computational neuroscience & medical physics — FitzHugh-Nagumo model, Hodgkin-Huxley model, Ornstein-Uhlenbeck membrane noise, and MRI Bloch equations | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/MLX-Bio-Qwen/notebooks/01-compmod-intro.ipynb)|
|  [02-compmod-Q-and-A.ipynb](https://nbviewer.jupyter.org/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/MLX-Bio-Qwen/notebooks/02-compmod-Q-and-A.ipynb)<br> Interactive Q&A interface with ipywidgets GUI, multiple expert personas, temperature/max-token controls, conversation history, and LaTeX rendering. **Two backends:** locally via Qwen 2.5 72B on Apple Silicon, or via **Gemini 2.5 Flash** on Google Colab (free tier — no API key, no billing setup; monthly usage limits apply per [Google's free tier policy](https://ai.google.dev/gemini-api/docs/pricing)) | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/BMED365-2026/blob/main/Lab5-Comp-Mod/MLX-Bio-Qwen/notebooks/02-compmod-Q-and-A.ipynb)|


---


## Your turn!

Spend some time playing around with the provided examples. You'll find some questions for you to investigate in the notebooks. If you're already familiar with this level of computational modeling you can try your hand at more advanced examples, or, even better, help out other less experienced team members.


