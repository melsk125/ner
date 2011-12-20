import lib
import sys
import re

from optparse import OptionParser

args = sys.argv[1:]

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat(raw)

n = len(lines)

for i in range(n):
    if lines[i] == [""]:
        print
        continue
    feats = ["" for slot in range(19)]
    feats[2] = "w[t]=" + lines[i][0]
    feats[9] = "pos[t]=" + lines[i][1]
    isBOS = False
    isEOS = False
    if i >= 1 and lines[i-1] != [""]:
        feats[1] = "w[t-1]=" + lines[i-1][0]
        feats[8] = "pos[t-1]=" + lines[i-1][1]
        feats[5] = "w[t-1]|w[t]=" + lines[i-1][0] + "|" + lines[i][0]
        feats[13]= "pos[t-1]|pos[t]=" + lines[i-1][1] + "|" + lines[i][1]
        if i >= 2 and lines[i-2] != [""]:
            feats[0] = "w[t-2]=" + lines[i-2][0]
            feats[7] = "pos[t-2]=" + lines[i-2][1]
            feats[12]= "pos[t-2]|pos[t-1]=" + lines[i-2][1] + "|" + lines[i-1][1]
            feats[16]= "pos[t-2]|pos[t-1]|pos[t]=" + lines[i-2][1] + "|" + lines[i-1][1] + "|" + lines[i][1]
    else:
        isBOS = True
    if i+1 < n and lines[i+1] != [""]:
        feats[3] = "w[t+1]=" +  lines[i+1][0]
        feats[10]= "pos[t+1]=" + lines[i+1][1]
        feats[6] = "w[t]|w[t+1]=" + lines[i][0] + "|" + lines[i+1][0]
        feats[14]= "pos[t]|pos[t+1]=" + lines[i][1] + "|" + lines[i+1][1]
        if feats[13] != "":
            feats[17] = "pos[t-1]|pos[t]|pos[t+1]=" + lines[i-1][1] + "|" + lines[i][1] + "|" + lines[i+1][1]
        if i+2 < n and lines[i+2] != [""]:
            feats[4] = "w[t+2]=" + lines[i+2][0]
            feats[11]= "pos[t+2]=" + lines[i+2][1]
            feats[15]= "pos[t+1]|pos[t+2]=" + lines[i+1][1] + "|" + lines[i+2][1]
            feats[18]= "pos[t]|pos[t+1]|pos[t+2]=" + lines[i][1] + "|" + lines[i+1][1] + "|" + lines[i+2][1]
    else:
        isEOS = True
    out = lines[i][2]
    for feat in feats:
        if feat != "": out += "\t" + feat
    if isBOS: out += "\t__BOS__"
    if isEOS: out += "\t__EOS__"
    print out

