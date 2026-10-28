# Raw Data

These files are the original data and documentation. They are **never modified**.
All cleaning happens in `notebooks/02_clean.ipynb`, and results are saved in `data/processed/`.

## Source
Eerola, T. (2016). *Survey Data on Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences.*
Harvard Dataverse, V2. https://doi.org/10.7910/DVN/GLSIXB

Related study: Eerola, T. & Peltola, H.-R. (2016). Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences. *PLOS ONE*, 11(6), e0157444.
https://doi.org/10.1371/journal.pone.0157444

## License
CC0 1.0 (Public Domain)

## Downloaded
2026-10-28 from Harvard Dataverse, format: "Original File Format"

## Files

The files are grouped into four types.

### 1. Survey data (the answers)
Each file has the same 131 columns. One row = one person, one column = one question.

| File | Rows | Sample (documentation) | Sample (likely, my check) |
|---|---|---|---|
| `S1_data.csv` | 1,577 | Finland, convenience | Finland, convenience |
| `S2_data.csv` | 414 | UK, representative | Finland, quota |
| `S3_data.csv` | 445 | Finland, quota | UK, representative |

**Note:** The documentation and the paper do not match for S2 and S3. The paper reports UK n = 445 and Finnish quota n = 414.
In `S3_data.csv`, the columns `listen` and `expert` are 100% empty, and the paper reports no expertise data only for the UK sample.
So S2 and S3 are probably swapped in the documentation (not confirmed by the authors). See `notebooks/01_explore.ipynb`, step 4.

### 2. Label files (question texts)
The data columns only have short names (e.g. `FEELING27`). These files contain the full question texts.
One line = one item, line 1 = item 1. The files have no header row.

| File | Lines | Belongs to | Content |
|---|---|---|---|
| `ASM_label.csv` | 25 | `ASM1–ASM25` | Attitudes towards Sad Music (statements rated 1–7) |
| `REASON_label.csv` | 24 | `R1–R24` | general reasons for listening to sad music |
| `FEELING_label.csv` | 36 | `FEELING1–FEELING36` | feelings during the experience (e.g. sadness, comfort, nostalgia) |
| `PHYS_label.csv` | 5 | `PHYS1–PHYS5` | physical reactions (none, chills, cried a little, cried a lot, other) |
| `MEC_label.csv` | 10 | `MEC1–MEC10` | mechanisms that caused the emotion (e.g. memories, beauty) |
| `ESSENTIAL_label.csv` | 3 | `ESSENTIAL1–ESSENTIAL3` | how often people feel 1) grief/loss, 2) depression/gloom/sadness, 3) relief/comfort/joy |

**Note on `REASON_label.csv`:** The documentation says this file belongs to `REASON1–REASON13`, but it has 24 lines and fits `R1–R24`.
Labels for `REASON1–REASON13` are not included in the data release, so these columns are not used.

### 3. Documentation by the author
| File | Content |
|---|---|
| `index.md` | codebook: meaning and possible values of every column |
| `data_release_notes_of_Eerola_et_Peltola_2016.pdf` | data release notes (same content as `index.md`, as PDF) |

Note: the documentation differs from the data in some details (e.g. values are abbreviated in the data, such as `mult./d` or `MusicL`).

### 4. This README
`README.md` – my own description of the raw data: source, license, download date, files and known issues.

## Where these files are used
See `notebooks/README.md`.
