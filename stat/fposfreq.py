import re
import sys
import nltk
import lib

f = open(sys.argv[1])
raw = f.read()

sys.stderr.write("Read finished\n")

terms = lib.get_freq(raw)

if '' in terms: terms.pop('')

sys.stderr.write("Extracted freq\n")
sys.stderr.write("Total: " + str(len(terms)) + " entries\n")

posfreq = dict([])

count = 0
tcount = len(terms)

for entry in terms:
	if count % 1000 == 0:
		sys.stderr.write("Tagging word " + str(count) + "/" + str(tcount) + "\n");
	count += 1
	pos = nltk.pos_tag(nltk.word_tokenize(entry))
	pos = [word[1] for word in pos]
	pos = lib.collapse_string(pos, '/')
	if pos in posfreq:
		posfreq[pos] += terms[entry]
	else:
		posfreq[pos] = terms[entry]

sys.stderr.write("End tagging\n")

for pos, freq in sorted(posfreq.items(), key = lambda entry: entry[1], reverse=True):
	print pos + '\t' + str(freq)


