#!/usr/bin/env bash
set -e
test -d python_env || (python3 -m venv python_env && source python_env/bin/activate && pip install -r requirements.txt && deactivate)
python_env/bin/python -m examples.random_curve_nonoverlapping.main
bash plot.sh random_curve_nonoverlapping
