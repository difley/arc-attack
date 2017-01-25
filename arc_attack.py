#!/usr/bin/env python3
import scipy
import sys


def curve_generator():
    iteration_count = 20
    state = {'x_center': 0.,
             'y_center': 0.,
             'direction': 1,
             'start_angle': 0.,
             'end_angle': 9.*scipy.pi/5.,
             'radius': scipy.random.random(),
             'distance': 1.}
    for j in range(iteration_count):
        arc(state)
        state.update(line(state))
        dist = compute_next_line()
        state.update(compute_next_arc(state))


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
    radius_scaling_factor = 0.2
    radius = scipy.random.random()*radius_scaling_factor + minimum_radius
    return radius


def compute_next_arc(state):
        #sign randomly is 1 or -1.  if sign == 1,
        #next circle's center is on convex side of
        #current circle, else next center is
        #on concave side of current circle
        sign = get_random_plus_or_minus_one()
        direction = -state['direction']*sign
        #new start_angle is on opposite side of circle from previous start_angle
        if (sign == 1):
            angle_start = state['end_angle'] + scipy.pi
        else:
            angle_start = state['end_angle']
        angle_start = normalize_angle(angle_start)
        old_radius = state['radius']
        new_radius = compute_random_radius()
        new_x_center = state['x_center'] + (sign*new_radius + old_radius)*scipy.cos(state['end_angle'])
        new_y_center = state['y_center'] + (sign*new_radius + old_radius)*scipy.sin(state['end_angle'])
        angle_end = angle_start + scipy.random.random()*2.*scipy.pi
        return {'x_center': new_x_center,
                'y_center': new_y_center,
                'radius': new_radius,
                'direction': direction,
                'start_angle': angle_start,
                'end_angle': angle_end}


#return arc points specified by present state
#precondition: if direction != -1 (clockwise arc),
#then thetai < thetaf.
#postcondition: direction==-1 for a clockwise arc,
#else anti-clockwise arc is produced.
def arc(state, point_density=3):
    directed_angle = compute_directed_angle(state)
    generate_points_along_arc(state, point_density, directed_angle)


def compute_directed_angle(state):
    directed_angle = state['end_angle'] - state['start_angle']
    if ((state['direction'] == -1) and
        (state['start_angle'] < state['end_angle'])):
        directed_angle -= 2.*scipy.pi
    return directed_angle


def generate_points_along_arc(state, point_density, tf):
    np = int(abs(tf)*point_density)
    for i in range(np):
        ang = (tf*float(i)/float(np) + state['start_angle'])
        print("{x_coordinate} {y_coordinate}".format(
                x_coordinate=state['radius']*scipy.cos(ang) + state['x_center'],
                y_coordinate=state['radius']*scipy.sin(ang) + state['y_center']))


def compute_next_line():
    minimum_line_distance = 0.3
    line_scale_factor = 1.0
    return scipy.random.random()*line_scale_factor + minimum_line_distance


def line(state, point_density=4):
    start_x = state['radius']*scipy.cos(state['end_angle']) + state['x_center']
    start_y = state['radius']*scipy.sin(state['end_angle']) + state['y_center']
    generate_points_along_line(state, point_density, start_x, start_y)
    return {'x_center': state['x_center'] -
            state['direction']*state['distance']*scipy.sin(state['end_angle']),
            'y_center': state['y_center'] +
            state['direction']*state['distance']*scipy.cos(state['end_angle'])}


def generate_points_along_line(state, point_density, start_x, start_y):
    np = int(state['distance']*point_density)
    for i in range(np):
        iteration_scale_factor = state['direction']*state['distance']*float(i)/float(np)
        print("{x_coordinate} {y_coordinate}".format(
            x_coordinate=start_x - iteration_scale_factor*scipy.sin(state['end_angle']),
            y_coordinate=start_y + iteration_scale_factor*scipy.cos(state['end_angle'])))


def main():
    scipy.random.seed(int(sys.argv[1]));
    curve_generator()


if __name__ == '__main__':
    main()
