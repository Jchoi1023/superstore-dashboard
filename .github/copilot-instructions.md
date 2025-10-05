# Copilot Instructions for Supersote_Sales

## Project Overview
- This project appears to be a data analysis or data science project, centered around the `Superstore.csv` dataset.
- The main analysis and code are contained in the Jupyter notebook `SuperStore.ipynb`.

## Key Files
- `Superstore.csv`: Primary dataset. Contains sales or business data for analysis.
- `SuperStore.ipynb`: Main notebook for data exploration, analysis, and visualization.

## Developer Workflows
- **Data Analysis:** All code and analysis should be added to `SuperStore.ipynb` unless a new notebook is required for a distinct purpose.
- **Data Loading:** Use pandas to load the CSV: `pd.read_csv('Superstore.csv')`.
- **Visualization:** Use matplotlib, seaborn, or plotly for visualizations. Follow existing patterns in the notebook.
- **Environment:** Use Python 3.8+ with standard data science libraries (pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, etc.).

## Project Conventions
- Keep all exploratory code, data cleaning, and analysis steps in the notebook, with clear markdown explanations.
- Use English for all code comments and markdown cells.
- Do not modify the original `Superstore.csv` file; create derived datasets in-memory or as new files if needed.
- Place any new datasets or outputs in the project root unless a `data/` or `output/` directory is created.
- If adding new notebooks, use descriptive names and document their purpose at the top.

## Integration & Dependencies
- No external APIs or services are integrated by default.
- All dependencies should be installable via pip. If new packages are required, document them in a `requirements.txt` (if created).

## Examples
- To load the dataset:
  ```python
  import pandas as pd
  df = pd.read_csv('Superstore.csv')
  ```
- To add a new analysis section, use a markdown cell with a heading, followed by code cells.

## Additional Notes
- If you add new files or directories, update this instruction file to reflect new conventions or workflows.
- For large outputs or derived data, consider creating a `data/` or `output/` directory.

---

_If any conventions or workflows are unclear, please request clarification or propose updates to this file._
