import scipy
import basic_api


class SampleAccumulator(object):
    def __init__(self, start_point, tangent_angle, config):
        self.__samples = []
        self.__state = {'point': start_point,
                        'angle': tangent_angle}
        self.__config = config


    def add_sample(self, sample_type, parameters):
        allow_intersections = self.__config.get('allow_intersections', True)
        if sample_type == 'line':
            proposed_state = self._line(self.__state['point'], self.__state['angle'],
                                        parameters['distance'])
        elif sample_type == 'arc':
            proposed_state = self._arc(parameters['radius'], parameters['central_angle'],
                                       parameters['clockwise'], self.__state['point'],
                                       self.__state['angle'])
        else:
            raise ValueError("sample_type must be 'line' or 'arc'")
        parametrized_function = proposed_state['function']
        candidate = basic_api.sampler(parametrized_function, 0.0, 1.0,
                                   self.__config['arc_sample_count'])
        if allow_intersections or basic_api.is_sample_acceptable(self.__samples, candidate):
            self.__state = {'angle': proposed_state['angle']}
            self.__state['point'] = parametrized_function(1.0)
            self.__state['sample'] = candidate
            self.__samples.append(self.__state['sample'])
            return True
        return False


    def _line(self, origin, tangent_angle, distance):
        parametrized_function = basic_api.generate_parametrized_line(origin, tangent_angle, distance)
        return {'function': parametrized_function,
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
        tangent_angle = basic_api.normalize_angle(
                      basic_api.get_arc_tangent_angle_from_radial_angle(angles['stop'],
                                                                        clockwise))
        return {'function': parametrized_function,
                'angle': tangent_angle}


    def return_samples(self):
        return self.__samples
