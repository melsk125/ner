#!/bin/bash

grep -e '^[0-9]' $1 |		# Get only lines starting with number
  grep -v '^[1-4]	' > tmp	# Get only lines starting with number more than 5

python ../../corresponding.je.py tmp > raw
							# Get corresponding word list
  cut -f 3- raw |				# Get from the third column
  sed 's|[^	]||g' |
  sed 's|	|x|g' |
  sed 's|^|x|g' |
  sort |
  uniq -c

rm tmp
