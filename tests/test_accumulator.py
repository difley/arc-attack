import unittest
import scipy
from accumulator import SampleAccumulator


class TestSampleAccumulator(unittest.TestCase):
    def test_sample_acculumator(self):
        accumulator = SampleAccumulator({'x': 0.0, 'y': 0.0},
                                         scipy.pi*3./2.,
                                         {'line_sample_count': 2,
                                         'arc_sample_count': 10})
        accumulator.add_sample('line', {'distance': 1.0})
        accumulator.add_sample('arc', {'radius': 1.0,
                                       'central_angle': scipy.pi,
                                       'clockwise': False})
        accumulator.add_sample('line', {'distance': 0.5})
        accumulator.add_sample('arc', {'radius': 0.5,
                                       'central_angle': scipy.pi*5./3.,
                                       'clockwise': True})
        accumulator.add_sample('arc', {'radius': 0.75,
                                       'central_angle': scipy.pi*5./3.,
                                       'clockwise': False})
        samples = accumulator.return_samples()
        final_sample = samples[-1]
        final_point = None
        for final_point in final_sample:
            pass
        self.assertAlmostEqual(final_point['x'], 2.625)
        self.assertAlmostEqual(final_point['y'], -1.582531754)


if __name__ == '__main__':
    unittest.main()
