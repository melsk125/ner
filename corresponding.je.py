import sys
import lib
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-l", action="store_true", dest="lowercase", default=False, help="force lowercase")

parser.add_option("-L", action="store_true", dest="lemmatize", default=False, help="force lemmatize")

options, args = parser.parse_args()

lowercase = options.lowercase
lemmatize = options.lemmatize

if lowercase:
    sys.stderr.write("Lowercase\n")
else:
    sys.stderr.write("Not lowercase\n")

if lemmatize:
    sys.stderr.write("Lemmatize\n")
    import nltk
    wnl = nltk.stem.WordNetLemmatizer()
else:
    sys.stderr.write("Not lemmatize\n")

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat(raw)

je_dict = dict([])

sys.stderr.write("Start making dict\n")

count = 0

sys.stderr.write("Total: " + str(len(lines)) + " entries\n")

for line in lines:
    if count%1000 == 0:
        sys.stderr.write(str(count) + " ")
    if count%10000 == 0:
        sys.stderr.write("\n")
    count += 1
    add_text = line[2]
    if lemmatize:
        pos = nltk.pos_tag(add_text.split())
        lterm = []
        for word, p in pos:
            if word[0] == 'N':
                lterm.append(wnl.lemmatize(word))
            elif word[0] == 'V':
                lterm.append(wnl.lemmatize(word, 'v'))
            elif word[0] == 'J':
                lterm.append(wnl.lemmatize(word, 'a'))
            else:
                lterm.append(word)
        add_text = lib.collapse_string(lterm, ' ')
    if lowercase:
        add_text = add_text.lower()
    if (line[1] in je_dict):
        je_dict[line[1]].add(add_text)
    else:
        je_dict[line[1]] = set([add_text])
        

sys.stderr.write("Finished making dict\n")

sys.stderr.write(str(len(je_dict)))

for jw, ew in sorted(je_dict.items(), key=lambda entry: len(entry[1]), reverse=True):
	print jw + '\t' + str(len(ew)) + '\t' + lib.collapse_string(list(ew), '\t')
	

