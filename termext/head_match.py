from __future__ import division
import sys

f = open(sys.argv[1])

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
			count_match += 1
	#print line[1], line[2], stat_match, count_gold, count_tag, count_match

print count_match/count_tag
print count_match/count_gold
