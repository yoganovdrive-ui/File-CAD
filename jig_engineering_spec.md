# JIG Pick-and-Place Tutup Botol — Engineering Concept

Status: concept untuk DFM review, bukan drawing release.

## 1. Design basis

- Cap nominal: Ø28 mm, tinggi 15 mm, PP/HDPE.
- Bottle neck/cap axis: Z.
- Target: 30–60 caps/minute.
- Pneumatic supply: 5–6 bar, dry filtered air.
- Datum scheme: A = top surface base plate, B = longitudinal feeder reference, C = bottle-axis locator.
- Cap geometry, bottle geometry, cycle time, and robot interface wajib dikonfirmasi sebelum manufacturing.

## 2. Real materials and components

| Item | Component | Material / specification | Manufacturing / source |
|---|---|---|---|
| 1 | Base plate | Aluminium 6061-T6, clear anodized 15 µm | CNC mill, deburr 0.2–0.5 mm |
| 2 | Feeder rail | SUS304, t=3 mm | Laser cut + bend, passivate |
| 3 | Side guides | POM-C / Delrin, black | CNC mill; slotted adjustment |
| 4 | Pickup nest insert | POM-C, replaceable | CNC mill; captive screws |
| 5 | Bottle nest insert | UHMW-PE or POM-C | CNC mill; replaceable wear part |
| 6 | Stoppers | SMC / Festo compact pneumatic stopper, Ø16–20 mm bore | Bought-out component |
| 7 | Linear guide | HIWIN MGN12 or equivalent | Bought-out component |
| 8 | Z slide | SMC MXS / guided cylinder, sized by payload | Bought-out component |
| 9 | Vacuum generator | SMC ZH / Festo VN ejector, -40 to -60 kPa | Bought-out component |
| 10 | Suction cup | Silicone, Ø15–20 mm, food-contact grade if required | Bought-out component |
| 11 | Vacuum sensor | SMC ZSE20 / Festo vacuum switch | Bought-out component |
| 12 | Presence sensor | Omron E3Z / Keyence photoelectric sensor | Bought-out component |
| 13 | Fasteners | SUS304 socket-head M4/M5 | Standard hardware |
| 14 | Locating pins | Hardened steel Ø6 h6 | Reamed holes in base |
| 15 | Tube fittings | Nickel-plated brass or SUS304, 6 mm OD tubing | Standard pneumatic hardware |

## 3. Manufacturability rules

- Use 6 mm minimum internal corner radius where possible; use smaller radius only when feature requires it.
- Use 3 mm or 5 mm standard plate thicknesses; avoid custom sheet thickness.
- Use through holes and standard counterbores; avoid deep blind pockets.
- Use M4/M5 fasteners only; tool access must remain from top or front.
- Use slotted holes for feeder and sensor adjustment: 6 × 20 mm for M5 hardware.
- Keep replaceable wear inserts separate from aluminium base.
- Avoid contact between aluminium and wet product path; use POM/UHMW inserts.
- No sharp edges in cap path; break edges 0.2–0.5 mm.
- Design all food/product-contact surfaces removable without disassembling the base.
- Use standard pneumatic cylinders, tubing, sensors, and fittings; do not custom-machine actuators.

## 4. Functional dimensions — preliminary

| Feature | Nominal | Tolerance / note |
|---|---:|---|
| Base plate | 300 × 180 × 15 mm | ±0.10 mm overall |
| Feeder rail width | 30.0 mm | +0.20 / -0.00 mm; confirm cap OD |
| Side-guide opening | 28.8–29.5 mm adjustable | Do not freeze before cap sample test |
| Pickup pocket | Ø28.6 mm | +0.10 / -0.00 mm; replaceable insert |
| Cap pickup height | 50 mm from A | ±0.20 mm |
| Bottle-axis location | B/C intersection | ±0.10 mm |
| Vacuum cup | Ø18 mm nominal | Select after cap top-surface test |
| Stopper stroke | 5–10 mm | Per bought-out actuator |
| Bottle nest clearance | Cap/bottle supplier data | Must allow insertion without interference |

## 5. GD&T proposal

Apply to controlled drawing, not only 3D model:

- Base top datum A: flatness `0.10`.
- Feeder rail mounting face: perpendicularity `0.10 | A`.
- Feeder centerline: position `⌀0.20 | A | B`.
- Pickup pocket axis: position `⌀0.15 | A | B`.
- Bottle locator axis C: position `⌀0.15 | A | B`.
- Stopper mounting holes: position `⌀0.20 | A | B`.
- Linear guide mounting surface: parallelism `0.10 | A`.
- Z-slide axis to bottle axis: position `⌀0.20 | A | B | C`.
- Replaceable nest insert interface: profile `0.20 | A | B`.
- Do not assign tight tolerances to non-functional cosmetic faces.

Recommended datum logic:

```text
A = machined top of base plate
B = two reamed locating holes defining feeder direction
C = bottle-axis locator / third locating feature
```

## 6. Assembly strategy

1. Machine base plate, datum A, B holes, C locator, and tapped holes.
2. Install two Ø6 locating pins.
3. Bolt feeder rail using M5 slotted holes.
4. Install POM guide and pickup insert.
5. Install linear guide and pneumatic slide.
6. Install vacuum cup, vacuum sensor, and blow-off valve.
7. Install bottle nest and photoelectric sensors.
8. Adjust rail width with a master cap gauge.
9. Validate pickup using 100 consecutive cycles.

## 7. Acceptance test

- 100 cycles without double-feed.
- Pickup success ≥99% with production caps.
- Release success ≥99%.
- No cap deformation or visible scratches.
- Cap axis to bottle axis within ±0.30 mm at handoff.
- Vacuum loss detected within 100 ms.
- All fasteners accessible with standard hex tools.
- Wear inserts replaceable without removing base plate.

## 8. Open inputs before production release

- Actual cap drawing and supplier tolerance.
- Actual bottle-neck drawing and cap fit.
- Feeder type and incoming cap orientation.
- Robot/slide payload and stroke.
- Required cycle time.
- Product-contact and washdown requirements.
- Final GD&T drawing and inspection method.

## Important limitation

This is an engineering concept with preliminary dimensions. It is not yet a certified food-contact design or production-ready drawing. Release only after measuring real caps/bottles, checking vacuum pickup, and completing tolerance stack-up.
