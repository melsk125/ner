import lib
import sys
import re
from optparse import OptionParser
from nltk import word_tokenize
from features import print_features

optionParser = OptionParser()

optionParser.add_option("-d", dest="dicfile", action="store", type="string", metavar="DFILE")

options, args = optionParser.parse_args()

dicfile = options.dicfile

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

have_dic = False
if dicfile:
    fdic = open(dicfile)
    have_dic = True
    sys.stderr.write("Reading dictionary\n")
    d = dict()
    lines = fdic.readlines()
    lines = [re.split('\t', line, 1) for line in lines]
    for line in lines:
        d[line[0]] = line[1]

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
                    if have_dic:
                        if keyword[0] in d:
                            print "B\t" + d[keyword[0]]
                        else:
                            print "B\t" + print_features(keyword[0])
                    else:
                        print "B\t" + print_features(keyword[0])
                    #print "B\t" + print_features(keyword[0]) + "\t" + jkeyword
                    #print keyword[0] + "\tB\t" + str(i+1) + "\t" + str(k+1)
                    for l in keyword[1:]:
                        if have_dic:
                            if l in d:
                                print "I\t" + d[l]
                            else:
                                print "I\t" + print_features(l)
                        else:
                            print "I\t" + print_features(l)
                        #print "I\t" + print_features(l) + "\t" + jkeyword
                    #print l + "\tI\t" + str(i+1) + "\t" + str(k+1)
                    found = True
                    j += keyword_len
                if found:
                    break
            if j >= len(abstract):
                break
            if have_dic:
                if abstract[j] in d:
                    print "O\t" + d[abstract[j]]
                else:
                    print "O\t" + print_features(abstract[j])
            else:
                print "O\t" + print_features(abstract[j])
            #print abstract[j] + "\tO\t" + str(i+1) + "\t0"
            j += 1


sys.stderr.write("Finished\n")
