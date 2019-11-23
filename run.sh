#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

cd "$(dirname "$0")"
export PYTHONPATH=$PYTHONPATH:pwd

python3 stocks.py