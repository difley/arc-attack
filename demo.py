import scipy
from arc_attack import write_samples_to_file
from api import sample_accumulator


def main():
    data_filename = 'output.out'
    accumulator = sample_accumulator({'x': 0.0, 'y': 0.0},
                                      scipy.pi*3./2.,
                                      {'line_sample_count': 2,
                                       'arc_sample_count': 10})
    accumulator['add_sample']('line', {'distance': 1.0})
    accumulator['add_sample']('arc', {'radius': 1.0,
                                   'central_angle': scipy.pi,
                                   'clockwise': False})
    accumulator['add_sample']('line', {'distance': 0.5})
    accumulator['add_sample']('arc', {'radius': 0.5,
                                   'central_angle': scipy.pi*5./3.,
                                   'clockwise': True})
    accumulator['add_sample']('arc', {'radius': 0.75,
                                   'central_angle': scipy.pi*5./3.,
                                   'clockwise': False})
    samples = accumulator['return_samples']()
    write_samples_to_file(samples, data_filename)


if __name__ == '__main__':
    main()
