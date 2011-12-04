import re
import lib
import sys
import itertools
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-l", action="store_true", dest="lowercase", default=False, help="force lowercase")

parser.add_option("-w", action="store_true", dest="byword", default=False, help="calculate by word")

parser.add_option("-m", type="int", dest="max_dist", default=5, help="maxmimum distance")

options, args = parser.parse_args()

lowercase = options.lowercase
byword = options.byword
max_dist = options.max_dist

if lowercase:
    sys.stderr.write("Lowercase\n")
else:
    sys.stderr.write("Not lowercase\n")

if byword:
    sys.stderr.write("By word\n")
else:
    sys.stderr.write("By phrase\n")

sys.stderr.write("Max dist: " + str(max_dist) + "\n")

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat(raw)
lines = [line[2] for line in lines]

if lowercase:
    lines = [line.lower() for line in lines]

if byword:
    lines = lib.collapse([line.split() for line in lines])

wordset = set(lines)

sys.stderr.write(str(len(wordset)) + "\n")

allcount = 0
scount = 0
for str1, str2 in itertools.combinations(wordset, 2):
    if allcount%10000 == 0:
        sys.stderr.write("allcount: " + str(allcount) + "\n")
        sys.stderr.write("  scount: " + str(scount) + "\n")
    allcount += 1
    dist = lib.levenshtein(str1, str2)
    if dist <= max_dist:
        scount += 1
        print str(dist) + "\t" + str1 + "\t" + str2




