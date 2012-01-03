import sys
import re

if len(sys.argv) < 2:
    f = sys.stdin
else:
    f = open(sys.argv[1])

for line in f:
    line = line.strip()
    line = re.split("\t", line)
    out = line[0]
    for item in line[1:]:
        if item.startswith("f[0]="):
            out += "\t" + item
        elif not item.startswith("f[") and not item.startswith("POS="):
            out += "\t" + item
    print out

