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

s.discard('')

posdict = dict([])

sys.stderr.write("Start tagging\n")

count = 0
tcount = len(s)

for entry in s:
	if count % 1000 == 0:
		sys.stderr.write("Tagging word " + str(count) + "/" + str(tcount) + "\n");
	count += 1
	tagged_entry = nltk.pos_tag(nltk.word_tokenize(entry))
	tag_list = [word[1] for word in tagged_entry]
	posdict[entry] = lib.collapse_string(tag_list, '/')
	
sys.stderr.write("End tagging\n")

posset = set(posdict.values())

posfreq = dict([(posent, 0) for posent in posset])

sys.stderr.write("Start counting for each POS tag string\n")

for entry in list:
	if entry != '':
		posfreq[posdict[entry]] += 1

sys.stderr.write("Finished counting\n");
sys.stderr.write("Start writing output\n");

for pos, freq in sorted(posfreq.items(), key = lambda entry: entry[1], reverse=True):
	print pos + '\t' + str(freq)
