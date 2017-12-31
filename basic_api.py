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


def determinant(point_a, point_b, point_c):
    return ((point_b['x'] - point_a['x'])*(point_c['y'] - point_a['y'])
            - (point_b['y'] - point_a['y'])*(point_c['x'] - point_a['x']))


#Does the line that passes through point_a and point_b intersect with
#the line that passes through point_c and point_d?
def is_intersection(point_a, point_b, point_c, point_d):
    det_abc = determinant(point_a, point_b, point_c)
    det_abd = determinant(point_a, point_b, point_d)
    if det_abc*det_abd > 0.:
        return False
    det_cda = determinant(point_c, point_d, point_a)
    det_cdb = determinant(point_c, point_d, point_b)
    if det_cda*det_cdb > 0.:
        return False
    return True


def get_first_last_points(sample):
    if len(sample) < 2:
        raise ValueError
    return sample[0], sample[-1]


def get_consecutive_points_from_sample(sample):
    if len(sample) < 2:
        raise ValueError
    for i in range(len(sample) - 1):
        yield sample[i], sample[i + 1]


def is_sample_acceptable(samples, candidate):
    if len(samples) < 2:
        return True
    point_c, point_d = get_first_last_points(candidate)
    #do not compare samples[:-1] to candidate because
    #consecutive samples will intersect by construction
    for sample in samples[:-1]:
        for point_a, point_b in get_consecutive_points_from_sample(sample):
            if is_intersection(point_a, point_b,
                               point_c, point_d):
                return False
    return True


def sampler(parametrized_function, start_t, stop_t, point_count):
    return list(map(lambda t: parametrized_function(t),
               scipy.linspace(start_t, stop_t, point_count)))


def write_samples_to_file(samples, filename):
    with open(filename, 'w') as file_handle:
        for sample in samples:
            for point in sample:
                file_handle.write('{x} {y}\n'.format(x=point['x'],
                                                     y=point['y']))
