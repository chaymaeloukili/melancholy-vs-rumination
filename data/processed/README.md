# Processed Data

This folder contains data that was cleaned with Python. The original files are in `data/raw/` and are never modified.

## sad_music_clean.csv

Created by `notebooks/02_clean.ipynb` from `S1_data.csv`, `S2_data.csv` and `S3_data.csv` (Eerola, 2016, CC0).

- **Rows:** 2,436 (one row = one person)
- **Columns:** 118

### Changes compared to the raw data
| Change | Why |
|---|---|
| Combined S1, S2 and S3 into one table | same cleaning steps for all samples |
| New column `sample`: `S1_Finland_convenience`, `S2_Finland_quota`, `S3_UK_representative` | to keep the samples apart (S2/S3 labels based on my check, see `01_explore.ipynb`) |
| New column `id` (e.g. `S1_1`) | `subj` starts at 1 in every file |
| Removed `expert`, `listen` | 100% missing in S3 |
| Removed `REASON1–REASON13` | no labels in the data release |
| Checkbox columns (`R`, `FEELING`, `PHYS`, `MEC`): `NaN` → `0` | `NaN` meant "not ticked"; now 1 = ticked, 0 = not ticked |
| `age`: `65 to 74` and `75 or older` → `65 or older` | `75 or older` only in S3 and only 2 people |

### Notes for using this file
- **Missing values** in `MOODCHANGE`, `PHYSCHANGE` and `INTENSITY` are kept as empty cells. Always report how many people answered (`n`).
- **Order of categories** (e.g. Worse → Same → Better) is not stored in a CSV file. Set it again after loading (see `category_order` in `02_clean.ipynb`).
- **Samples should be analysed separately**, because they differ in country, recruitment and size.
- Meanings of all columns: see `notebooks/01_explore.ipynb` (step 6) and the label files in `data/raw/`.