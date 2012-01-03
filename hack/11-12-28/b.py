from collections import namedtuple

line = namedtuple("line", ["word", "outdoc", "indoc", "outword", "inword"])

from sys import stdin

a = [line(word=word, outdoc=int(outdoc), indoc=int(indoc), outword=int(outword), inword=int(inword)) for word, outdoc, indoc, outword, inword in (l.rstrip("\n").split("\t") for l in stdin)]

for threshold in (t/1000.0 for t in xrange(0,1001,5)):
	s = 0
	for i in a:
		if i.inword/float(i.outword) >= threshold:
			s += i.outword
	print str(threshold) + "\t" + str(s)
