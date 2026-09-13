# Sources and assumptions

Aircraft data must be checked against the chosen model year, serial range and
configuration. The initial project mixes an early-weight assumption with some
later G36 reference specifications; this is documented, not resolved.

## Source register


1. [Continental 550-series engine specification, IO-550-B row](https://continental.aero/wp-content/uploads/2026/03/Continental-specsheet-Avgas-550-Engine-Series-v4_WEB.pdf).
2. [Beechcraft G36 Specification and Description, E-4063–E-4080, manufacturer document mirrored on Scribd](https://www.scribd.com/document/357917315/Bonanza-G36-Specification-and-Description-E-4063-Thru-E-4080).
   A later equipment configuration, used selectively rather than adopted wholesale.
3. [Bonanza 36 overview, Korean aviation portal](https://www.airportal.go.kr/file/htmlOpen/upload/aircraft/Beechcraft%20Bonanza%2036.pdf).
   Secondary family-level reference from the earlier input review, not a G36 POH.
4. [JSBSim v1.3.1 Aeromatic Aircraft.cpp](https://github.com/JSBSim-Team/jsbsim/blob/v1.3.1/utils/aeromatic%2B%2B/Aircraft.cpp).
5. [FlightGear 2024.1 JSBSim interface](https://github.com/FlightGear/flightgear/blob/release/2024.1/src/FDM/JSBSim/JSBSim.cxx).
6. [JSBSim v1.3.1 FGPropeller.cpp](https://github.com/JSBSim-Team/jsbsim/blob/v1.3.1/src/models/propulsion/FGPropeller.cpp).

## Recording future data

For every new or revised value, record the document title, revision, page/table,
serial applicability, original units, conversion and target XML property. Label
it as published, calculated or estimated. Track missing evidence as a roadmap
item instead of silently promoting estimates to verified values.

The initial corrections and unresolved assumptions are in
[BASELINE_AUDIT.md](BASELINE_AUDIT.md). Generator input choices are recorded in
[AEROMATIC_INPUTS.json](AEROMATIC_INPUTS.json).
