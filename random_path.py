import scipy
from accumulator import SampleAccumulator
from basic_api import write_samples_to_file, is_sample_acceptable
import itertools


def get_line_distance(min_line_distance, max_line_distance):
    line_scale_factor = max_line_distance - min_line_distance
    distance = scipy.random.random()*line_scale_factor + min_line_distance
    return distance


def get_arc_radius(min_radius, max_radius):
    radius_scaling_factor = max_radius - min_radius
    radius = scipy.random.random()*radius_scaling_factor + min_radius
    return radius


def get_central_angle(max_angle_factor=2.):
    central_angle = scipy.random.random()*scipy.pi*max_angle_factor
    return central_angle


def get_random_samples(config):
    data_filename = config['data_filename']
    scipy.random.seed(config['random_seed'])
    accumulator = SampleAccumulator(config['starting_point'],
                                    config['starting_tangent_angle'],
                                    config['arc_sample_count'],
                                    config['allow_intersections'])
    for counter in range(config['sample_count']):
        sample_added = False
        sample_type = scipy.random.choice(config['curve_choices'])
        attempt_count = 0
        while not sample_added and attempt_count < config['attempt_max']:
            attempt_count += 1
            if sample_type == 'line':
                distance = get_line_distance(config['min_line_distance'],
                                             config['max_line_distance'])
                sample_added = accumulator.add_sample('line', {'distance': distance})
            elif sample_type == 'arc':
                radius = get_arc_radius(config['min_radius'],
                                        config['max_radius'])
                central_angle = get_central_angle(config['max_angle_factor'])
                clockwise = scipy.random.choice(config['arc_direction_choices'])
                sample_added = accumulator.add_sample('arc',
                                                      {'radius': radius,
                                                       'central_angle': central_angle,
                                                       'clockwise': clockwise})
    samples = accumulator.return_samples()
    write_samples_to_file(samples, data_filename)
