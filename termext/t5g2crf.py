import lib
import sys
import re

if len(sys.argv) < 3:
    exit()

ft5 = open(sys.argv[1])
fgcrf = open(sys.argv[2])

for t5_line in ft5:
    t5_line = t5_line.strip()
    gcrf_line = fgcrf.readline().strip()
    t5_line = re.split("\t", t5_line)
    gcrf_line = re.split("\t", gcrf_line)
    out = gcrf_line[0]
    for item in gcrf_line[1:]:
        out += "\t" + item
    for item in t5_line[1:]:
        if item.startswith("POS=") or item.startswith("f[01]="):
            continue
        out += "\t" + item
    print out

ft5.close()
fgcrf.close()

