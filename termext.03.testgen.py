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

for i in range(len(lines)):
    if i % 1000 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if 'EKYWD' in line and 'EABST' in line:
        abstract = line['EABST']
        keywords = re.split('\t', line['EKYWD'])
        abstract = word_tokenize(abstract)
        keywords = [word_tokenize(keyword) for keyword in keywords]
        j = 0
        while j < len(abstract):
            found = False
            for k in range(len(keywords)):
                keyword = keywords[k]
                keyword_len = len(keyword)
                if keyword_len > 0 and keyword == abstract[j:j+keyword_len]:
                    print "B\t" + print_features(keyword[0])
                    for l in keyword[1:]:
                        print "I\t" + print_features(l)
                    found = True
                    j += keyword_len
                if found:
                    break
            if j >= len(abstract):
                break
            print "O\t" + print_features(abstract[j])
            j += 1


sys.stderr.write("Finished\n")
