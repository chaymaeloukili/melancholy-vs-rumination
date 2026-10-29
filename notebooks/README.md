# Notebooks

The analysis is split into four notebooks. Run them in this order.
Each notebook reads data from `../data/raw/` or `../data/processed/`. Raw data is never modified.

| Notebook | Step | Status |
|---|---|---|
| `01_explore.ipynb` | Explore: understand the raw data and select columns | done |
| `02_clean.ipynb` | Clean: combine samples, remove columns, fix values, save clean data | done |
| `03_analysis.ipynb` | Analysis: compare people who felt better and worse | next |
| `04_visualize.ipynb` | Visualize: final charts | open |

**How these notebooks were made:** The approach, the steps and all decisions about the data are my own. Claude (Anthropic) supports me like a tutor: it writes most of the code based on my instructions, explains it, and helps me structure and document each notebook. I run every step and check every result myself. Details: [AI_USAGE.md](../AI_USAGE.md)

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

Uses: `data/raw/` – survey data, label files and `index.md`.

## 02_clean.ipynb
How I cleaned the data, step by step:
0. Setup
1. Load the three samples
2. Add a `sample` column
3. Create a unique `id`
4. Compare the answer values across samples
5. Combine the three samples
6. Remove columns (`expert`, `listen`, `REASON1–13`)
7. Checkbox columns: `NaN` → `0`
8. Check the scales (1–7)
9. Combine age groups (`65 or older`)
10. Set the order of categories
11. Document missing values
12. Reorder columns and save
13. Reload and check the saved file
14. Summary

Uses: `data/raw/S1–S3_data.csv` → creates `data/processed/sad_music_clean.csv`.

## 03_analysis.ipynb
Next: load `data/processed/sad_music_clean.csv`, set the order of categories again (`category_order` from `02_clean`), and compare people who felt better and worse.

## 04_visualize.ipynb
Planned: the final charts (see the chart plan in `01_explore.ipynb`, step 10).
