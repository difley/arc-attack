import sys
import scipy
from basic_api import write_samples_to_file
from accumulator import SampleAccumulator


def build_wavy(side_count):
    accumulator = SampleAccumulator({'x': 0.0, 'y': 0.0},
                                     0.0,
                                     arc_sample_count=20)
    for counter in range(side_count):
        accumulator.add_sample('line', {'distance': 0.25/8.})
        for line_counter in range(6):
            accumulator.add_sample('arc', {'radius': 0.25/8.,
                                           'central_angle':
                                           scipy.pi,
                                           'clockwise': True})
            accumulator.add_sample('arc', {'radius': 0.25/8.,
                                           'central_angle':
                                           scipy.pi,
                                           'clockwise': False})
            accumulator.add_sample('line', {'distance': 0.25/8.})
        accumulator.add_sample('arc', {'radius': 0.2,
                                       'central_angle':
                                       scipy.pi*2.*(side_count - 1.)/side_count,
                                       'clockwise': True})
    samples = accumulator.return_samples()
    write_samples_to_file(samples, 'wavy_polygon.out')

if __name__ == '__main__':
    side_count = int(sys.argv[1])
    build_wavy(side_count)
