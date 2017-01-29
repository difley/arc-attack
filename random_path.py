import scipy


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


def get_angle_end(angle, generator=None):
    if not generator:
        generator = random_generator()
    angle_end = angle + next(generator)*2.*scipy.pi
    return angle_end
