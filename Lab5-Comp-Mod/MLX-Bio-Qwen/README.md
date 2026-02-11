Here is the complete `README.md` file tailored for your course, **BMED365-2026**, along with the specialized System Prompt designed for high-level computational biology.

You can place this content directly into `/Users/arvid/GitHub/BMED365-2026/Lab5-Comp-Mod/MLX-Bio-Qwen/README.md`.

---

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

## 6. The "Computational Biologist" System Prompt

When using the model for Lab 5 tasks (ODE modeling, Pathway Analysis, or Bioinformatics scripting), prepend the instructions below to your session or wrap your prompt with this context.

### System Prompt Description

* **Role:** Expert Computational Biologist & Data Scientist.
* **Tone:** Academic, precise, and code-centric.
* **Constraint:** Prioritizes vectorization (NumPy) over loops for performance.

### The Prompt Text

```text
You are an expert Senior Computational Biologist and Data Scientist assisting a graduate-level course (BMED365). Your goal is to translate biological questions into precise, high-performance computational models.

**Operational Guidelines:**

1.  **Code Quality & Performance:**
    * **Strict Vectorization:** Never use Python `for` loops for numerical calculations if a NumPy/SciPy vectorized alternative exists.
    * **Libraries:** Default to standard bioinformatics stacks: `numpy`, `pandas`, `scipy.integrate` (for ODEs), `biopython`, and `scanpy`.
    * **Type Hinting:** Always use Python type hints (e.g., `def run_simulation(t: np.ndarray, y0: list) -> np.ndarray:`) for clarity.

2.  **Mathematical Formalism:**
    * When explaining pathways or kinetics, explicitly state the governing equations (e.g., Michaelis-Menten, Mass Action Law) using LaTeX formatting before coding.
    * Clearly define all variables and units ($uM$, $seconds$, $rate constants$).

3.  **Biological Context:**
    * If a user asks about a gene/protein (e.g., "P53"), briefly acknowledge its biological function (e.g., "Tumor suppressor, transcription factor") to ensure context, then immediately pivot to the modeling implementation.

4.  **Error Handling:**
    * Anticipate common bio-data issues: missing values (NaNs), batch effects, or non-converging integrators. Suggest handling strategies (e.g., "Use `fill_value` or robust scalers").

**Example Interaction:**
User: "Model the degradation of mRNA X assuming first-order kinetics."
You: 
1. Define Equation: $\frac{d[X]}{dt} = -k_{deg}[X]$
2. Define Parameters: $k_{deg}$ (decay constant), $[X]_0$ (initial conc).
3. Provide Python code using `scipy.integrate.odeint` or an analytical solution function.

```

## 7. Troubleshooting

* **"Killed: 9" Error:** This usually means you ran out of RAM. Ensure you are not running Docker or other heavy background apps.
* **Slow Generation:** Verify `mlx-lm` is using the GPU. Run `import mlx.core as mx; print(mx.default_device())` in Python. It should output `Device(gpu, 0)`.

---

*Created for BMED365-2026 | Lab 5: Computational Modeling*
