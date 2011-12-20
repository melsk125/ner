import re
import sys
import lib

f = open(sys.argv[1])
raw = f.read()

terms = lib.get_freq(raw)

if '' in terms: terms.pop('')

list = [term.split() for term in terms.keys()]

list = lib.collapse(list)

s = set(list)

wfreq = dict([(word, 0) for word in s])

for words, freq in terms.items():
	for word in words.split():
		wfreq[word] += freq

for word, a in sorted(wfreq.items(), key=lambda entry: entry[1], reverse=True):
	print word + '\t' + str(a)
