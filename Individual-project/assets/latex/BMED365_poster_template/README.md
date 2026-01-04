# BMED365 LaTeX Poster Template

This directory contains a LaTeX template for creating scientific posters for the BMED365 Individual Project.

## Template Overview

- **Document class:** `tikzposter`
- **Dimensions:** 70cm × 120cm (portrait orientation)
- **Color scheme:** UiB/BMED365 institutional colors

## Files

| File | Description |
|------|-------------|
| `BMED365_poster_template.tex` | Main template file |
| `README.md` | This file |

## Requirements

### For local compilation

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

### Compilation

```bash
pdflatex BMED365_poster_template.tex
```

Or use `lualatex` for better font support:

```bash
lualatex BMED365_poster_template.tex
```

### Using Overleaf

1. Create a new project on [Overleaf](https://www.overleaf.com)
2. Upload `BMED365_poster_template.tex`
3. Compile automatically

The template is designed to compile without errors on Overleaf with default settings.

## Customization

### Title and Author

Edit the metadata section near the top of the file:

```latex
\title{Your Poster Title Here}
\author{Your Name}
\institute{Department of Biomedicine, University of Bergen}
```

### Adding Figures

Place your figure files in the same directory (or a `figures/` subdirectory) and include them:

```latex
\includegraphics[width=0.8\linewidth]{figures/your-figure.pdf}
```

**Tip:** Use PDF or PNG format for figures. PDF is preferred for diagrams and plots; PNG for photographs.

### Adding Equations

```latex
\begin{equation}
    y = f(x; \theta) = \sigma(W^{(L)} \cdots \sigma(W^{(1)} x + b^{(1)}) \cdots + b^{(L)})
\end{equation}
```

### Adding Code

```latex
\begin{lstlisting}[language=Python]
import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
\end{lstlisting}
```

### Adding Tables

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

### Color Customization

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

## Tips for a Good Poster

1. **Visual hierarchy:** Use clear headings and consistent formatting
2. **White space:** Don't overcrowd—aim for ~40% text, 40% figures, 20% space
3. **Readable fonts:** The template uses 25pt base size; don't go smaller than 20pt
4. **High-quality figures:** Use vector graphics (PDF) when possible
5. **Concise text:** A poster is not a paper—be brief and clear

## Troubleshooting

### "File not found" errors
- Ensure figure files are in the correct path
- Check for typos in filenames (LaTeX is case-sensitive on Linux)

### Compilation timeout on Overleaf
- Reduce image file sizes
- Use PDF instead of high-resolution PNG

### Package not found
- Install the missing package via your TeX distribution's package manager
- On Overleaf, packages are usually available automatically

## Support

- **Course questions:** Contact the course coordinator
- **LaTeX questions:** Post in the bmed365-channel on Discord

---

*BMED365: Computational Imaging, Modeling and AI in Biomedicine*  
*University of Bergen, Spring 2026*
