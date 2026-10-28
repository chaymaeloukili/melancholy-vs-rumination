# Notebooks

The analysis is split into four notebooks. Run them in this order.
Each notebook reads data from `../data/raw/` or `../data/processed/`. Raw data is never modified.

| Notebook | Step | Status |
|---|---|---|
| `01_explore.ipynb` | Explore: understand the raw data and select columns | done |
| `02_clean.ipynb` | Clean: combine samples, select columns, fix values | next |
| `03_analysis.ipynb` | Analysis: compare people who felt better and worse | open |
| `04_visualize.ipynb` | Visualize: final charts | open |

## 01_explore.ipynb
How I explored the raw data, step by step:
1. Load Sample 1 and take a first look
2. Main outcome in Sample 1: `MOODCHANGE`
3. Samples 2 and 3, comparison of all three
4. Which file is which sample? (documentation vs. data)
5. Overview of all 131 columns
6. Column index with meanings (from the label files)
7. The person columns
8. Missing values
9. Column selection
10. Summary, open questions and plan
11. My own contributions and AI usage
12. Outlook: from self-reports to the brain

Files from `data/raw/` used here:
- **Survey data** (`S1–S3_data.csv`): steps 1–4, 7, 8
- **Label files** (`*_label.csv`): step 6
- **Documentation** (`index.md`): steps 6–7
- **Known issues** (swapped samples, missing `REASON` labels, missing values): steps 4, 6, 8

## 02_clean.ipynb
Planned: combine S1–S3 with a `sample` column, keep the selected columns, convert checkbox `NaN` to `0`, rename abbreviated values, save to `data/processed/`.

## 03_analysis.ipynb and 04_visualize.ipynb
Planned. See the plan in `01_explore.ipynb`, step 10.