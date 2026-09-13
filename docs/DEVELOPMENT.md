# Development workflow

## Local setup

Keep the checkout at `FGAircraft/Bonanza-G36` so FlightGear can use it directly.
Follow the README to install the pinned standalone JSBSim dependency and run:

```sh
.venv/bin/python -m unittest discover -s tests -v
git diff --check
```

GitHub Actions runs the same suite using Python 3.12 on Ubuntu and macOS.
These jobs exercise standalone JSBSim, not a graphical FlightGear installation.

Use a focused branch for work, for example `feat/fuel-selector` or
`fix/propeller-governor`. Keep factual specification corrections separate from
performance tuning so changes can be assessed independently.

## First GitHub upload

Create an empty GitHub repository named `Bonanza-G36`, with no automatically
generated README, gitignore or license. Extract this project's folder and run
the following **inside that folder**, after the tests pass:

```sh
git init -b main
git add .
git diff --cached --check
git status --short
git commit -m "Initial Bonanza G36 development baseline"
```

Copy the repository URL shown by GitHub and use it in these commands:

```sh
git remote add origin <repository-url>
git push -u origin main
```

Replace `<repository-url>` before running; it is a placeholder, not a shell
argument to paste literally. If this folder already has Git history, retain it
and use its existing branch/remotes instead of treating it as a new repository.
Commit the source files, including `.github/`, rather than uploading the ZIP as
the repository's only file.

Suggested description: **Beechcraft Bonanza G36 for FlightGear — JSBSim aircraft
in early development, with FG1000 integration planned.**

Suggested topics: `flightgear`, `jsbsim`, `beechcraft`, `bonanza`, `flight-simulator`.

## FlightGear development start

Add these options to your usual FlightGear invocation, replacing the path:

```sh
--aircraft-dir=/path/to/FGAircraft/Bonanza-G36
--aircraft=Bonanza-G36
--airport=KSFO
--on-ground
--prop:/sim/presets/running=true
--prop:/controls/engines/engine/throttle=0.2
```

This requests a running-engine start and bypasses a realistic start sequence.
The parking brake remains set. This invocation still needs testing in FlightGear.
The absence of an exterior mesh and cockpit is expected at this stage.

## Verification scope

The tests establish that the model loads without external engine/system files,
the initial mass matches the chosen load, flaps reach requested positions, gear
cycles in an airborne case and a running engine integrates without nonfinite
state. They do not prove real-world flight behavior or ground-system interlocks.

For performance work, record commit, simulator version, mass, CG, fuel, pressure,
temperature, altitude, configuration, control settings and stabilization period.
Define expected measurements and tolerances before changing coefficients.
Keep disposable outputs under `test-results/`; commit only useful reference
datasets and accompanying provenance.
