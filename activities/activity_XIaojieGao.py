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

def run_example(scanned_elev, env, **kwargs):
    gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope',
                        format='percent', env=env)
    # reclassify using rules passed as a string to standard input
    # 0:2:1 means reclassify interval 0 to 2 percent of slope to category 1 
    rules = ['0:2:1', '2:5:2', '5:8:3', '8:15:4', '15:30:5', '30:*:6']
    gs.write_command('r.recode', input='slope', output='slope_class',
                          rules='-', stdin='\n'.join(rules), env=env)
    # set new color table: green - yellow - red
    gs.run_command('r.colors', map='slope_class', color='gyr', env=env)

def run_curvatures(scanned_elev, env, **kwargs):
    gs.run_command('r.param.scale', input=scanned_elev, output='profile_curv',
                   method='profc', size=11, env=env)
    gs.run_command('r.param.scale', input=scanned_elev, output='tangential_curv',
                   method='crosc', size=11, env=env)
    gs.run_command('r.colors', map=['profile_curv', 'tangential_curv'], color='curvature', env=env)

def run_slope(scanned_elev, env, **kwargs):
    gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope', env=env)


def run_contours(scanned_elev, env, **kwargs):
    interval = 5
    gs.run_command('r.contour', input=scanned_elev, output='contours', step=interval, flags='t', env=env)

def run_function_with_points(scanned_elev, env, points=None, **kwargs):
    if not points:
        points = 'points'
        import analyses
        analyses.change_detection('scan_saved', scanned_elev, points,
                                  height_threshold=[10, 100], cells_threshold=[5, 50],
                                  add=True, max_detected=5, debug=True, env=env)
    # read coordinates into a list
    point_list = []
    data = gs.read_command('v.out.ascii', input=points, type='point',
                           format='point', separator='comma', env=env).strip().splitlines()
    for point in data:
        point_list.append([float(p) for p in point.split(',')])


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

    # this will run all 3 examples (slope, contours, points)
    # run_slope(scanned_elev=elev_resampled, env=None)
    # run_contours(scanned_elev=elev_resampled, env=None)

    # create points
    points = 'points'
    gs.write_command('v.in.ascii', flags='t', input='-', output=points, separator='comma',
                     stdin='638432,220382\n638621,220607')
    # run_function_with_points(scanned_elev=elev_resampled, env=None, points=points)
    run_example(scanned_elev=elev_resampled, env=None)
    run_curvatures(scanned_elev=elev_resampled, env=None)

if __name__ == '__main__':
    main()

