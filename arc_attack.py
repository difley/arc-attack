#!/usr/bin/env python3
import scipy
import sys


def curve_generator():
    iteration_count = 100
    state = {'x_center': 0.,
             'y_center': 0.,
             'direction': 1,
             'start_angle': 0.,
             'end_angle': 9.*scipy.pi/5.,
             'radius': scipy.random.random(),
             'distance': 1.}
    for iteration in range(iteration_count):
        yield generate_points_along_arc(state)
        yield generate_points_along_line(state)
        state.update(compute_line_segment_end(state))
        state.update(compute_next_arc(state))
        state.update(compute_next_line())


def normalize_angle(angle):
    """put angle in the range 0 to 2*pi"""
    normalized_angle = scipy.fmod(angle, 2.*scipy.pi)
    if normalized_angle < 0.:
        normalized_angle += 2.*scipy.pi
    return normalized_angle


def get_random_plus_or_minus_one():
    return scipy.random.randint(2)*2 - 1


def compute_random_radius():
    minimum_radius = 0.2
    radius_scaling_factor = 0.3
    radius = scipy.random.random()*radius_scaling_factor + minimum_radius
    return radius


def compute_point_on_circle(x_center, y_center, radius, angle, y_radius_sign=1.):
    x_coordinate = x_center + radius*scipy.cos(angle)
    y_coordinate = y_center + y_radius_sign*radius*scipy.sin(angle)
    return x_coordinate, y_coordinate


def compute_next_arc(state):
    sign = get_random_plus_or_minus_one()
    direction = -state['direction']*sign
    if (sign == 1):
        angle_start = state['end_angle'] + scipy.pi
    else:
        angle_start = state['end_angle']
    angle_start = normalize_angle(angle_start)
    old_radius = state['radius']
    new_radius = compute_random_radius()
    new_x_center, new_y_center = compute_point_on_circle(state['x_center'],
                                                         state['y_center'],
                                                         sign*new_radius + old_radius,
                                                         state['end_angle'])
    angle_end = angle_start + scipy.random.random()*2.*scipy.pi
    return {'x_center': new_x_center,
            'y_center': new_y_center,
            'radius': new_radius,
            'direction': direction,
            'start_angle': angle_start,
            'end_angle': angle_end}


def compute_directed_angle(state):
    directed_angle = state['end_angle'] - state['start_angle']
    if ((state['direction'] == -1) and (state['start_angle'] < state['end_angle'])):
        directed_angle -= 2.*scipy.pi
    return directed_angle


def generate_points_along_arc(state, point_density=3):
    directed_angle = compute_directed_angle(state)
    point_count = int(abs(directed_angle)*point_density)
    for counter in range(point_count):
        angle = (directed_angle*float(counter)/float(point_count) + state['start_angle'])
        x_coordinate, y_coordinate = compute_point_on_circle(state['x_center'],
                                                             state['y_center'],
                                                             state['radius'],
                                                             angle)
        yield x_coordinate, y_coordinate


def compute_next_line():
    minimum_line_distance = 0.3
    line_scale_factor = 1.0
    line_distance = scipy.random.random()*line_scale_factor + minimum_line_distance
    return {'distance': line_distance}


def line(state, point_density=4):
    start_x, start_y = compute_point_on_circle(state['x_center'],
                                               state['y_center'],
                                               state['radius'],
                                               state['end_angle'])
    yield generate_points_along_line(state, point_density, start_x, start_y)


def compute_line_segment_end(state):
    end_y, end_x = compute_point_on_circle(state['y_center'],
                                           state['x_center'],
                                           state['direction']*state['distance'],
                                           state['end_angle'],
                                           y_radius_sign=-1.)
    return {'x_center': end_x,
            'y_center': end_y}


def generate_points_along_line(state, point_density=4):
    start_x, start_y = compute_point_on_circle(state['x_center'],
                                               state['y_center'],
                                               state['radius'],
                                               state['end_angle'])
    point_count = int(state['distance']*point_density)
    for counter in range(point_count):
        iteration_scale_factor = state['direction']*state['distance']*float(counter)/float(point_count)
        y_coordinate, x_coordinate = compute_point_on_circle(start_y,
                                                             start_x,
                                                             iteration_scale_factor,
                                                             state['end_angle'],
                                                             y_radius_sign=-1.)
        yield x_coordinate, y_coordinate


def print_coordinate_pair(x_coordinate, y_coordinate):
    print("{x_coordinate} {y_coordinate}".format(
        x_coordinate=x_coordinate,
        y_coordinate=y_coordinate
    ))


def set_seed_from_argv_or_default():
    if (sys.argv[1]).isdigit():
        seed = int(sys.argv[1])
    else:
        seed = 4455582
    scipy.random.seed(seed);


def main():
    set_seed_from_argv_or_default()
    for curve_segment in curve_generator():
        for x_coordinate, y_coordinate in curve_segment:
            print_coordinate_pair(x_coordinate, y_coordinate)


if __name__ == '__main__':
    main()
