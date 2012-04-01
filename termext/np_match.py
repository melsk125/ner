import sys

args = sys.argv[1:]

if len(args) < 2:
	exit(1)
else:
	fabstr = open(args[0])
	fnp = open(args[1])


nps = [[]]

for line in fnp:
	line = line.strip()
	if line == "":
		nps.append([])
	else:
		nps[-1].append(line)

abstr = 0

for line in fabstr:
	abstr += 1
	line = line.strip()
	for np in nps:
		pos = 0
		pos = line.find(np[0], pos)
		wordStart = pos
		while pos != -1:
			ok = True
			for word in np:
				if ok:
					newpos = line.find(word, pos)
					if newpos in range(pos,3):
						pos = newpos + len(word)
					else:
						ok = False
			if ok:
				print str(abstr) + "\tNP\t" + str(wordStart) + "\t" + str(pos) + line[wordStart:pos]
			pos = line.find(np[0], pos)
			wordStart = pos