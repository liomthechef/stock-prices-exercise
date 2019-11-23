#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

. venv/bin/activate
flake8 --exclude=venv* --statistics
pytest -v