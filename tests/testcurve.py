import unittest
import curve
import scipy


class TestGetArcCenter(unittest.TestCase):
    def test_zero_angle(self):
        center = curve.get_arc_center({'x': 1.0, 'y': 0.0}, 1.0, 0.0)
        self.assertAlmostEqual(center['x'], 0.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_angle(self):
        center = curve.get_arc_center({'x': 1.0, 'y': 0.0}, 1.0, scipy.pi)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_halves_angle(self):
        center = curve.get_arc_center({'x': 0.0, 'y': 1.0}, 1.0, scipy.pi/2.)
        self.assertAlmostEqual(center['x'], 0.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_pi_halves_angle_translated(self):
        center = curve.get_arc_center({'x': 2.0, 'y': 1.0}, 1.0, scipy.pi/2.)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 0.0)


    def test_three_halves_pi(self):
        center = curve.get_arc_center({'x': 2.0, 'y': 1.0}, 1.0, scipy.pi*3./2.)
        self.assertAlmostEqual(center['x'], 2.0)
        self.assertAlmostEqual(center['y'], 2.0)


if __name__ == '__main__':
    unittest.main()
