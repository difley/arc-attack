import scipy
import curve


def main():
    samples = []
    origin = {'x': 0.0, 'y': 0.0}
    tangent_angle = scipy.pi*3./2.
    distance = 1.0
    parametrized_function = curve.generate_parametrized_line(origin, tangent_angle, distance)
    samples.append(curve.sampler(parametrized_function, 0.0, 1.0, 1))
    point = parametrized_function(1.0)
    radius = 1.0
    radial_angle = curve.normalize_angle(curve.get_radial_angle_from_arc_tangent(tangent_angle,
                                                              clockwise=False))
    center = curve.get_arc_center(point, radius, radial_angle)
    angles = {'start': radial_angle,
              'stop': radial_angle + scipy.pi}
    arc_function = curve.generate_parametrized_arc(center, angles, radius)
    samples.append(curve.sampler(arc_function, 0.0, 1.0, 10))
    tangent_angle = curve.normalize_angle(curve.get_arc_tangent_angle_from_radial_angle(angles['stop']))
    origin = arc_function(1.0)
    distance = 0.5
    parametrized_function = curve.generate_parametrized_line(origin, tangent_angle, distance)
    samples.append(curve.sampler(parametrized_function, 0.0, 1.0, 2))
    radial_angle = curve.normalize_angle(curve.get_radial_angle_from_arc_tangent(tangent_angle,
                                                              clockwise=True))
    radius = 0.5
    point = parametrized_function(1.0)
    center = curve.get_arc_center(point, radius, radial_angle)
    angles = {'start': radial_angle,
              'stop': radial_angle - scipy.pi*5./3.}
    arc_function = curve.generate_parametrized_arc(center, angles, radius)
    samples.append(curve.sampler(arc_function, 0.0, 1.0, 10))
    radius = 0.75
    point = arc_function(1.0)
    tangent_angle = curve.normalize_angle(
                         curve.get_arc_tangent_angle_from_radial_angle(angles['stop'],
                                                           clockwise=True))
    radial_angle = curve.normalize_angle(
                        curve.get_radial_angle_from_arc_tangent(tangent_angle,
                                                     clockwise=False))
    center = curve.get_arc_center(point, radius, radial_angle)
    angles = {'start': radial_angle,
              'stop': radial_angle + scipy.pi*5./3.}
    arc_function = curve.generate_parametrized_arc(center, angles, radius)
    samples.append(curve.sampler(arc_function, 0.0, 1.0, 10))
    curve.write_samples_to_file(samples, 'output.out')


if __name__ == '__main__':
    main()
