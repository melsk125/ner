import lib
import sys
import re
from optparse import OptionParser
from nltk import word_tokenize
from features import print_features

optionParser = OptionParser()

options, args = optionParser.parse_args()

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

d = dict()

for i in range(len(lines)):
    if i % 1000 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if "EKYWD" in line and "EABST" in line and "KYWD" in line:
        keywords = re.split("\t", line["EKYWD"])
        jkeywords = re.split("\t", line["KYWD"])
        if len(keywords) == len(jkeywords):
            keywords = [word_tokenize(keyword) for keyword in keywords]
            for k in range(len(keywords)):
                keyword = keywords[k]
                jkeyword = jkeywords[k]
                for word in keyword:
                    if word in d:
                        f, s = d[word]
                        s.add(jkeyword)
                        d[word] = f, s
                    else:
                        d[word] = print_features(word), set([jkeyword])

sys.stderr.write("Printing dict\n")
for k, (f, s) in d.iteritems():
    line = k + "\t"
    line += f
    for j in s:
        line += "\t" + j
    print line
sys.stderr.write("Finished\n");

