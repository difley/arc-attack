import scipy
from accumulator import SampleAccumulator
from basic_api import write_samples_to_file
import itertools


def random_generator():
    while True:
        yield scipy.random.random()


def get_line_distance(generator=None):
    if not generator:
        generator = random_generator()
    minimum_line_distance = 0.3
    line_scale_factor = 1.0
    distance = next(generator)*line_scale_factor + minimum_line_distance
    return distance


def get_arc_radius(generator=None):
    if not generator:
        generator = random_generator()
    minimum_radius = 0.2
    radius_scaling_factor = 0.3
    radius = next(generator)*radius_scaling_factor + minimum_radius
    return radius


def get_central_angle(generator=None):
    if not generator:
        generator = random_generator()
    central_angle = next(generator)*2.*scipy.pi
    return central_angle


def get_boolean(generator=None):
    if not generator:
        generator = random_generator()
    if next(generator) > 0.5:
        return True
    else:
        return False


def get_random_samples(config):
    data_filename = config['data_filename']
    accumulator = SampleAccumulator(config['starting_point'],
                                    config['starting_tangent_angle'],
                                    {'line_sample_count': config['line_sample_count'],
                                     'arc_sample_count': config['arc_sample_count']})
    sample_type_generator = itertools.cycle(('arc', 'line'))
    for counter in range(config['sample_count']):
        sample_type = next(sample_type_generator)
        if sample_type == 'line':
            distance = get_line_distance()
            accumulator.add_sample('line', {'distance': distance})
        elif sample_type == 'arc':
            radius = get_arc_radius()
            central_angle = get_central_angle()
            clockwise = get_boolean()
            accumulator.add_sample('arc', {'radius': radius,
                                           'central_angle': central_angle,
                                           'clockwise': clockwise})
    samples = accumulator.return_samples()
    write_samples_to_file(samples, data_filename)
