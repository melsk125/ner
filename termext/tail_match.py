from __future__ import division
import sys

f = open(sys.argv[1])

in_gold = False
in_tag = False

stat_match = False

count_gold = 0
count_tag = 0

count_match = 0


for line in f:
	line = line.split()
	if line[1] == "B":
		count_gold += 1
	if line[2] == "B":
		count_tag += 1
	if line[1] == line[2]:
		if line[1] == "B":
			stat_match = True
			count_match += 1
		elif line[1] == "O":
			stat_match = False
	else:
		if stat_match:
			stat_match = False
			count_match -= 1
	#print line[1], line[2], stat_match, count_gold, count_tag, count_match

print count_match/count_tag
print count_match/count_gold
