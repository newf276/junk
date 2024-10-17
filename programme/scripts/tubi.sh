#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

python3 $(dirname $0)/programme/scripts/tubi.py

echo Done!