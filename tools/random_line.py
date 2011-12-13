import sys
import random
from optparse import OptionParser

optionParser = OptionParser()

optionParser.add_option("-s", action="store_true", dest="sort", default=False, help="sort")

options, args = optionParser.parse_args()

sort = options.sort

fn = args[0]
lc = int(args[1])

f = open(fn)
lines = f.readlines()

sys.stderr.write("Sample from " + fn + " with " + str(len(lines)) + " lines\n")
sys.stderr.write("Take " + str(lc) + " samples\n")

random.seed()

lnum = random.sample(range(len(lines)), lc)
if sort:
    lnum = sorted(lnum)
for ln in lnum:
    sys.stdout.write(lines[ln])
