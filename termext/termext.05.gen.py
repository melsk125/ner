import lib
import sys
import re
from optparse import OptionParser
from nltk import word_tokenize, pos_tag, PunktSentenceTokenizer, tag
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

if dicfile:
    fdic = open(dicfile)
    sys.stderr.write("Reading dictionary\n")
    d = dict()
    lines = fdic.readlines()
    lines = [re.split("\t", line, 1) for line in lines]
    for line in lines:
        d[line[0]] = line[1]
else:
    sys.stderr.write("Please input dict file")
    exit(1)

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

p = PunktSentenceTokenizer()

taking_pos = set(["ADJ", "ADV", "FW", "N", "NP", "NUM", "VG", "VN"])

for i in range(len(lines)):
    if i % 100 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if "EKYWD" in line and "EABST" in line:
        abstract = line["EABST"]
        abstract = p.tokenize(abstract)
        abstract = [word_tokenize(sent) for sent in abstract]
        abstract = lib.collapse(abstract)
        pos_abstract = pos_tag(abstract)
        pos_abstract = [(word, tag.simplify.simplify_wsj_tag(t)) for word, t in pos_abstract]
        keywords = re.split("\t", line["EKYWD"])
        keywords = [word_tokenize(keyword) for keyword in keywords]
        j = 0
        while j < len(abstract):
            found = False
            for k in range(len(keywords)):
                keyword = keywords[k]
                keyword_len = len(keyword)
                if keyword_len > 0 and keyword == abstract[j:j+keyword_len]:
                    for l in range(keyword_len):
                        this_word = keyword[l]
                        this_pos = pos_abstract[j+l][1]
                        out = ""
                        if l == 0:
                            out += "B\t"
                        else:
                            out += "I\t"
                        out += print_features(this_word)
                        out += "\tPOS=" + this_pos
                        if this_pos in taking_pos and this_word in d:
                            out += "\t" + d[this_word]
                        print out
                    found = True
                    j += keyword_len
                if found:
                    break
            if j >= len(abstract):
                break
            this_word = abstract[j]
            this_pos = pos_abstract[j][1]
            out = "O\t" + print_features(this_word)
            out += "\tPOS=" + this_pos
            if this_pos in taking_pos and this_word in d:
                out += "\t" + d[this_word]
            print out
            j += 1

sys.stderr.write("Finished\n")



