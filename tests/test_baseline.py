# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2026 Philips (philip2012)
"""Basic JSBSim integration checks; not G36 performance validation."""

import math
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

import jsbsim


ROOT = Path(__file__).resolve().parents[1]
DT = 1 / 120


class BaselineTests(unittest.TestCase):
    def load_model(self):
        fdm = jsbsim.FGFDMExec(str(ROOT))
        fdm.set_debug_level(0)
        # Deliberately absent global directories: dependencies must resolve locally.
        self.assertTrue(fdm.load_model_with_paths(
            "Bonanza-G36", str(ROOT), str(ROOT / "unused-global-engines"),
            str(ROOT / "unused-global-systems"), False,
        ))
        fdm.set_dt(DT)
        fdm["ic/h-sl-ft"] = 5000
        fdm["ic/vc-kts"] = 120
        self.assertTrue(fdm.run_ic())
        return fdm

    def run_for(self, fdm, seconds):
        for _ in range(round(seconds / DT)):
            self.assertTrue(fdm.run())
            for prop in (
                "position/h-sl-ft", "velocities/vtrue-fps",
                "attitude/theta-rad", "propulsion/engine/engine-rpm",
            ):
                self.assertTrue(math.isfinite(fdm[prop]), prop)

    def test_runtime_xml_parses(self):
        paths = list(ROOT.glob("*.xml"))
        for folder in ("Engines", "Systems"):
            paths.extend((ROOT / folder).rglob("*.xml"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=str(path.relative_to(ROOT))):
                ET.parse(path)

    def test_local_dependencies_and_initial_weight(self):
        fdm = self.load_model()
        # 2530 lb empty + 289.9 lb payload + 222 lb usable fuel.
        self.assertAlmostEqual(fdm["inertia/weight-lbs"], 3041.9, delta=0.01)

    def test_flap_travel(self):
        for command, degrees in ((0.4, 12), (1, 30), (0, 0)):
            with self.subTest(command=command):
                fdm = self.load_model()
                if command == 0:
                    fdm["fcs/flap-cmd-norm"] = 1
                    self.run_for(fdm, 8)
                fdm["fcs/flap-cmd-norm"] = command
                self.run_for(fdm, 8)
                self.assertAlmostEqual(fdm["fcs/flap-pos-deg"], degrees, delta=0.01)

    def test_airborne_gear_cycle(self):
        fdm = self.load_model()
        for command in (1, 0, 1):
            with self.subTest(command=command):
                fdm["gear/gear-cmd-norm"] = command
                self.run_for(fdm, 6)
                self.assertAlmostEqual(fdm["gear/gear-pos-norm"], command, delta=0.001)

    def test_running_engine_integration(self):
        fdm = self.load_model()
        fdm["fcs/mixture-cmd-norm"] = 1
        fdm["fcs/throttle-cmd-norm"] = 0.7
        fdm["fcs/advance-cmd-norm"] = 1
        # Propagate command values into positions before JSBSim's start helper.
        self.assertTrue(fdm.run())
        fdm.get_propulsion().init_running(-1)
        self.run_for(fdm, 10)
        self.assertGreater(fdm["propulsion/engine/engine-rpm"], 500)
        self.assertGreater(fdm["propulsion/engine/power-hp"], 0)


if __name__ == "__main__":
    unittest.main()
