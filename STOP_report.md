---
title: "Structural-Thermal-Optical Analysis of a 50 mm f/1.25 LWIR Objective"
author: "Tufan Turşu"
date: "November 2026"
---

## Abstract

A three-element Ge/ZnSe/Ge objective (f = 50 mm, f/1.25, 8–12 µm) was designed in Zemax OpticStudio and reaches the diffraction limit at 20 °C (MTF 0.353 vs 0.355 at 42 lp/mm). Its thermal focus shift is linear at −5.9 µm/°C, about 20 depths of focus over −40…+70 °C. A titanium housing reduces the shift by only ~10 %. A passive Ge/ZnSe/AMTIR-1 solution removes it but degrades MTF at f/1.25, so an active focus compensator is required (≈0.69 mm travel). A steady-state Ansys thermal model of the lens and housing (internal dissipation 3.5 W, wind convection, solar load) shows lens temperatures 4.8–6.0 °C above a 70 °C ambient with intra-lens gradients below 0.1 °C. The model is mesh-independent within 0.002 % and closes the energy balance. Feeding these temperatures back into Zemax yields 35 µm of extra defocus relative to the ambient-based prediction, equal to one depth of focus. The compensator must therefore be referenced to the lens-mount temperature.


![Thermal focus shift versus temperature; uniform-temperature cases and STOP case](../results/figures/00_focus_shift_vs_temperature.png)

## 1. Optical design (Zemax OpticStudio 2025 R2)

| Parameter | Value |
|---|---|
| Effective focal length | 50.0 mm |
| Entrance pupil / f-number | 40 mm / f/1.25 |
| Spectral band | 8–12 µm (primary 10 µm) |
| Field of view | 0°, 4°, 5.6° (half-diagonal) |
| Detector (assumed) | 640 × 512, 12 µm pitch uncooled microbolometer → Nyquist 42 lp/mm |
| Elements | Ge / ZnSe / Ge, all spherical |
| Total track | 71.85 mm (back focal distance 4.91 mm) |

Prescription at 20 °C (`zemax/v1_nominal.zmx`, configuration 1):

| Surface | Radius (mm) | Thickness (mm) | Material | Clear semi-diameter (mm) |
|---|---|---|---|---|
| 1 (stop) | 63.783 | 5.000 | Germanium | 20.32 |
| 2 | 90.200 | 21.107 | air | 19.47 |
| 3 | −143.609 | 4.000 | ZnSe | 14.97 |
| 4 | −191.407 | 31.832 | air | 14.83 |
| 5 | 20.785 | 5.000 | Germanium | 8.18 |
| 6 | 20.210 | 4.913 | air | 6.54 |

The design is diffraction-limited at 20 °C: polychromatic MTF at the 42 lp/mm Nyquist frequency is 0.353 against a diffraction limit of 0.355 (99 %). The through-focus MTF at 20 lp/mm peaks at 0.68, at the nominal image plane.

![Nominal MTF](../results/figures/01_mtf_nominal_20C.png)

## 2. Thermal defocus with uniform temperature

Using Zemax *Make Thermal*: −40 / 20 / +70 °C, glass dn/dT and CTE from the INFRARED catalog, and aluminium air-space mounts (CTE 23.6 × 10⁻⁶ /K).

| Temperature | Best-focus shift | Peak MTF @ 20 lp/mm (refocused) |
|---|---|---|
| −40 °C | +0.36 mm | 0.689 |
| 20 °C | 0.00 mm | 0.68 |
| +70 °C | −0.29 mm | 0.675 |

- The focus shift is linear at **−5.9 µm/°C**, dominated by the dn/dT of germanium (≈400 × 10⁻⁶ /K).
- Refocused, image quality is unchanged at every temperature. **The problem is focus position, not aberrations.**
- With the detector fixed, MTF collapses to ≈0 at both temperature extremes.

| −40 °C | 20 °C | +70 °C |
|---|---|---|
| ![](../results/figures/02_throughfocus_m40C.png) | ![](../results/figures/03_throughfocus_20C.png) | ![](../results/figures/04_throughfocus_p70C.png) |

### Athermalization options investigated

| Approach | Outcome |
|---|---|
| Titanium instead of aluminium housing | Shift at +70 °C reduced only from −0.30 to −0.27 mm (≈10 %). A single housing material would need CTE ≈ −85 × 10⁻⁶ /K, which no metal has. |
| Passive optical (Ge / ZnSe / AMTIR-1, all-spherical, optimised over 3 temperatures) | Focus shift removed, but peak MTF @ 20 lp/mm fell from 0.68 to ≈0.24–0.35 at f/1.25 |
| **Active focus compensator (selected)** | Restores diffraction-limited performance; required travel ≈ 0.69 mm (−0.33 … +0.36 mm) |

## 3. Thermal model (Ansys Workbench / Mechanical 2025 R2, steady-state)

**Geometry:** `geometry/lwir_geometri_spaceclaim.py`, a parametric SpaceClaim script. Lenses are modelled as flat disks of their centre thickness and clear diameter. Each lens sits in an aluminium mount ring inside a Ø46/52 mm tube with a 3 mm rear cap. The detector is a Ø12 × 1 mm silicon disk. Nine bonded contacts are detected automatically.

**Materials:**

| Material | k (W/m·K) | ρ (kg/m³) | E (GPa) | ν | CTE (10⁻⁶ /K) |
|---|---|---|---|---|---|
| Germanium | 60 | 5323 | 103 | 0.28 | 5.7 |
| ZnSe | 18 | 5270 | 67 | 0.28 | 7.1 |
| Silicon | 149 | 2330 | 130 | 0.28 | 2.6 |
| Aluminium alloy | Ansys library | | | | |

**Loads and boundary conditions:**

- Detector: 0.5 W internal heat generation.
- Electronics: 3 W heat flow into the rear cap.
- External convection on all six exterior faces: h ≈ 55 W/m²·K (Churchill–Bernstein gives 53; rounded up) for 10 m/s cross-flow over a Ø52 mm cylinder.
- Solar (case B only): 1000 W/m², absorptivity 0.5, averaged around the circumference → 160 W/m² on the tube.

**Results:**

| Case | Lens 1 (Ge) | Lens 2 (ZnSe) | Lens 3 (Ge) | Model min / max |
|---|---|---|---|---|
| A: 20 °C, no sun | — | — | — | 22.8 / 25.2 °C (avg 23.7) |
| **B: 70 °C + sun** | **74.8 °C** | **75.2 °C** | **76.0 °C** | 74.8 / 77.2 °C |

- **Energy-balance check (case A):** 3.5 W / (55 W/m²·K × 0.0178 m²) = 3.6 K above ambient → 23.6 °C, against a computed average of 23.7 °C.
- **Gradient inside each lens is below 0.1 °C.** Thermal behaviour is governed by the bulk temperature offset, not by gradients.
- **Mesh independence** (lens 3 mean temperature, case B): 3 mm, 5,295 elements → 75.998 °C; 1.5 mm → 75.997 °C; 0.75 mm, 226,595 elements → 75.998 °C. The variation is below 0.002 %, and the 1.5 mm mesh was retained.

| Case A: 20 °C | Case B: 70 °C + solar |
|---|---|
| ![](../results/figures/05_thermal_20C.png) | ![](../results/figures/06_thermal_70C_solar.png) |

## 4. Closing the STOP loop

The mean Ansys lens temperature for case B (≈75.5 °C) was applied as the configuration temperature in Zemax (`zemax/v2_stop_75C.zmx`):

| | Best-focus shift |
|---|---|
| Ambient-based assumption (70 °C) | −0.290 mm |
| Thermal-model lens temperature (75.5 °C) | **−0.325 mm** |
| Difference | **35 µm ≈ 1 × depth of focus** |

A compensator positioned from ambient temperature would leave the image ~35 µm out of focus. Read from the through-focus curve, that lowers MTF at 20 lp/mm from ≈0.68 to ≈0.55, and the loss is larger at Nyquist. The temperature sensor for the compensator belongs at the lens mount.

![STOP through-focus](../results/figures/07_throughfocus_STOP_75p5C.png)

## Assumptions and limitations

- The optical temperature in each Zemax configuration is uniform; the three lens temperatures (74.8–76.0 °C) are represented by their mean.
- The thermal model is conduction-only: internal air convection and radiation are not modelled, and lenses are flat disks.
- External h comes from a correlation, not CFD. Solar load is smeared uniformly, so no lateral gradient (tilt) is captured.
- No thermo-elastic (structural) analysis was run. The sub-0.1 °C intra-lens gradients suggest surface deformation is negligible here, but this is not verified.
- The detector format and solar absorptivity are assumed values.

## Next steps

1. External-flow CFD (Fluent) to replace the correlation-based h with a computed distribution.
2. One-sided solar loading to capture lateral gradients and line-of-sight tilt.
3. Thermo-structural analysis in Static Structural, with Zernike decomposition of the surface deformation fed back to Zemax.
4. Transient warm-up to size the compensator control loop.

