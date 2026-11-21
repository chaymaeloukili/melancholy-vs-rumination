"""Settings that all scripts share: folder paths, sample names and the order of categories."""

from pathlib import Path

# Folders. ROOT is the project folder, found from where this file is (src/ -> one folder up).
# This way the scripts work no matter from which folder you start them.
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"              # original data (never modified)
PROCESSED_DIR = ROOT / "data" / "processed"  # cleaned data
RESULTS_DIR = ROOT / "results"               # tables from the analysis

CLEAN_FILE = PROCESSED_DIR / "sad_music_clean.csv"

# Raw file -> sample name (S2 and S3 are swapped in the documentation, see data/raw/README.md)
SAMPLES = {
    "S1_data.csv": ("S1", "S1_Finland_convenience"),
    "S2_data.csv": ("S2", "S2_Finland_quota"),
    "S3_data.csv": ("S3", "S3_UK_representative"),
}
SAMPLE_NAMES = [name for _, name in SAMPLES.values()]

# Order of the answers, from little / bad to a lot / good.
# A CSV file only stores text, so this order is set again every time the data is loaded.
CATEGORY_ORDER = {
    "age": ["18 to 24", "25 to 34", "35 to 44", "45 to 54", "55 to 64", "65 or older"],
    "listensad": ["I don't listen to sad music voluntarily", "Rarely", "Sometimes", "Often", "Frequently"],
    "AGO": ["less than day", "2-5 days", "6-10 days", "11-30 days", "1-6 mo", "7-12 mo", "over year"],
    "FAM": ["unfamiliar", "somewhat familiar", "familiar", "extremely familiar"],
    "IMPORTANCE": ["Not at all", "Quite Important", "Important", "Extremely Important"],
    "DURATION": ["<5min", "5-10 min", "10-30 min", "31-60 min", "60 min+"],
    "MOODCHANGE": ["Worse", "Same", "Better"],
    "PHYSCHANGE": ["Worse", "Same", "Better"],
    "ESSENTIAL1": ["Never", "Rarely", "Sometimes", "Frequently", "Very Frequently"],
    "ESSENTIAL2": ["Never", "Rarely", "Sometimes", "Frequently", "Very Frequently"],
    "ESSENTIAL3": ["Never", "Rarely", "Sometimes", "Frequently", "Very Frequently"],
}

# Stricter limit for tests on many items at once (about 0.05 divided by 50 tests)
P_LIMIT = 0.001
