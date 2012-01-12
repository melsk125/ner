import sys

if len(sys.argv) < 2:
	f = sys.stdin
else:
	f = open(sys.argv[1])

line = f.read()

for c in line[:-1]:
	print c

