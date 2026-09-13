# Contributing

The project is in early development. Start with [the roadmap](docs/ROADMAP.md)
and open an issue before a large system implementation so work does not overlap.

## Changes

Keep each pull request focused on a concrete behavior or feature. Explain the
problem, the change and its effect. For FDM or system changes, include the source,
applicable serial range, units and any remaining assumptions in
[docs/SOURCES.md](docs/SOURCES.md).

Use descriptive XML/Nasal/property names and preserve source attribution.
Use two-space indentation in new XML and YAML, and four spaces in Python.
Avoid reformatting unrelated aerodynamic tables or changing numbers merely to
make a test pass.

## Verification

Run the README's unittest command and `git diff --check` before submitting.
Add a behavior check when it protects a meaningful assumption or fixes a defect;
documentation changes do not need new tests.

For a FlightGear test, record the simulator version, platform, aircraft commit,
initial state, weight/CG, fuel, weather and steps. Attach relevant log excerpts
or measurements. A screenshot alone cannot establish correct aerodynamics.

Do not commit virtual environments, simulator logs, generated ZIPs, downloaded
manuals or unrelated aircraft assets. Link to references instead. For any new
third-party asset, record its author, source and redistribution license.
Submit original project contributions under GPL-2.0-or-later and preserve
applicable upstream notices. See [docs/LICENSING.md](docs/LICENSING.md).
