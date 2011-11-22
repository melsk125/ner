import re
import sys
import lib

f = open(sys.argv[1])
raw = f.read()
lines = re.split('\n', raw)[:-1]
lines = [re.split('\t', line) for line in lines]
entries = [line[4+int(line[2]):4+int(line[2])+int(line[3])] for line in lines]

list = lib.collapse(entries)

list = [phrase.split() for phrase in list]

list = lib.collapse(list)

s = set(list)

d = dict([(el, 0) for el in s])

for node in list:
	d[node] += 1

for word in sorted(d):
	print word + '\t' + str(d[word])
