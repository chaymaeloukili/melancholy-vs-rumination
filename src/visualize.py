"""Charts: reads the tables from results/ and saves the charts as PNG files in figures/.

Run from the project folder (after analysis.py):  python src/visualize.py
"""

import textwrap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import to_rgb
from matplotlib.patches import FancyBboxPatch

from config import RESULTS_DIR, ROOT, SAMPLE_NAMES

FIGURES_DIR = ROOT / "figures"


# ---------- Style: the same look for every chart ----------

PURPLE = "#551A8B"   # the purple of a link you have already clicked
COLORS = {"Worse": "#C48BB8", "Same": "#DCD2EA", "Better": PURPLE}
TEXT_ON = {"Worse": "#3f2340", "Same": "#3f3550", "Better": "white"}   # readable text on each colour
BACKGROUND = "#F8F5FA"
INK = "#241c2e"      # titles
SOFT_INK = "#3f3550" # labels
MUTED = "#9b90a6"    # small notes

SAMPLE_LABELS = {
    "S1_Finland_convenience": "Finland · fans",
    "S2_Finland_quota": "Finland · quota",
    "S3_UK_representative": "UK · representative",
}
SOURCE = "Data: Eerola (2016), CC0"


def new_card(width=9, height=4.4):
    """A figure that looks like a white card with round corners on a soft background."""
    fig = plt.figure(figsize=(width, height), dpi=200, facecolor=BACKGROUND)
    card = FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="round,pad=0,rounding_size=0.04",
                          transform=fig.transFigure, facecolor="white", edgecolor="#ECE6F2",
                          linewidth=1.2, zorder=-10)
    fig.patches.append(card)
    return fig


def add_titles(fig, kind, title, note):
    """Small coloured chart type, the title (the finding) and a note with the source at the bottom."""
    fig.text(0.06, 0.91, kind, color=PURPLE, fontsize=9, fontweight="bold", va="top")
    # long titles go onto a new line instead of being cut off ("\n" in the title = my own line break)
    title = "\n".join(textwrap.fill(line, width=70) for line in title.split("\n"))
    fig.text(0.06, 0.85, title, color=INK, fontsize=11, fontweight="bold", va="top", linespacing=1.4)
    fig.text(0.06, 0.08, f"{note}  ·  {SOURCE}", color=MUTED, fontsize=7.5)


def add_legend(fig, x=0.62, y=0.66):
    """Round colour dots with Worse, Same, Better."""
    for i, (mood, color) in enumerate(COLORS.items()):
        dot_x = x + i * 0.11
        dot = FancyBboxPatch((dot_x, y), 0.016, 0.028, boxstyle="round,pad=0,rounding_size=0.014",
                             transform=fig.transFigure, facecolor=color, edgecolor="none", alpha=0.9)
        fig.patches.append(dot)
        fig.text(dot_x + 0.024, y, mood, fontsize=8.5, color=SOFT_INK)


def soft_bar(ax, x, y, w, h, color, px_per_x, px_per_y):
    """One round bar with soft edges, a little lighter in the middle (the watercolour look).

    Instead of a normal bar, this draws a small picture (an image) of the bar:
    - dist tells for every pixel how far it is from the edge of a rounded shape (negative = inside)
    - alpha makes the edge fade out softly instead of a hard line
    - strength makes the colour a bit lighter towards the middle
    """
    pw, ph = max(int(w * px_per_x), 8), int(h * px_per_y)   # size of the bar in pixels
    pad = 6                                                  # space for the soft edge
    X, Y = np.meshgrid(np.arange(pw + 2 * pad), np.arange(ph + 2 * pad))
    cx, cy = (pw + 2 * pad) / 2, (ph + 2 * pad) / 2
    r = min(ph / 2, pw / 2)                                  # radius: fully round ends
    dx = np.maximum(np.abs(X - cx) - (pw / 2 - r), 0)
    dy = np.maximum(np.abs(Y - cy) - (ph / 2 - r), 0)
    dist = np.sqrt(dx ** 2 + dy ** 2) - r

    alpha = np.clip(0.5 - dist / 2.5, 0, 1)                  # soft edge
    strength = 0.9 - 0.12 * np.clip(-dist / (ph / 2), 0, 1)  # lighter in the middle
    rgb = 1 - strength[..., None] * (1 - np.array(to_rgb(color)))   # mix colour with white paper
    image = np.dstack([rgb, alpha * 0.93])

    ex, ey = pad / px_per_x, pad / px_per_y
    ax.imshow(image, extent=[x - ex, x + w + ex, y + h + ey, y - ey],
              aspect="auto", zorder=2, interpolation="bilinear")


def save(fig, name):
    FIGURES_DIR.mkdir(exist_ok=True)
    fig.savefig(FIGURES_DIR / f"{name}.png", facecolor=BACKGROUND)
    plt.close(fig)
    print(f"Saved figures/{name}.png")


# ---------- Chart 1: Better / Same / Worse per sample ----------

def chart_mood_by_sample():
    pct = pd.read_csv(RESULTS_DIR / "02_moodchange_by_sample.csv", index_col=0)    # rows: Worse, Same, Better
    n = pd.read_csv(RESULTS_DIR / "02_moodchange_by_sample_n.csv", index_col=0).loc["All"]

    fig = new_card()
    box = [0.24, 0.16, 0.7, 0.46]                    # where the bars are: left, bottom, width, height
    ax = fig.add_axes(box)
    ax.set_zorder(5)
    ax.patch.set_alpha(0)

    width, height = fig.get_size_inches()
    px_per_x = box[2] * width * 100 / 102          # pixels per percent (x goes from -1 to 101)
    px_per_y = box[3] * height * 100 / 3.2         # pixels per bar row (y goes from -0.6 to 2.6)

    for row, sample in enumerate(SAMPLE_NAMES):
        left = 0
        for mood in ["Worse", "Same", "Better"]:
            value = pct.loc[mood, sample]
            soft_bar(ax, left + 0.5, row - 0.24, value - 1.0, 0.48, COLORS[mood], px_per_x, px_per_y)
            if value >= 5:                          # only label parts that are wide enough
                ax.text(left + value / 2, row, f"{value:.0f}%", ha="center", va="center",
                        color=TEXT_ON[mood], fontsize=9.5, fontweight="bold", zorder=3)
            left += value

    ax.set_xlim(-1, 101)
    ax.set_ylim(2.6, -0.6)                          # first sample at the top
    ax.set_yticks(range(3))
    ax.set_yticklabels([f"{SAMPLE_LABELS[s]}\nn = {n[s]:,}" for s in SAMPLE_NAMES])
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, labelsize=9.5, labelcolor=SOFT_INK)

    add_titles(fig, "Stacked Bar Chart", "After listening to sad music, most people in Finland felt better.\nIn the UK, many simply felt the same.",
               "Mood after a memorable experience with sad music")
    add_legend(fig)
    save(fig, "01_mood_by_sample")


def main():
    chart_mood_by_sample()


if __name__ == "__main__":
    main()
