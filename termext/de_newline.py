import sys

if len(sys.argv) < 2:
	f = sys.stdin
else:
	f = open(sys.argv[1])

str = ""

for line in f:
	if line[-1] == "\n":
		str += line[:-1]
	else:
		str += line

print str
