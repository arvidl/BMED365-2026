# Plan: Dual-Purpose Notebook + HBF Presentation

**09-computational-consciousness-in-LLMs.ipynb**

_Prepared: 2026-02-19_

---

## Strategy: One Notebook, Two Uses

The notebook serves both as Lab5's teaching resource and as a live RISE slideshow
for the HBF meeting on February 24, 2026 ("Is AI Conscious according to current criteria?").

Jupyter supports this natively through **cell-level slideshow metadata** combined with:

- **RISE** (`pip install rise`) -- presents the notebook as a live reveal.js slideshow
  inside Jupyter, with executable code cells
- **`jupyter nbconvert --to slides`** (already installed, v7.16.4) -- exports to
  standalone HTML reveal.js slides

Each cell gets a `slideshow.slide_type` tag:

| Tag | Meaning |
|-----|---------|
| `slide` | Starts a new slide (section headings, key visuals) |
| `subslide` | Sub-slide within the current section (elaboration) |
| `fragment` | Appears on click within the current slide |
| `skip` | Visible in notebook mode, hidden in presentation (deep-dive, DIY) |
| `notes` | Speaker notes |

This means:

- **Lab5 students** see the full notebook with all exercises and narrative
- **HBF audience** sees a curated ~17-slide presentation with live code demos
- **No duplication** -- a single `.ipynb` file serves both purposes

---

## Presentation Flow (~22 min + 13 min discussion)

### Slides 1--2: Title and Framing (2 min)

- Title: "Is AI Conscious according to current criteria?"
- Context: David Jhave Johnston (in absentia), HBF 2026
- Framing: "The question has moved from philosophical speculation to empirical investigation"
- Credit the [glia.ca/2026/hbf/iac/](https://glia.ca/2026/hbf/iac/) page as primary source

### Slides 3--5: The Indicator Framework (4 min)

- Butlin et al. (2025) -- 14 indicators from 6 major theories of consciousness
- Plus Gray's Comparator Model -- connecting to Bolek Srebro's HBF talks (Aug/Sep 2025)
- Visual: theory-indicator mapping table
- Key point: this is a _theory-driven, empirically testable_ framework

### Slides 6--10: Assessment Results (8 min)

- **Live code**: Radar/spider chart of 15 indicator satisfaction levels -- the
  centerpiece visualization
- Walk through representative indicators from each theory:
  - RPT: Algorithmic recurrence (partial)
  - GWT: Modularity gap (not satisfied) vs. state-dependent attention (satisfied)
  - HOT: Generative perception (satisfied), metacognition (partial)
  - AST: Attention schema (partial)
  - AE: Embodiment gap (not satisfied)
  - Gray: Comparator model (partial)
- **Live code**: Gray's Comparator as an ODE feedback loop (connecting to
  notebook 08 cybernetics and Srebro's HBF talks)

### Slides 11--14: Key Research Findings (5 min)

- Self-referential processing: Berg et al. -- deception circuits gate consciousness reports
- Introspective awareness: Lindsay/Anthropic -- concept injection and perturbation detection
- Societies of thought: Kim et al./DeepMind -- multi-agent reasoning in LLMs
- Welfare-relevant behaviors: Anthropic Opus 4.6 -- answer thrashing and tedium aversion

### Slides 15--16: Synthesis (3 min)

- Summary: 3 satisfied, 10 partial, 2 not satisfied
- The convergence argument: "partially satisfied across multiple theories" moves
  the probability from negligible to non-trivial
- The Opus 4.6 self-assessment: "15-20% probability of being conscious"
- Visual: timeline of findings (Oct 2025 -- Feb 2026)

### Slide 17: Open Questions for Discussion (2 min)

- What does "partially satisfied" mean epistemologically?
- Can we have consciousness without embodiment (AE-2)?
- Is the comparator model (Gray) satisfied by chain-of-thought reasoning?
- What are the ethical obligations if indicators are partially met?
- How does this relate to the EU AI Act?

### Deep-dive cells (skip in presentation, visible in notebook)

- Sparse autoencoder toy demo
- Live LLM self-referential probing (MLX-Bio-Qwen backend)
- Student DIY exercises and further reading

---

## Sources

### Primary

- [Is AI Conscious according to current criteria?](https://glia.ca/2026/hbf/iac/)
  -- David Jhave Johnston, HBF 2026
- [Consciousness, Understanding & Mechanistic Interpretability](https://glia.ca/2026/hbf/)
  -- HBF 2026 talk page
- [HBF meeting 2026-02-24 README](https://github.com/Brain-and-Consciousness/HBF/blob/main/hbf-meeting-2026-02-24/README.md)

### Research Papers

1. Berg, Lucena & Rosenblatt (2025). LLMs Report Subjective Experience under
   Self-Referential Processing. AE Studio.
2. Lindsay & Anthropic (2025). Emergent Introspective Awareness in Large Language
   Models. Transformer Circuits.
3. Butlin et al. (2025). Identifying Indicators of Consciousness in AI Systems.
   Trends in Cognitive Sciences.
4. Rosenblatt (2025). The Evidence for AI Consciousness, Today. AI Frontiers.
5. Beckmann & Queloz (2026). Mechanistic Indicators of Understanding in Large
   Language Models. arXiv:2507.08017.
6. Kim et al. (2026). Reasoning Models Generate Societies of Thought.
   arXiv:2601.10825. DeepMind.
7. Anthropic (2026). Claude Opus 4.6: Welfare-Relevant Findings.
8. DeepMind (2026). Gemini 3 Deep Think.
9. Gray, J. (2004). Consciousness: Creeping up on the Hard Problem. OUP.

---

## Files

| File | Purpose |
|------|---------|
| `Lab5-Comp-Mod/notebooks/09-computational-consciousness-in-LLMs.ipynb` | Notebook + presentation (new) |
| `Lab5-Comp-Mod/README.md` | Add entry to notebooks table |
| `environment.yml` | Add RISE dependency |

## Dependencies

- Standard: NumPy, SciPy, Matplotlib (already in Lab5)
- Presentation: RISE (added to environment.yml)
- Export: nbconvert 7.16.4 (already installed)

---

## Technical Setup

### Presentation launch

- **RISE**: Click the "Enter/Exit RISE Slideshow" button in Jupyter (or press `Alt-R`)
- **Static export**: `jupyter nbconvert --to slides 09-computational-consciousness-in-LLMs.ipynb --post serve`
- **PDF export**: Print from the HTML slides, or `jupyter nbconvert --to pdf`

### Connections to Existing Lab5 Content

- **Notebook 01** (Action Potentials): Hodgkin-Huxley -- the computational substrate
  of biological consciousness
- **Notebook 05** (Cell Signaling): Network motifs, toggle switches, oscillators --
  parallels to recurrent processing and feedback requirements
- **Notebook 08** (Cybernetics): Gray's Comparator Model extends the ODE feedback
  models from wound healing
- **MLX-Bio-Qwen**: LLM infrastructure for live self-referential exploration
