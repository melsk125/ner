import re
import sys
import lib

argc = len(sys.argv)

terms = dict([])

for i in range(1,argc):
	f = open(sys.argv[i])
	sys.stderr.write("Opened " + sys.argv[i] + "\n")
	raw = f.read()
	new_terms = lib.get_multidict(raw)
	for entry in new_terms.items():
		if entry[0] in terms:
			v = terms[entry[0]]
			for j in range(len(v)):
				v[j] += entry[1][j]
			terms[entry[0]] = v
		else:
			terms[entry[0]] = entry[1]
	sys.stderr.write("Combined\n")

sys.stderr.write("Start writing output " + str(len(terms)) + " entries\n")
for word, freq in sorted(terms.items(), key=lambda entry: entry[1][0], reverse=True):
	print word + '\t' + lib.collapse_string([str(f) for f in freq], '\t')

