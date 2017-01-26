#!/usr/bin/env bash
set -e
test -d python_env || python3 -m venv python_env && source python_env/bin/activate && pip install -r requirements.txt && deactivate
python_env/bin/python arc_attack.py 95832495 > output.out
gnuplot < plot_output.gnuplot
