#!/bin/bash
set -e
test -d ../../python_env || (python3 -m venv ../../python_env && source ../../python_env/bin/activate && pip install -r requirements.txt && deactivate)
export PYTHONPATH='../../../arc_attack'
../../python_env/bin/python polygon.py 5 0.2
bash ../../plot.sh polygon
