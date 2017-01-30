#!/usr/bin/env bash
set -e
test -d python_env || (python3 -m venv python_env && source python_env/bin/activate && pip install -r requirements.txt && deactivate)
random_seed=$1
python_env/bin/python main.py "${random_seed}"
gnuplot < plot_output.gnuplot
