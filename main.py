import config
import random_path
import scipy
import sys


def set_seed_from_argv_or_default():
    if (len(sys.argv) == 2) and (sys.argv[1]).isdigit():
        seed = int(sys.argv[1])
    else:
        seed = 43
    scipy.random.seed(seed);


if __name__ == '__main__':
   set_seed_from_argv_or_default()
   random_path.get_random_samples(config.config)
