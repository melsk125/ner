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

lfreq = dict([])

count = 0
tcount = len(terms)

wnl = nltk.stem.WordNetLemmatizer()

for entry in terms:
	if count %1000 == 0:
		sys.stderr.write("Tagging and lemmatizing word " + str(count) + "/" + str(tcount) + "\n")
	count += 1
	pos = nltk.pos_tag(nltk.word_tokenize(entry))
	lterm = []
	for word in pos:
		if word[1][0] == 'N':
			lterm.append(wnl.lemmatize(word[0]))
		elif word[1][0] == 'V':
			lterm.append(wnl.lemmatize(word[0], 'v'))
		elif word[1][0] == 'J':
			lterm.append(wnl.lemmatize(word[0], 'a'))
		else:
			lterm.append(word[0])
	lterm = lib.collapse_string(lterm, ' ')
	if lterm in lfreq:
		lfreq[lterm] += terms[entry]
	else:
		lfreq[lterm] = terms[entry]

sys.stderr.write("End tagging\n")

for lword, freq in sorted(lfreq.items(), key = lambda entry: entry[1], reverse=True):
	print lword + '\t' + str(freq)
	
