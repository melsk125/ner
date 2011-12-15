import sys
import re
from optparse import OptionParser
from nltk import word_tokenize

optionParser = OptionParser()

options, args = optionParser.parse_args()

if len(args) == 0:
    f = sys.stdin
else:
    f = open(args[0])

d = dict()
i = 0
for line in f:
    if i % 20000 == 0:
        sys.stderr.write("Entry: " + str(i) + "\n")
    i += 1
    line = re.split('\t', line)
    if line[0] != '1' and line[0] != '2' and line[0] != '3' and line[0] != '4':
        jterm = line[1]
        eterm = word_tokenize(line[2])
        for token in eterm:
            if token in d:
                d[token].add(jterm)
            else:
                d[token] = set([jterm])

sys.stderr.write(str(i) + "\n")
sys.stderr.write(str(len(d)) + "\n")

for k, v in d.iteritems():
    sys.stdout.write(k)
    for j in v:
        sys.stdout.write('\t' + j)
    sys.stdout.write('\n')
