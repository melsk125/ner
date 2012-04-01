from __future__ import division
import sys

args = sys.argv[1:]

if len(args) < 2:
    sys.stderr.write("usage: python " + sys.argv[0] + " (gold) (test)\n")
    exit(1)

fgold = open(args[0])
ftest = open(args[1])

gm = 0
gn = 0

tm = 0
tn = 0

mm = 0
mn = 0

for lgold in fgold:
    lgold = lgold.strip()
    ltest = ftest.readline()
    ltest = ltest.strip()
    if lgold == "MODEL":
        gm += 1
    else:
        gn += 1
    if ltest == "MODEL":
        tm += 1
    else:
        tn += 1
    if lgold == ltest:
        if lgold == "MODEL":
            mm += 1
        else:
            mn += 1

pm = mm/tm
rm = mm/gm
fm = 2*pm*rm/(pm+rm)

pn = mn/tn
rn = mn/gn
fn = 2*pn*rn/(pn+rn)

print "Model"
print "  Precision:", pm
print "  Recall:   ", rm
print "  F1:       ", fm
print
print "NP"
print "  Precision:", pn
print "  Recall:   ", rn
print "  F1:       ", fn


