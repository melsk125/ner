import re
import sys
import lib

f = open(sys.argv[1])
raw = f.read()

lines = lib.get_dat(raw)
list = lib.get_eterms(lines)

list = [entry.lower() for entry in list]
list = [entry.split() for entry in list]

list = lib.collapse(list)

s = set(list)

d = dict([(el, 0) for el in s])

for entry in list:
	d[entry] += 1

for word, a in sorted(d.items(), key=lambda entry: entry[1], reverse=True):
	print word + '\t' + str(a)
