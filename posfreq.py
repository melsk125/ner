import re
import sys
import nltk
import lib

f=open(sys.argv[1])
raw = f.read()

sys.stderr.write("Read finished\n")

lines = lib.get_dat(raw)
list = lib.get_eterms(lines)

sys.stderr.write("Extracted keywords for each line\n")
sys.stderr.write("Total: " + str(len(list)) + " entries\n")

list = [entry.lower() for entry in list]

sys.stderr.write("Decapitalized\n")

s = set(list)

ulist = [entry.split() for entry in s]

sys.stderr.write("Extracted unique entries\n")
sys.stderr.write("Total: " + str(len(ulist)) + " unique entries\n")

nusize = len(ulist)

sys.stderr.write("POS Tag started\n")

taggedlist = []

for i in range(nusize):
	if i%1000 == 0:
		sys.stderr.write(str(i) + "/" + str(nusize) + "\n")
	taggedlist.append(nltk.pos_tag(ulist[i]))

sys.stderr.write("POS Tag finished\n");

