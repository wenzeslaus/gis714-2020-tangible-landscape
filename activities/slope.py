#!/usr/bin/env python3

import grass.script as gs


def run_slope(scanned_elev, env, **kwargs):
    gs.run_command("r.slope.aspect", elevation=scanned_elev, slope="slope", env=env)


if __name__ == "__main__":
    elevation = "elev_lid792_1m"
    env = None
    run_slope(scanned_elev=elevation, env=env)
