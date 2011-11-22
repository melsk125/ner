import re
import sys

f = open(sys.argv[1])
raw = f.read()
lines = re.split('\n', raw)[:-1]
lines = [re.split('\t', line) for line in lines]
entries = [line[4+int(line[2]):4+int(line[2])+int(line[3])] for line in lines]

#print lines[0]
#print entries[0]

list = []
for entry in entries:
	list.extend(entry)

set = set(list)
#print set

dict = dict([(el, 0) for el in set])
#print dict

for node in list:
	dict[node] += 1

for word in sorted(dict):
	print word + '\t' + str(dict[word])
