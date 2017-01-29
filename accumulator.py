import scipy
import arc_attack as curve


def sample_accumulator(original_start_point, original_tangent_angle, config):
    samples = []
    state = {'point': original_start_point,
             'angle': original_tangent_angle}

    def add_sample(sample_type, parameters):
        nonlocal state
        if sample_type == 'line':
            state = line(state['point'], state['angle'],
                         parameters['distance'])
        elif sample_type == 'arc':
            state = arc(parameters['radius'], parameters['central_angle'],
                        parameters['clockwise'], state['point'],
                        state['angle'])

    def line(origin, tangent_angle, distance):
        parametrized_function = curve.generate_parametrized_line(origin, tangent_angle, distance)
        samples.append(curve.sampler(parametrized_function, 0.0, 1.0,
                                     config['line_sample_count']))
        end_point = parametrized_function(1.0)
        return {'point': end_point,
                'angle': tangent_angle}

    def arc(radius, central_angle, clockwise,
                      start_point, start_tangent_angle):
        start_angle = curve.normalize_angle(
                          curve.get_radial_angle_from_arc_tangent(start_tangent_angle,
                                                                  clockwise))
        if not clockwise:
            stop_angle = start_angle + central_angle
        else:
            stop_angle = start_angle - central_angle
        angles = {'start': start_angle,
                  'stop': stop_angle}
        center = curve.get_arc_center(start_point, radius, start_angle)
        parametrized_function = curve.generate_parametrized_arc(center, angles, radius)
        samples.append(curve.sampler(parametrized_function, 0.0, 1.0,
                                     config['arc_sample_count']))
        end_point = parametrized_function(1.0)
        tangent_angle = curve.normalize_angle(
                      curve.get_arc_tangent_angle_from_radial_angle(angles['stop'],
                                                                    clockwise))
        return {'point': end_point,
                'angle': tangent_angle}



    def return_samples():
        return samples

    return {'add_sample': add_sample,
            'return_samples': return_samples}
