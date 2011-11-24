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

worddict = dict([(el, (0,0,0,0,0)) for el in wordset])

for term in terms:
	term = term.split()
	for i in range(len(term)):
		f,a,b,c,d = worddict[term[i]]
		if len(term) == 1:
			worddict[term[i]] = f+1,a+1,b,c,d
		if i == 0:
			worddict[term[i]] = f+1,a,b+1,c,d
		elif i == (len(term)-1):
			worddict[term[i]] = f+1,a,b,c,d+1
		else:
			worddict[term[i]] = f+1,a,b,c+1,d

for word, (f,a,b,c,d) in sorted(worddict.items(), key=lambda entry: entry[1][0], reverse=True):
	print word + '\t' + str(f) + '\t' + str(a) + '\t' + str(b) + '\t' + str(c) + '\t' + str(d)
