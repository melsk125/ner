import sys
import re

if len(sys.argv) < 3:
    exit()

ftpos = open(sys.argv[1])
fgtag = open(sys.argv[2])

for tpos_line in ftpos:
    tpos_line = tpos_line.strip()
    gtag_line = fgtag.readline().strip()
    tpos_line = re.split("\t", tpos_line)
    gtag_line = re.split("\t", gtag_line)
    if len(tpos_line) < 3:
        print
        continue
    print tpos_line[0] + "\t" + tpos_line[1] + "\t" + gtag_line[1]

ftpos.close()
fgtag.close()

