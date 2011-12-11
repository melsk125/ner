import sys
import random

fn = sys.argv[1]
lc = int(sys.argv[2])

f = open(fn)
lines = f.readlines()

sys.stderr.write("Sample from " + fn + " with " + str(len(lines)) + " lines\n")
sys.stderr.write("Take " + str(lc) + " samples\n")

random.seed()

lnum = sorted(random.sample(range(len(lines)), lc))
for ln in lnum:
    print lines[ln]
