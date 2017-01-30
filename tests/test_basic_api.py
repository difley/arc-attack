import unittest
import basic_api
import scipy


class TestGetArcCenter(unittest.TestCase):
    def test_zero_angle(self):
        center = basic_api.get_arc_center({'x': 1.0, 'y': 0.0}, 1.0, 0.0)
        self.assertAlmostEqual(center['x'], 0.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_angle(self):
        center = basic_api.get_arc_center({'x': 1.0, 'y': 0.0}, 1.0, scipy.pi)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_halves_angle(self):
        center = basic_api.get_arc_center({'x': 0.0, 'y': 1.0}, 1.0, scipy.pi/2.)
        self.assertAlmostEqual(center['x'], 0.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_halves_angle_translated(self):
        center = basic_api.get_arc_center({'x': 2.0, 'y': 1.0}, 1.0, scipy.pi/2.)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_three_halves_pi(self):
        center = basic_api.get_arc_center({'x': 2.0, 'y': 1.0}, 1.0, scipy.pi*3./2.)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 2.0)


class TestGetParametrizedLine(unittest.TestCase):
    def test_vertical_line(self):
        origin = {'x': 0.0, 'y': 0.0}
        tangent_angle = scipy.pi*3./2.
        distance = 1.0
        parametrized_function = basic_api.generate_parametrized_line(origin, tangent_angle, distance)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], 0.0)
        self.assertAlmostEqual(end_point['y'], -1.0)


    def test_horizontal_line(self):
        origin = {'x': 0.0, 'y': 0.0}
        tangent_angle = scipy.pi
        distance = 1.0
        parametrized_function = basic_api.generate_parametrized_line(origin, tangent_angle, distance)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], -1.0)
        self.assertAlmostEqual(end_point['y'], 0.0)


    def test_diagonal_line(self):
        origin = {'x': 0.0, 'y': 0.0}
        tangent_angle = scipy.pi*3./4.
        distance = scipy.sqrt(2.0)
        parametrized_function = basic_api.generate_parametrized_line(origin, tangent_angle, distance)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], -1.0)
        self.assertAlmostEqual(end_point['y'], 1.0)


class TestGetParametrizedArc(unittest.TestCase):
    def test_full_circle(self):
        angles = {'start': 0.0,
                  'stop': scipy.pi*2.}
        radius = 2.0
        center = {'x': 3.0, 'y': -5.0}
        parametrized_function = basic_api.generate_parametrized_arc(center, angles, radius)
        start_point = parametrized_function(0.0)
        self.assertAlmostEqual(start_point['x'], 5.0)
        self.assertAlmostEqual(start_point['y'], -5.0)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], 5.0)
        self.assertAlmostEqual(end_point['y'], -5.0)


    def test_arc_segment(self):
        angles = {'start': 0.0,
                  'stop': scipy.pi/4.}
        radius = scipy.sqrt(2.0)
        center = {'x': 3.0, 'y': -5.0}
        parametrized_function = basic_api.generate_parametrized_arc(center, angles, radius)
        start_point = parametrized_function(0.0)
        self.assertAlmostEqual(start_point['x'], 4.4142135623)
        self.assertAlmostEqual(start_point['y'], -5.0)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], 4.0)
        self.assertAlmostEqual(end_point['y'], -4.0)


    def test_reversed_arc_segment(self):
        angles = {'start': scipy.pi/4.,
                  'stop': 0.0}
        radius = scipy.sqrt(2.0)
        center = {'x': 3.0, 'y': -5.0}
        parametrized_function = basic_api.generate_parametrized_arc(center, angles, radius)
        start_point = parametrized_function(0.0)
        self.assertAlmostEqual(start_point['x'], 4.0)
        self.assertAlmostEqual(start_point['y'], -4.0)
        end_point = parametrized_function(1.0)
        self.assertAlmostEqual(end_point['x'], 4.4142135623)
        self.assertAlmostEqual(end_point['y'], -5.0)


if __name__ == '__main__':
    unittest.main()
