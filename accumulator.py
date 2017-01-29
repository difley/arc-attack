import scipy
import basic_api


class SampleAccumulator(object):
    def __init__(self, original_start_point, original_tangent_angle, config):
        self.samples = []
        self.state = {'point': original_start_point,
                      'angle': original_tangent_angle}
        self.config = config


    def add_sample(self, sample_type, parameters):
        if sample_type == 'line':
            self.state = self._line(self.state['point'], self.state['angle'],
                                    parameters['distance'])
        elif sample_type == 'arc':
            self.state = self._arc(parameters['radius'], parameters['central_angle'],
                                   parameters['clockwise'], self.state['point'],
                                   self.state['angle'])


    def _line(self, origin, tangent_angle, distance):
        parametrized_function = basic_api.generate_parametrized_line(origin, tangent_angle, distance)
        self.samples.append(basic_api.sampler(parametrized_function, 0.0, 1.0,
                                     self.config['line_sample_count']))
        end_point = parametrized_function(1.0)
        return {'point': end_point,
                'angle': tangent_angle}


    def _arc(self, radius, central_angle, clockwise,
                      start_point, start_tangent_angle):
        start_angle = basic_api.normalize_angle(
                          basic_api.get_radial_angle_from_arc_tangent(start_tangent_angle,
                                                                  clockwise))
        if not clockwise:
            stop_angle = start_angle + central_angle
        else:
            stop_angle = start_angle - central_angle
        angles = {'start': start_angle,
                  'stop': stop_angle}
        center = basic_api.get_arc_center(start_point, radius, start_angle)
        parametrized_function = basic_api.generate_parametrized_arc(center, angles, radius)
        self.samples.append(basic_api.sampler(parametrized_function, 0.0, 1.0,
                                     self.config['arc_sample_count']))
        end_point = parametrized_function(1.0)
        tangent_angle = basic_api.normalize_angle(
                      basic_api.get_arc_tangent_angle_from_radial_angle(angles['stop'],
                                                                    clockwise))
        return {'point': end_point,
                'angle': tangent_angle}


    def return_samples(self):
        return self.samples
