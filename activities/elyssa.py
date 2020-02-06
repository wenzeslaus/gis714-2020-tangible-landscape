#!/usr/bin/env python3
"""
Instructions

- Functions intended to run for each scan
  need to be named run_xxxxx

- Do not modify the parameters of the run_xxx function
  unless you know what you are doing
  see optional parameters:
  https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Running-analyses-and-developing-workflows#python-workflows

- All gs.run_command/read_command/write_command/parse_command
  need to be passed env parameter (..., env=env)
"""

import grass.script as gs


def run_waterflow(scanned_elev, env, **kwargs):
    # first we need to compute x- and y-derivatives
    gs.run_command('r.slope.aspect', elevation=scanned_elev, dx='scan_dx', dy='scan_dy', env=env)
    gs.run_command('r.sim.water', elevation=scanned_elev, dx='scan_dx', dy='scan_dy',
                   rain_value=150, depth='flow', env=env)

# this part is for testing without TL
def main():
    import os

    # we want to run this repetetively without deleted the created files
    os.environ['GRASS_OVERWRITE'] = '1'

    elevation = 'elev_lid792_1m'
    elev_resampled = 'elev_resampled'
    # resampling to have similar resolution as with TL
    gs.run_command('g.region', raster=elevation, res=4, flags='a')
    gs.run_command('r.resamp.stats', input=elevation, output=elev_resampled)

    run_waterflow(scanned_elev = elev_resampled, env = None)
    

if __name__ == '__main__':
    main()
