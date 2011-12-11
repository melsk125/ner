import lib
import sys
import re
from optparse import OptionParser
from nltk import word_tokenize

optionParser = OptionParser()

options, args = optionParser.parse_args()

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat_sgml(raw)

"""
    Assume the input is in the format
        <Abstract text> <Count of keyword>  <Keyword 1> ... <Keyword n>
    Output
        <Token> <Tag (BIO)> (If Tag==B <Abstract number>   <Keyword number>)
"""

sys.stderr.write(str(len(lines)) + " entries\n")

for i in range(len(lines)):
    if i % 100 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if 'EKYWD' in line and 'EABST' in line:
        abstract = line['EABST']
        keywords = re.split('\t', line['EKYWD'])
        abstract = word_tokenize(abstract)
        output = []
        keywords = [word_tokenize(keyword) for keyword in keywords]
        j = 0
        while j < len(abstract):
            found = False
            for k in range(len(keywords)):
                keyword = keywords[k]
                keyword_len = len(keyword)
                if keyword == abstract[j:j+keyword_len]:
                    output.append((keyword[0], "B", k+1))
                    print keyword[0] + "\tB\t" + str(i+1) + "\t" + str(k+1)
                    for l in keyword[1:]:
                        output.append((l, "I", k+1))
                        print l + "\tI\t" + str(i+1) + "\t" + str(k+1)
                    found = True
                    j += keyword_len
                if found:
                    break
            output.append((abstract[j], "O", 0))
            print abstract[j] + "\tO\t" + str(i+1) + "\t0"
            j += 1

sys.stderr.write("Finished\n")
