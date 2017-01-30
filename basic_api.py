import scipy


def generate_parametrized_line(origin, angle, distance):
    def parametrized_line(t):
        x = origin['x'] + distance*scipy.cos(angle)*t
        y = origin['y'] + distance*scipy.sin(angle)*t
        return {'x': x, 'y': y}
    return parametrized_line


def generate_parametrized_arc(center, angles, radius):
    angle_delta = angles['stop'] - angles['start']
    def parametrized_arc(t):
        effective_angle = angle_delta*t + angles['start']
        x = center['x'] + radius*scipy.cos(effective_angle)
        y = center['y'] + radius*scipy.sin(effective_angle)
        return {'x': x, 'y': y}
    return parametrized_arc


def get_arc_center(point, radius, angle):
    center_x = point['x'] - radius*scipy.cos(angle)
    center_y = point['y'] - radius*scipy.sin(angle)
    return {'x': center_x,
            'y': center_y}


def get_radial_angle_from_arc_tangent(tangent_angle, clockwise=False):
    if clockwise:
        angle = tangent_angle + scipy.pi/2.
    else:
        angle = tangent_angle - scipy.pi/2.
    return angle


def get_arc_tangent_angle_from_radial_angle(radial_angle, clockwise=False):
    if clockwise:
        angle = radial_angle - scipy.pi/2.
    else:
        angle = radial_angle + scipy.pi/2.
    return angle


def normalize_angle(angle):
    return scipy.fmod(angle, scipy.pi*2.)


def sampler(parametrized_function, start_t, stop_t, point_count):
    return map(lambda t: parametrized_function(t),
               scipy.linspace(start_t, stop_t, point_count))


def write_samples_to_file(samples, filename):
    with open(filename, 'w') as file_handle:
        for sample in samples:
            for point in sample:
                file_handle.write('{x} {y}\n'.format(x=point['x'],
                                                    y=point['y']))