#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

python3 -m pip install bs4

from bs4 import BeautifulSoup as bs

python3 $(dirname $0)/scripts/tubi.py

echo Done!
