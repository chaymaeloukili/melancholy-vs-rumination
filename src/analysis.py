"""Analysis: all tables and tests from notebooks/03_analysis.ipynb, saved as CSV files.

The notebook shows my thinking and my notes. This script only repeats the calculations.
Run from the project folder (after clean.py):  python src/analysis.py
Result: CSV tables in results/
"""

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

from config import CATEGORY_ORDER, CLEAN_FILE, P_LIMIT, RAW_DIR, RESULTS_DIR, SAMPLE_NAMES


# ---------- Loading ----------

def load_data():
    """Load the clean table and set the order of the categories again (lost in the CSV)."""
    df = pd.read_csv(CLEAN_FILE)
    for col, order in CATEGORY_ORDER.items():
        df[col] = pd.Categorical(df[col], categories=order, ordered=True)
    return df


def load_items(df, prefix, label_file):
    """Columns of one question block (e.g. FEELING1-36) and their labels from the label file.

    c[len(prefix):].isdigit() keeps only columns where a number follows the prefix,
    so PHYSCHANGE is not taken for PHYS, and R1-R24 are found with the prefix R.
    """
    cols = [c for c in df.columns if c.startswith(prefix) and c[len(prefix):].isdigit()]
    labels = pd.read_csv(RAW_DIR / label_file, header=None)[0].tolist()
    assert len(cols) == len(labels), f"{prefix}: {len(cols)} columns but {len(labels)} labels"
    return cols, labels


def save(table, name):
    """Save a table as CSV in results/."""
    table.to_csv(RESULTS_DIR / f"{name}.csv")


# ---------- Tables ----------

def pct(table):
    """Turn a table of counts into percentages, rounded to 1 decimal."""
    return (table * 100).round(1)


def mood_by(df, column):
    """Mood change by a column (e.g. DURATION), per sample: row percentages plus group size n."""
    table = pct(pd.crosstab([df["sample"], df[column]], df["MOODCHANGE"], normalize="index"))
    table["n"] = pd.crosstab([df["sample"], df[column]], df["MOODCHANGE"]).sum(axis=1)
    return table


def items_by_mood(df, cols, labels):
    """Share of people (%) who ticked each item, per sample and mood change.

    The code (e.g. FEELING4) and its label (e.g. sadness) are both kept in the row names.
    """
    table = pct(df.groupby(["sample", "MOODCHANGE"], observed=True)[cols].mean()).T
    table.index = pd.MultiIndex.from_arrays([cols, labels], names=["code", "label"])
    return table


def better_minus_worse(table):
    """Difference Better minus Worse for each sample (percentage points or scale points)."""
    better = table.xs("Better", axis=1, level="MOODCHANGE")
    worse = table.xs("Worse", axis=1, level="MOODCHANGE")
    return (better - worse).round(2)


def intensity_pleasure(df):
    """Mean intensity and pleasure (1-7) and number of answers, per sample and mood change."""
    return (df.groupby(["sample", "MOODCHANGE"], observed=True)[["INTENSITY", "PLEASURE"]]
              .agg(["mean", "count"]).round(2))


# ---------- Data quality check (step 7b) ----------

def pattern_similarity(df, cols):
    """How similar is the whole correlation pattern of a question block between the samples?

    Close to 1 = same pattern, close to 0 = the answers do not fit together the same way.
    """
    n = len(cols)
    mask = np.triu(np.ones((n, n)), k=1).astype(bool)   # each pair of items only once
    pairs = {s: df[df["sample"] == s][cols].corr().values[mask] for s in SAMPLE_NAMES}
    s1, s2, s3 = SAMPLE_NAMES
    return {"S1 vs S2": round(np.corrcoef(pairs[s1], pairs[s2])[0, 1], 2),
            "S1 vs S3": round(np.corrcoef(pairs[s1], pairs[s3])[0, 1], 2)}


# ---------- Statistical tests ----------

def cramers_v(table, chi2):
    """Effect size from 0 (no link) to 1 (perfect link)."""
    return (chi2 / (table.values.sum() * (min(table.shape) - 1))) ** 0.5


def chi_situation(df, columns):
    """Chi-square test of mood change vs. each situation column, per sample (p and Cramér's V)."""
    rows = []
    for column in columns:
        for s in SAMPLE_NAMES:
            sub = df[df["sample"] == s]
            table = pd.crosstab(sub[column], sub["MOODCHANGE"])
            chi2, p, dof, expected = chi2_contingency(table)
            rows.append({"question": column, "sample": s, "p": p, "V": round(cramers_v(table, chi2), 2)})
    return pd.DataFrame(rows)


def chi_items(df, cols, labels):
    """Cramér's V for each 0/1 item vs. mood change, per sample. Empty = not significant (p >= P_LIMIT)."""
    result = pd.DataFrame({"label": labels}, index=cols)
    for s in SAMPLE_NAMES:
        sub = df[df["sample"] == s]
        values = []
        for col in cols:
            table = pd.crosstab(sub[col], sub["MOODCHANGE"])
            if min(table.shape) < 2:   # item never ticked in this sample -> no test possible
                values.append(None)
                continue
            chi2, p, dof, expected = chi2_contingency(table)
            values.append(round(cramers_v(table, chi2), 2) if p < P_LIMIT else None)
        result[s] = values
    return result


# ---------- Run everything ----------

def main():
    df = load_data()
    RESULTS_DIR.mkdir(exist_ok=True)

    # Question blocks with their labels
    feelings = load_items(df, "FEELING", "FEELING_label.csv")
    reasons = load_items(df, "R", "REASON_label.csv")
    phys = load_items(df, "PHYS", "PHYS_label.csv")
    mec = load_items(df, "MEC", "MEC_label.csv")
    asm_cols, asm_labels = load_items(df, "ASM", "ASM_label.csv")
    asm_labels = [label.split(" ", 1)[1] for label in asm_labels]   # remove the code before the first space

    # Steps 2-3: who feels better, and who are the people in each sample
    save(pct(pd.crosstab(df["MOODCHANGE"], df["sample"], normalize="columns")), "02_moodchange_by_sample")
    save(pd.crosstab(df["MOODCHANGE"], df["sample"], margins=True), "02_moodchange_by_sample_n")
    for col in ["age", "gender", "listensad"]:
        save(pct(pd.crosstab(df[col], df["sample"], normalize="columns")), f"03_{col}_by_sample")

    # Step 4 and 8a: mood change by listening frequency and by the situation
    for col in ["age", "listensad", "CHOICE", "FAM", "IMPORTANCE", "DURATION", "AGO"]:
        save(mood_by(df, col), f"04_mood_by_{col}")

    # Steps 5, 6, 8b: feelings, reasons, physical reactions, mechanisms (0/1 items)
    for name, (cols, labels) in [("feelings", feelings), ("reasons", reasons),
                                 ("physical", phys), ("mechanisms", mec)]:
        table = items_by_mood(df, cols, labels)
        save(table, f"05_{name}_by_mood")
        save(better_minus_worse(table), f"05_{name}_better_minus_worse")
    save(pct(df.groupby("sample")[reasons[0]].mean()).T, "06_reasons_by_sample")

    # Step 7: attitudes (scale 1-7). UK (S3) answers are not reliable, see step 7b.
    asm = df.groupby(["sample", "MOODCHANGE"], observed=True)[asm_cols].mean().round(2).T
    asm.index = pd.MultiIndex.from_arrays([asm_cols, asm_labels], names=["code", "label"])
    save(asm, "07_attitudes_by_mood")
    save(better_minus_worse(asm), "07_attitudes_better_minus_worse")

    # Step 7b: data quality check
    quality = {name: pattern_similarity(df, cols) for name, cols in
               [("attitudes (ASM)", asm_cols), ("reasons", reasons[0]), ("feelings", feelings[0])]}
    save(pd.DataFrame(quality).T, "07b_pattern_similarity")

    # Step 8c: intensity and pleasure
    save(intensity_pleasure(df), "08c_intensity_pleasure")

    # Step 9: statistical tests
    table = pd.crosstab(df["MOODCHANGE"], df["sample"])
    chi2, p, dof, expected = chi2_contingency(table)
    print(f"Test 1, mood change between samples: chi2 = {chi2:.1f}, df = {dof}, p = {p:.3g}")

    situation = chi_situation(df, ["CHOICE", "FAM", "IMPORTANCE", "DURATION", "AGO"])
    save(situation, "09_test_situation")
    for name, (cols, labels) in [("physical", phys), ("mechanisms", mec),
                                 ("feelings", feelings), ("reasons", reasons)]:
        save(chi_items(df, cols, labels), f"09_test_{name}")

    print("Data quality (similarity of the answer pattern):")
    print(pd.DataFrame(quality).T.to_string())
    print(f"Done. {len(list(RESULTS_DIR.glob('*.csv')))} tables saved in {RESULTS_DIR.name}/")


if __name__ == "__main__":
    main()
