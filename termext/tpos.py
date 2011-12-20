import lib
import sys
import re

from nltk import word_tokenize, pos_tag, PunktSentenceTokenizer, tag

if len(sys.argv) < 2:
    raw = sys.stdin.read()
else:
    f = open(sys.argv[1])
    raw = f.read()

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

p = PunktSentenceTokenizer()

for i in range(len(lines)):
    if i % 100 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if not ("EKYWD" in line and "EABST" in line):
        continue
    abstract = line["EABST"]
    abstract = p.tokenize(abstract)
    abstract = [word_tokenize(sentence) for sentence in abstract]
    keywords = re.split("\t", line["EKYWD"])
    keywords = [word_tokenize(keyword) for keyword in keywords]
    for sentence in abstract:
        pos_sentence = pos_tag(sentence)
        pos_sentence = [(word, tag.simplify.simplify_wsj_tag(t)) for word, t in pos_sentence]
        j = 0
        while j < len(sentence):
            found = False
            for k in range(len(keywords)):
                keyword = keywords[k]
                keyword_len = len(keyword)
                if keyword_len > 0 and keyword == sentence[j:j+keyword_len]:
                    for l in range(keyword_len):
                        this_word = keyword[l]
                        this_pos = pos_sentence[j+l][1]
                        out = this_word + "\t" + this_pos + "\t"
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
            this_pos = pos_sentence[j][1]
            out = this_word + "\t" + this_pos + "\tO"
            print out
            j += 1
        print

sys.stderr.write("Finished\n")

