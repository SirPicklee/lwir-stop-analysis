"""Project 1b: lens temperature rise above 70 °C ambient for three thermal boundary-condition cases."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1] if len(sys.argv) > 1 else "10_project1b_lens_temperatures.png"
lenses = ["Lens 1 (Ge)", "Lens 2 (ZnSe)", "Lens 3 (Ge)"]
amb = 70.0
cases = {
    "h = 55 W/m²K (correlation), uniform sun": [74.83, 75.21, 76.00],
    "h = 67 W/m²K (Fluent CFD), uniform sun":  [73.80, 74.22, 74.99],
    "h = 67 W/m²K (Fluent CFD), one-sided sun": [73.84, 74.22, 74.98],
}
colors = ["#2a78d6", "#eb6834", "#1baf7a"]
surf, ink, ink2, grid = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(8, 4.6), dpi=150)
fig.patch.set_facecolor(surf); ax.set_facecolor(surf)
x = np.arange(len(lenses)); w = 0.26
for i, ((name, T), c) in enumerate(zip(cases.items(), colors)):
    rise = np.array(T) - amb
    bars = ax.bar(x + (i - 1) * w, rise, w - 0.03, color=c, label=name, edgecolor=surf, linewidth=2)
    for b, r in zip(bars, rise):
        ax.text(b.get_x() + b.get_width() / 2, r + 0.08, f"{r:.1f}", ha="center", color=ink2, fontsize=9)
ax.set_xticks(x, lenses, color=ink)
ax.set_ylabel("Mean lens temperature above ambient (°C)", color=ink)
ax.set_title("Lens heating at 70 °C ambient + solar — effect of CFD h and sun direction",
             color=ink, fontsize=11, loc="left")
ax.set_ylim(0, 7)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(colors=ink2)
ax.legend(frameon=False, loc="upper left", fontsize=9)
fig.tight_layout(); fig.savefig(out, facecolor=surf)
