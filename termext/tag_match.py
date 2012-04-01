import sys

args = sys.argv[1:]

if len(args) < 2:
	exit(1)
else:
	fabstr = open(args[0])
	ftag = open(args[1])

pos = 0
wordStart = 0
inTerm = False

abstr = 0

for line in fabstr:
	abstr += 1
	line = line.strip()
	tag, word = ftag.readline().strip().split("\t")
	if tag == "B":
		inTerm = True
		wordStart = line.find(word, pos)
		pos = wordStart + len(word)
	if tag == "I":
		pos = line.find(word, pos) + len(word)
	else:
		if inTerm:
			inTerm = False
			print str(abstr) + "\tMODEL\t" + str(wordStart) + "\t" + str(pos) + line[wordStart:pos]
		pos = line.find(word, pos) + len(word)


