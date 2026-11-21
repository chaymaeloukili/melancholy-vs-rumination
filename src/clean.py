"""Cleaning: turns the three raw samples into one clean table.

Same steps as notebooks/02_clean.ipynb, without the exploring.
Run from the project folder:  python src/clean.py
Result: data/processed/sad_music_clean.csv
"""

import pandas as pd

from config import CATEGORY_ORDER, CLEAN_FILE, PROCESSED_DIR, RAW_DIR, SAMPLES


def load_samples():
    """Load S1, S2, S3, add a sample column and a unique id, then combine them into one table."""
    tables = []
    for file, (short, name) in SAMPLES.items():
        sample = pd.read_csv(RAW_DIR / file).copy()
        sample["sample"] = name
        sample["id"] = short + "_" + sample["subj"].astype(str)   # subj starts at 1 in every file
        tables.append(sample)
    return pd.concat(tables, ignore_index=True)


def drop_columns(df):
    """Remove expert and listen (100 % missing in S3) and REASON1-13 (no labels)."""
    reason_cols = [c for c in df.columns if c.startswith("REASON")]
    return df.drop(columns=["expert", "listen"] + reason_cols)


def checkbox_columns(df):
    """All checkbox columns (R, FEELING, PHYS, MEC), without PHYSCHANGE, which is not a checkbox."""
    cols = [c for c in df.columns if c.startswith(("R", "FEELING", "PHYS", "MEC"))]
    cols.remove("PHYSCHANGE")
    return cols


def fix_checkboxes(df):
    """In checkbox columns NaN means 'not ticked', so NaN -> 0. Then 1 = ticked, 0 = not ticked."""
    cols = checkbox_columns(df)
    df[cols] = df[cols].fillna(0).astype(int)
    return df


def check_scales(df):
    """ASM1-25, INTENSITY and PLEASURE may only have values from 1 to 7. Stops with an error if not."""
    scale_cols = [c for c in df.columns if c.startswith("ASM")] + ["INTENSITY", "PLEASURE"]
    assert df[scale_cols].min().min() >= 1, "a scale value is below 1"
    assert df[scale_cols].max().max() <= 7, "a scale value is above 7"


def combine_age(df):
    """75 or older only exists in S3 (2 people), so 65 to 74 and 75 or older become 65 or older."""
    df["age"] = df["age"].replace({"65 to 74": "65 or older", "75 or older": "65 or older"})
    return df


def check_categories(df):
    """Every answer must fit into its list in CATEGORY_ORDER, otherwise it would become NaN later."""
    for col, order in CATEGORY_ORDER.items():
        unknown = set(df[col].dropna()) - set(order)
        assert not unknown, f"{col} has answers that are not in the list: {unknown}"


def main():
    df = load_samples()
    df = drop_columns(df)
    df = fix_checkboxes(df)
    check_scales(df)
    df = combine_age(df)
    check_categories(df)

    # id and sample first, then all other columns
    first = ["id", "sample"]
    df = df[first + [c for c in df.columns if c not in first]]

    PROCESSED_DIR.mkdir(exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)

    # Short report, so you can see that everything worked
    print(f"Saved {CLEAN_FILE.name}: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df["sample"].value_counts().to_string())
    print("Missing answers (%):")
    gap_cols = ["MOODCHANGE", "PHYSCHANGE", "INTENSITY"]
    print((df[gap_cols].isna().groupby(df["sample"]).mean() * 100).round(1).to_string())


if __name__ == "__main__":
    main()
