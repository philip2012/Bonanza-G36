# Baseline audit — 12 September 2026

## Result

The original upload loads and initializes in standalone JSBSim 1.3.1. It is a
generic generated model, not a validated G36. A successful load does not establish
correct handling, performance, systems behavior, or FlightGear compatibility.

## Changes made

| Item | Original XML | Revised XML | Basis |
|---|---|---|---|
| Engine maximum RPM | 2800 | 2700 | Continental IO-550-B specification [1] |
| Displacement | 570 in³ | 552 in³ | [1] |
| Bore / stroke | 5.125 / 4.375 in | 5.25 / 4.25 in | [1] |
| Compression ratio | 8.0 | 8.5 | [1] |
| Propeller blade count | 2 | 3 | G36 manufacturer description [2] |
| Propeller diameter | 6.33 ft | 6.333333 ft | Preserve chosen 76-inch baseline [3] |
| Governor maximum | 2962.6 RPM | 2700 RPM | Direct-drive engine rated speed [1] |
| Governor minimum command | 2518.2 RPM | 1800 RPM | Explicit development assumption; verify governor/POH |
| Usable fuel capacity | 540.2 lb total | 444 lb total, 222 per tank | Manufacturer usable capacity [2] |
| Initial fuel | 270.1 lb total | 222 lb total | Retain half-full starting condition |
| Flap traverse intermediate point | 15° | 12° | Bonanza family reference [3]; verify chosen POH |
| FlightGear launcher configuration | Absent | Bonanza-G36-set.xml | Minimal JSBSim registration [4,5] |

Engine power remains 300 hp. Correcting dimensions does not calibrate the engine's
power curve, fuel flow or temperatures. The propeller's blade-count field does
not rebuild its thrust/power tables: these remain generic, as do its inertia and
12°/45° pitch stops. The provisional 1800 RPM command minimum is not an idle speed
or a demonstrated operating limitation.

The original propeller comment claims 60,703 lb static thrust. This is generated
comment text, not a measured simulation result or a direct thrust input. It has
been replaced with an accurate development-status comment; the original value is
recorded here. Actual thrust must be tested using the coefficient tables.

The old JSON and original XML snapshots were retained in the earlier reviewed
ZIP. They are omitted from the repository package. The JSON disagrees with the
runtime XML (including mass and flap limits) and is not loaded by FlightGear.

## Weight, geometry and unresolved behavior

- Original start weight: 2530 empty + 289.9 payload + 270.1 fuel = **3090 lb**.
  Revised start weight: 2530 + 289.9 + 222 = **3041.9 lb**. At full usable fuel,
  the remaining allowance to the selected 3650 lb MTOW is 676 lb. Payload still
  sits at a single placeholder CG point. Neither version starts at MTOW.
- Empty weight 2530 lb remains the previously selected early-aircraft assumption;
  the later equipped aircraft described in [2] is heavier. Select a real serial
  and equipment list before treating weight as authoritative.
- The 5.44 ft chord in generated XML is the rounded mean aerodynamic chord
  calculated from 7 ft root chord and 0.5 taper. It is not evidence that the root
  chord input was lost. The generator's comment misleadingly labels it root chord.
  The supplied span, area and idealized trapezoid are not exactly self-consistent;
  do not force a root-glove wing into a single trapezoid without drawings.
- Inertias 1607.02 / 1925.20 / 3223.32 slug ft² are estimates. Tail arms 14.30 /
  13.75 ft were estimated automatically. Tail areas 36.82 / 15.6 ft² are provisional
  sums from [3], not verified manufacturer reference areas.
- CG at x=12.65 ft and the other stations use Aeromatic's estimated geometry.
  Do not enter POH CG limits into this datum without transforming coordinates.
  Both fuel tanks sit at the CG, so lateral fuel imbalance is not represented.
- The engine feeds only tank 0. Tank 1 is not connected through a selectable
  LEFT/RIGHT/OFF system. Its fuel cannot currently sustain this engine. This needs
  a proper selector, tank locations, unusable fuel accounting and pump behavior.
- Gear track is 6.04 ft and wheelbase 9.59 ft in this model. These are generated
  placements, not measured G36 geometry. Spring/damping rates, 5° nose steering,
  clearance, gear timing and ground behavior need reconstruction and testing.
- The gear-no-wow switch suppresses some aerodynamic terms on the ground; it
  does **not** prevent gear retraction on the ground. No electrical or emergency
  extension behavior exists. Do not infer those systems from the retractable flag.
- Flap motion now passes through 12°, but there is no three-position cockpit
  switch yet. Normalized commands 0 / 0.4 / 1 request 0° / 12° / 30°. Motion timing
  is still generic. Elevator, rudder and aileron limits remain generic.
- Stall input 68.5 kt was an approximate weight-scaled starting target, not a
  demonstrated result. The lift/stall tables, induced drag, Reynolds-number
  dependencies and stall-initiator yaw term remain unvalidated. Propwash pitch
  scaling uses wing span in the generated formula and warrants a derivation check
  before any change. Root/tip washout is not explicitly modeled.
- No 3D model, cockpit, FG1000, autopilot, electrical buses, annunciations or
  realistic startup/shutdown system has been added.

## Checks performed

Using JSBSim 1.3.1, the original standalone check script verifies XML parsing, aircraft-local engine
and system lookup with the same path layout used by FlightGear, initial weight,
flap extension/retraction, airborne gear cycling, and finite integration with a
running engine. All checks passed. The 10-second engine scenario ended at roughly
2058 RPM and 122 hp; it is an untrimmed integration smoke check, not a power or
governor calibration test. The engine initialization helper needs control positions
to update before invoking init_running; the check explicitly advances one frame.

FlightGear itself was not available for testing. No ground-handling, trim,
stall-speed, cruise, climb, fuel-selector, governor-range or electrical validation
has been completed. Next work should establish a POH/serial baseline and datum,
then calibrate propulsion before drawing conclusions from performance tests.


## Repository setup update — 13 September 2026

The smoke checks now live in `tests/test_baseline.py` and use unittest discovery.
Sources are collected in [SOURCES.md](SOURCES.md). Input choices are documented
in [AEROMATIC_INPUTS.json](AEROMATIC_INPUTS.json). Machine-specific paths were
removed from runtime comments; no numeric FDM values were changed in this update.
