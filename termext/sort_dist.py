import lib
import sys
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-n", action="store_true", dest="normalized", default=False, help="sort by normalized distance")

options, args = parser.parse_args()

normalized = options.normalized

if normalized:
    sys.stderr.write("Sort by normalized distance\n")
else:
    sys.stderr.write("Sort by distance\n")

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat(raw)
lines = [line for line in lines if len(line) == 4]

if normalized:
    lines = [[float(line[3]), line[0], line[1]] for line in lines]
else:
    lines = [[int(line[2]), line[0], line[1]] for line in lines]

for line in sorted(lines, key=lambda l:l[0]):
    print line[1] + "\t" + line[2] + "\t" + str(line[0])
