import lib
import sys
import re

from nltk import word_tokenize, PunktSentenceTokenizer

if len(sys.argv) < 2:
    raw = sys.stdin.read()
else:
    f = open(sys.argv[1])
    raw = f.read()

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

sys.stderr.write("Reading all keywords\n")

all_keywords = set([])

for line in lines:
    line_dict = dict(line)
    if "EKYWD" in line_dict and "EABST" in line_dict:
        keywords = re.split("\t", line_dict["EKYWD"])
        all_keywords.update(set(keywords))

sys.stderr.write("Tokenize keywords\n")

keywords = []

for keyword in all_keywords:
    keywords.append(word_tokenize(keyword))

sys.stderr.write("All keywords: " + str(len(all_keywords)) + "\n")

p = PunktSentenceTokenizer()

for i in range(len(lines)):
    if i % 10 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if not ("EKYWD" in line and "EABST" in line):
        continue
    abstract = line["EABST"]
    abstract = p.tokenize(abstract)
    abstract = [word_tokenize(sentence) for sentence in abstract]
    for sentence in abstract:
        j = 0
        while j < len(sentence):
            found = False
            for k in range(len(keywords)):
                keyword = keywords[k]
                keyword_len = len(keyword)
                if keyword_len > 0 and keyword == sentence[j:j+keyword_len]:
                    for l in range(keyword_len):
                        this_word = keyword[l]
                        out = this_word + "\t"
                        if l == 0:
                            out += "B"
                        else:
                            out += "I"
                        print out
                    found = True
                    j += keyword_len
                if found:
                    break
            if j >= len(sentence):
                break
            this_word = sentence[j]
            out = this_word + "\tO"
            print out
            j += 1
        print

sys.stderr.write("Finished\n")






