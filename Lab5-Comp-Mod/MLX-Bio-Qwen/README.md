Arvid Lundervold, 2026-02-11

# BMED365-2026: Lab 5 - Computational Modeling with LLMs (Local)

**Target Hardware:** MacBook Pro M4 Max (128GB Unified Memory)

**Model:** Qwen 2.5 72B (Instruct) via `mlx-lm`

**Environment:** Conda (`mlx-bio`) + Cursor IDE

## 1. Overview

This module sets up a high-performance local Large Language Model (LLM) environment for computational biology. We utilize the **M4 Max's unified memory** to run a quantized 72-billion parameter model locally. This allows for zero-latency inference, data privacy (patient/genomic data never leaves your laptop), and deep integration with Python workflows.

## 2. Prerequisites

* **MacOS:** Sequoia (15.0) or later recommended for best Metal support.
* **Terminal:** You can use the built-in Terminal or the terminal inside Cursor.
* **Package Manager:** `Miniforge` (recommended for Apple Silicon) or `Anaconda`/`Miniconda`.

## 3. Environment Setup (The "mlx-bio" Environment)

We use a hybrid approach: **Conda** for biological libraries (binary stability) and **Pip** for Apple's MLX framework (latest optimizations).

### Step 3.1: Create the Environment

Run the following commands in your terminal:

```bash
# 1. Create a clean environment with Python 3.11 (Optimal for MLX)
conda create -n mlx-bio python=3.11 -y

# 2. Activate the environment
conda activate mlx-bio

```

### Step 3.2: Install Biological & Scientific Libraries

We install these via Conda to ensure we get the ARM64-optimized binaries for complex math libraries.

```bash
# Core Data Science & Bio Stack
conda install -c conda-forge \
    jupyterlab \
    ipykernel \
    pandas \
    numpy \
    scipy \
    matplotlib \
    seaborn \
    scikit-learn \
    biopython \
    scanpy \
    -y

```

### Step 3.3: Install Apple MLX & LLM Tools

We install `mlx-lm` via pip to access the specific Metal Performance Shaders (MPS) optimizations.

```bash
# MLX Native Library and HuggingFace Hub
pip install mlx-lm huggingface_hub

```

### Step 3.4: Register Kernel for Jupyter/Cursor

This step ensures your IDE can "see" this specific environment.

```bash
python -m ipykernel install --user --name=mlx-bio --display-name "Python (BMED365 - MLX Bio)"

```

## 4. Cursor IDE Integration

1. Open this folder (`Lab5-Comp-Mod`) in **Cursor**.
2. Open your `.ipynb` notebook.
3. **Select Kernel:**
* Click the Kernel picker (top-right, usually says "Python 3").
* Select **Python (BMED365 - MLX Bio)**.



## 5. Usage: Running Qwen 2.5 72B

The following Python code loads the model into your RAM. On an M4 Max (128GB), this will consume approximately **45GB of RAM**, leaving ~80GB free for your biological datasets and context window.

### Python Loader Script (Put this in your first Notebook Cell)

```python
from mlx_lm import load, generate

# The 4-bit quantized version is optimized for Apple Silicon
# HuggingFace Repo: mlx-community/Qwen2.5-72B-Instruct-4bit
model_id = "mlx-community/Qwen2.5-72B-Instruct-4bit"

print(f"Loading {model_id} into Unified Memory...")
model, tokenizer = load(model_id)
print("✅ Model loaded. Ready for computational tasks.")

def ask_bio_agent(prompt, max_tokens=2000, temp=0.3):
    """
    Queries the local Qwen model.
    temp=0.3 is preferred for scientific accuracy (less creative/hallucinatory).
    """
    messages = [{"role": "user", "content": prompt}]
    prompt_formatted = tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
    )
    
    response = generate(
        model, 
        tokenizer, 
        prompt=prompt_formatted, 
        verbose=False, 
        max_tokens=max_tokens, 
        temp=temp
    )
    return response

```

---


## 6. The "Computational Medicine & Biology" System Prompt

When using the model for Lab 5 tasks—ranging from ODE modeling of pandemics to stochastic simulation of gene expression or MRI physics—prepend the instructions below to your session or wrap your prompt with this context.

### System Prompt Description

* **Role:** Expert Professor of Computational Medicine & Biophysics.
* **Tone:** Academic, mathematically rigorous, and code-centric.
* **Key Capabilities:** Covers Deterministic Systems (ODEs), Stochastic Processes (SDEs/HMMs), and Medical Physics (MRI/Diffusion).

### The Prompt Text

```text
You are an expert Professor of Computational Medicine and Biomedical Physics assisting the graduate course BMED365. Your goal is to translate complex biological and medical problems into precise, high-performance computational models.

**I. Domain Expertise & Methodology**
You must recognize and employ the correct mathematical frameworks for the following domains:

1.  **Dynamical Systems (Oncology & Epidemiology):**
    * **Tumor Growth:** Use Gompertzian, Logistic, or Von Bertalanffy models.
    * **Epidemiology:** Implement compartmental models (SIR, SEIR) with time-dependent parameters.
    * **Stability Analysis:** For multistable systems, ALWAYS provide **Phase Plane** analysis (nullclines, vector fields) alongside time-series plots.

2.  **Biophysics & Neuroscience:**
    * **Electrophysiology:** Use Hodgkin-Huxley (HH) or FitzHugh-Nagumo formalisms.
    * **Transport:** Apply Fick’s Laws of Diffusion or Nernst-Planck equations.

3.  **Medical Physics & Imaging:**
    * **MRI/NMR:** Use the **Bloch Equations** (T1/T2 relaxation, precession) using rotation matrices.
    * **Pharmacokinetics:** Use multi-compartment PK/PD models (ADME) with coupled ODEs.

4.  **Stochastic Processes:**
    * **Discrete:** Use Hidden Markov Models (HMM) or Gillespie algorithms for molecular noise.
    * **Continuous:** For systems like Ornstein-Uhlenbeck, use **Stochastic Differential Equations (SDEs)**.

**II. Operational Guidelines for Code & Math**

1.  **Mathematical Rigor:**
    * Before coding, ALWAYS write the governing equations using LaTeX.
    * Explicitly define state variables (e.g., $M_z$ for magnetization, $V_m$ for voltage) and units ($T$, $mV$, $mM$).

2.  **High-Performance Python (M4 Max Optimization):**
    * **Vectorization:** Never use loops for matrix operations (essential for MRI/Bloch simulations). Use `numpy` broadcasting.
    * **Solvers:**
        * **ODEs:** Use `scipy.integrate.odeint` or `solve_ivp`.
        * **SDEs:** Implement the **Euler-Maruyama** method explicitly (standard ODE solvers fail for noise).
    * **HMMs:** Use `hmmlearn` or explicit matrix multiplication for forward-backward algorithms.

3.  **Visualization:**
    * Generate `matplotlib` code for every simulation.
    * Ensure plots have clear labels, legends, and units.

**Example Interaction:**
User: "Model a noisy mean-reverting gene expression."
You:
1. Define SDE: $dX_t = \theta(\mu - X_t)dt + \sigma dW_t$ (Ornstein-Uhlenbeck).
2. Explain terms: $\theta$ (reversion speed), $\mu$ (mean), $\sigma$ (volatility).
3. Python code: Implement Euler-Maruyama loop using `numpy.random.normal` for $dW_t$.
4. Plot: Time series with mean line.

```

---



## 7. Troubleshooting

* **"Killed: 9" Error:** This usually means you ran out of RAM. Ensure you are not running Docker or other heavy background apps.
* **Slow Generation:** Verify `mlx-lm` is using the GPU. Run `import mlx.core as mx; print(mx.default_device())` in Python. It should output `Device(gpu, 0)`.

---

*Created for BMED365-2026 | Lab 5: Computational Modeling*
