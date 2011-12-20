import re
import sys
import lib

f = open(sys.argv[1])
raw = f.read()

terms = lib.get_freq(raw)

if '' in terms: terms.pop('')

wordset = set(lib.collapse([term.split() for term in terms.keys()]))

worddict = dict([(el, (0,0,0,0,0)) for el in wordset])

for term, count in terms.items():
	term = term.split()
	for i in range(len(term)):
		f,a,b,c,d = worddict[term[i]]
		if len(term) == 1:
			worddict[term[i]] = f+count,a+count,b,c,d
		elif i == 0:
			worddict[term[i]] = f+count,a,b+count,c,d
		elif i == (len(term)-1):
			worddict[term[i]] = f+count,a,b,c,d+count
		else:
			worddict[term[i]] = f+count,a,b,c+count,d

for word, (f,a,b,c,d) in sorted(worddict.items(), key=lambda entry: entry[1][0], reverse=True):
	print word + '\t' + str(f) + '\t' + str(a) + '\t' + str(b) + '\t' + str(c) + '\t' + str(d)

