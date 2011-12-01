#!/bin/bash

grep -v '^[1-4]	' $1 > tmp2	# Get only lines starting with number more than 5

python ../../corresponding.je.py tmp2 > raw2
							# Get corresponding word list
  cut -f 3- raw2 |				# Get from the third column
  sed 's|[^	]||g' |
  sed 's|	|x|g' |
  sed 's|^|x|g' |
  sort |
  uniq -c

rm tmp2
