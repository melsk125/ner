import lib
import sys
import re
import codecs
from optparse import OptionParser
from nltk import word_tokenize

optionParser = OptionParser()

optionParser.add_option("-o", dest="outfile", action="store", type="string", metavar="FILE")

options, args = optionParser.parse_args()

outfile = options.outfile

if outfile != '':
    out = codecs.open(outfile, 'w', 'utf-8')
else:
    out = sys.stdout

if len(args) == 0:
    f = codecs.EncodedFile(sys.stdin, 'utf-8')
else:
    f = codecs.open(args[0], 'r', 'utf-8')

d = dict()
i = 0
for line in f:
    if i % 1000 == 0:
        sys.stderr.write("Entry: " + str(i) + "\n")
    i += 1
    line = lib.get_line_sgml(line)
    line = dict(line)
    if 'EKYWD' in line and 'KYWD' in line:
        ekeywords = re.split('\t', line['EKYWD'])
        jkeywords = re.split('\t', line['KYWD'])
        if len(ekeywords) == len(jkeywords):
            ekeywords = [word_tokenize(keyword) for keyword in ekeywords]
            for k in range(len(ekeywords)):
                ek = ekeywords[k]
                jk = jkeywords[k]
                for w in ek:
                    if w in d:
                        d[w].add(jk)
                    else:
                        d[w] = set([jk])

sys.stderr.write(str(i) + "\n")
sys.stderr.write(str(len(d)) + "\n")

for k, v in d.iteritems():
    out.write(k)
    for j in v:
        out.write('\t' + j)
    out.write('\n')

