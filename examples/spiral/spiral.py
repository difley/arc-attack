import sys
import scipy
from basic_api import write_samples_to_file
from accumulator import SampleAccumulator


def build_poly(side_count, corner_radius):
    accumulator = SampleAccumulator({'x': 0.0, 'y': 0.0},
                                     0.0,
                                     {'line_sample_count': 2,
                                     'arc_sample_count': 20})
    for counter in range(side_count):
        accumulator.add_sample('arc', {'radius':
        float(corner_radius*float(side_count - counter + 1.)/float(side_count + 1.)),
                                       'central_angle':
                                       scipy.pi*2.*0.05,
                                       'clockwise': True})
    for counter in range(side_count - 1, -1, -1):
        accumulator.add_sample('arc', {'radius':
        float(corner_radius*float(side_count - counter + 1.)/float(side_count + 1.)),
                                       'central_angle':
                                       scipy.pi*2.*0.05,
                                       'clockwise': False})
    samples = accumulator.return_samples()
    write_samples_to_file(samples, 'spiral.out')

if __name__ == '__main__':
    side_count = int(sys.argv[1])
    corner_radius = float(sys.argv[2])
    build_poly(side_count, corner_radius)
