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
    fdic = open(dicfile, "w")
    have_dic = True

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

if have_dic:
    sys.stderr.write("Also calculate dict\n")

d = dict()

for i in range(len(lines)):
    if i % 1000 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if 'EKYWD' in line and 'EABST' in line and 'KYWD' in line:
        abstract = line['EABST']
        keywords = re.split('\t', line['EKYWD'])
        jkeywords = re.split('\t', line['KYWD'])
        if len(keywords) == len(jkeywords):
            abstract = word_tokenize(abstract)
            keywords = [word_tokenize(keyword) for keyword in keywords]
            j = 0
            while j < len(abstract):
                found = False
                for k in range(len(keywords)):
                    keyword = keywords[k]
                    jkeyword = jkeywords[k]
                    keyword_len = len(keyword)
                    if keyword_len > 0 and keyword == abstract[j:j+keyword_len]:
                        if have_dic:
                            if keyword[0] in d:
                                f, s = d[keyword[0]]
                                s.add(jkeyword)
                                d[keyword[0]] = f, s
                            else:
                                d[keyword[0]] = print_features(keyword[0]), set([jkeyword])
                        print "B\t" + print_features(keyword[0]) + "\t" + jkeyword
                        #print keyword[0] + "\tB\t" + str(i+1) + "\t" + str(k+1)
                        for l in keyword[1:]:
                            if have_dic:
                                if l in d:
                                    f, s = d[l]
                                    s.add(jkeyword)
                                    d[l] = f, s
                                else:
                                    d[l] = print_features(l), set([jkeyword])
                            print "I\t" + print_features(l) + "\t" + jkeyword
                        #print l + "\tI\t" + str(i+1) + "\t" + str(k+1)
                        found = True
                        j += keyword_len
                    if found:
                        break
                if j >= len(abstract):
                    break
                print "O\t" + print_features(abstract[j])
                #print abstract[j] + "\tO\t" + str(i+1) + "\t0"
                j += 1

if have_dic:
    sys.stderr.write("Printing dict\n")
    for k, (f, s) in d.iteritems():
        fdic.write(k + "\t")
        fdic.write(f)
        for j in s:
            fdic.write("\t" + j)
        fdic.write("\n")

sys.stderr.write("Finished\n")
