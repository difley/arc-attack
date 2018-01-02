import sys
import scipy
from basic_api import write_samples_to_file
from accumulator import SampleAccumulator


def build_poly(side_count, corner_radius):
    accumulator = SampleAccumulator({'x': 0.0, 'y': 0.0},
                                     0.0,
                                     arc_sample_count=20)
    for counter in range(side_count):
        accumulator.add_sample('line', {'distance': 1.})
        accumulator.add_sample('arc', {'radius': float(corner_radius),
                                       'central_angle':
                                       scipy.pi*2.*(side_count - 1.)/side_count,
                                       'clockwise': True})
    samples = accumulator.return_samples()
    write_samples_to_file(samples, 'polygon.out')

if __name__ == '__main__':
    side_count = int(sys.argv[1])
    corner_radius = float(sys.argv[2])
    build_poly(side_count, corner_radius)
