#!/bin/bash

set -x

grep -e '^[0-9]' $1 |		# Get only lines starting with number
grep -v '^[1-4]	' |	# Get only lines starting with number more than 5

python corresponding.je.py
