# Beechcraft Bonanza G36 for FlightGear

A Beechcraft Bonanza G36 aircraft project for FlightGear, using JSBSim for the
flight dynamics and aiming to integrate FlightGear's FG1000 avionics.

**Status: early development.** The project currently contains an Aeromatic++-based
FDM with initial corrections and a minimal FlightGear aircraft definition.
The exterior model, cockpit, avionics and most aircraft systems still need to be
built. Flight behavior has not yet been validated against a G36 POH.

## Aircraft target

- Normally aspirated Continental IO-550-B, rated at 300 hp.
- Three-blade constant-speed propeller.
- Retractable tricycle landing gear.
- Original G1000-era cockpit, with FG1000 integration planned.
- Initial maximum takeoff weight target: 3,650 lb.

The precise model year, serial range and equipment configuration remain to be
selected. Sources and assumptions are recorded in [docs/SOURCES.md](docs/SOURCES.md).

## Current progress

| Area | State |
| --- | --- |
| JSBSim model | Loads; short integration checks pass |
| Engine and propeller | Initial specification corrections; calibration pending |
| Flight controls, flaps and gear | Basic generated behavior; full system behavior pending |
| Fuel | Capacity corrected; selector and tank locations unfinished |
| FlightGear integration | Minimal aircraft definition; runtime testing pending |
| Exterior and cockpit | Not implemented |
| Electrical, avionics and autopilot | Not implemented |

See the [roadmap](docs/ROADMAP.md) for the development order and
[baseline audit](docs/BASELINE_AUDIT.md) for known limitations.

## Install

The folder containing `Bonanza-G36-set.xml` must be named `Bonanza-G36` and sit
inside an additional aircraft directory configured in the FlightGear launcher.
If downloading a GitHub ZIP, rename the extracted `Bonanza-G36-main` folder.

Select **Beechcraft Bonanza G36 (FDM development)** in the launcher. The declared
minimum is FlightGear 2024.1.1; compatibility testing is still pending.
There is currently no visible aircraft or instrument panel.

For command-line use, add the following to your usual FlightGear command, replacing
the example aircraft directory with your checkout's absolute path:

```sh
--aircraft-dir=/path/to/FGAircraft/Bonanza-G36
--aircraft=Bonanza-G36
```

Startup defaults to engine off, gear down and parking brake set. Development-only
running-start instructions are in [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Development

Python 3.12 is recommended. CI uses Python 3.12 with JSBSim 1.3.1.
From the repository root on macOS or Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
```

On Windows, use `.venv\Scripts\python.exe` for the last two commands.
The tests check loading, initial mass, flap travel, airborne gear cycling and a
short running-engine integration. They do not validate aircraft performance.

## Repository layout

| Path | Purpose |
| --- | --- |
| `Bonanza-G36-set.xml` | FlightGear aircraft definition |
| `Bonanza-G36.xml` | JSBSim aircraft model |
| `Engines/` | Engine and propeller definitions |
| `Systems/` | JSBSim control and system definitions |
| `tests/` | Standalone JSBSim checks |
| `docs/` | Roadmap, sources, input history and development notes |
| `.github/` | CI and issue/PR templates |

Model, instrument and Nasal directories will be added when their first assets or
implementations are ready.

## Contributing and attribution

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Record sources
and distinguish measured data from estimates when changing aircraft behavior.

The initial model was generated using Aeromatic++ 3.3.21 from JSBSim v1.3.1.
Author and generator credits are listed in [AUTHORS](AUTHORS).
This is an independent FlightGear project, not a manufacturer-endorsed product.

## License

This project is licensed under the **GNU General Public License, version 2 or
any later version** (`GPL-2.0-or-later`). See [COPYING](COPYING) for the license
text and [docs/LICENSING.md](docs/LICENSING.md) for the license notice and scope.
