import re
import sys
import lib

f = open(sys.argv[1])
raw = f.read()

lines = lib.get_dat(raw)
list = lib.get_eterms(lines)

list = [entry.lower() for entry in list]

terms = [entry.strip() for entry in list]
words = lib.collapse([entry.split() for entry in list])

termset = set(terms)
wordset = set(words)

worddict = dict([(el, (0,0,0,0)) for el in wordset])

for term in termset:
	term = term.split()
	for i in range(len(term)):
		f,a,b,c = worddict[term[i]]
		if i == 0:
			worddict[term[i]] = f+1,a+1,b,c
		elif i == (len(term)-1):
			worddict[term[i]] = f+1,a,b,c+1
		else:
			worddict[term[i]] = f+1,a,b+1,c

for word, (f,a,b,c) in sorted(worddict.items(), key=lambda entry: entry[1][0], reverse=True):
	print word + '\t' + str(f) + '\t' + str(a) + '\t' + str(b) + '\t' + str(c)