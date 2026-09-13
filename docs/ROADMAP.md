# Development roadmap

The first milestone is a reproducible, documented aircraft baseline. A successful
JSBSim load is the starting point, not a finished flight model.

## 1. Establish the reference aircraft

- [ ] Select model year, serial range, propeller/governor and installed equipment.
- [ ] Identify the applicable POH revisions and supplements.
- [ ] Record weight, CG datum, loading stations, dimensions and control limits.
- [ ] Separate confirmed inputs from derived values and placeholders in SOURCES.md.
- [x] Select GPL-2.0-or-later and record authorship and generator provenance.
- [ ] Record applicable terms for third-party assets as they are introduced.

Complete when the chosen configuration and reference set are explicit enough to
resolve conflicting specifications without mixing aircraft variants.

## 2. Build a dependable FDM baseline

- [x] Generate the initial model and correct basic engine/propeller specifications.
- [x] Add repeatable model-load, mass, flap, gear and engine smoke checks.
- [ ] Run the package in FlightGear and record startup behavior and logs.
- [ ] Reconstruct CG, loading stations, tank locations and gear contact geometry.
- [ ] Calibrate engine power, fuel flow, propeller coefficients and governor range.
- [ ] Validate ground clearance, suspension, steering and braking.
- [ ] Establish trim, clean/landing stall, climb and cruise test cases.
- [ ] Tune aerodynamic coefficients against those cases with explicit tolerances.

Complete when measurements can be reproduced at stated weights, CG positions and
atmospheric conditions, with discrepancies recorded. Do not calibrate aerodynamics
around an unverified engine/propeller combination.

## 3. Implement aircraft systems

- [ ] Fuel selector: LEFT / RIGHT / OFF, feed behavior and pump logic.
- [ ] Electrical: batteries, alternators, buses, loads, switches and failures.
- [ ] Engine start/shutdown: ignition, starter, mixture and electrical dependencies.
- [ ] Gear: interlocks, indications, timing, warning logic and manual extension.
- [ ] Flaps: cockpit selection, limits, timing and electrical dependencies.
- [ ] Lights, pitot/static instruments, warnings and startup states.

Complete each system with documented property inputs/outputs and normal/failure
checks. Shared initialization logic should apply to both cockpit controls and
aircraft states.

## 4. Build the exterior and cockpit

- [ ] Establish model axes, origin and dimensions against the FDM datum.
- [ ] Create exterior mesh, landing gear, control surfaces, materials and textures.
- [ ] Create cockpit, seats, panel, switches and instrument locations.
- [ ] Add animations, interaction areas, lighting and sound.

Visual work can proceed alongside systems once the reference geometry is stable.
Keep editable source assets with attribution; avoid unnecessary generated copies.

## 5. Integrate avionics and flight guidance

- [ ] Evaluate FG1000 against the selected G1000 installation.
- [ ] Connect displays to aircraft electrical power and sensor state.
- [ ] Add engine indications, alerts, radios and navigation behavior.
- [ ] Implement the selected autopilot and flight-director modes.
- [ ] Test normal operation, power loss, sensor failures and mode transitions.

The target is the selected G36 installation; FG1000 availability alone does not
make the avionics integration complete.

## 6. Prepare a first usable release

- [ ] Test complete startup, taxi, takeoff, climb, cruise, approach and shutdown.
- [ ] Record supported FlightGear versions and platform-specific issues.
- [ ] Add screenshots, user instructions, performance results and known limitations.
- [ ] Verify asset provenance, packaging and release installation.
- [ ] Tag a release only after the documented acceptance checks pass.

No release date is assigned yet. Track implementation tasks as GitHub issues and
keep this document focused on milestones and acceptance criteria.
