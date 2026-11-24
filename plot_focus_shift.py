import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1]
T = np.array([-40.0, 20.0, 70.0])          # uniform temperature (ambient) configs
dz = np.array([0.36, 0.00, -0.29]) * 1000  # best-focus shift, µm (Zemax through-focus, 0° field)
k, b = np.polyfit(T, dz, 1)
T_stop, dz_stop = 75.5, -325.0             # STOP case (lens temps from Ansys)

surf, ink, ink2, grid = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
c1, c2 = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(8, 4.8), dpi=150)
fig.patch.set_facecolor(surf); ax.set_facecolor(surf)

tt = np.linspace(-45, 80, 50)
ax.fill_between(tt, k*tt+b-31, k*tt+b+31, color=c1, alpha=0.10, lw=0)
ax.plot(tt, k*tt+b, color=c1, lw=2, label=f"Linear fit: {k:.2f} µm/°C")
ax.plot(T, dz, "o", color=c1, ms=9, mec=surf, mew=2, label="Uniform temperature (Zemax)")
ax.plot([T_stop], [dz_stop], "D", color=c2, ms=9, mec=surf, mew=2,
        label="STOP: Ansys lens temps, 70 °C + solar")
for t, d in zip(T, dz):
    ax.annotate(("0 µm" if d == 0 else f"{d:+.0f} µm"), (t, d), textcoords="offset points", xytext=(10, 6), color=ink2, fontsize=10)
ax.annotate("−325 µm\n(35 µm beyond ambient-based value)", (T_stop, dz_stop), textcoords="offset points",
            xytext=(-118, -30), color=ink2, fontsize=10)
ax.text(-44, k*-44+b+40, "± depth of focus (31 µm)", color=ink2, fontsize=9)

ax.axhline(0, color=ink2, lw=0.8)
ax.set_xlabel("Temperature (°C)", color=ink); ax.set_ylabel("Best-focus shift (µm)", color=ink)
ax.set_title("Thermal focus shift — f = 50 mm f/1.25 LWIR objective (Ge/ZnSe/Ge, Al housing)",
             color=ink, fontsize=11, loc="left")
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(colors=ink2)
ax.legend(frameon=False, loc="lower left", fontsize=9.5)
fig.tight_layout(); fig.savefig(out, facecolor=surf)
print(f"slope={k:.3f} um/C intercept={b:.1f}")
