import sys
import lib

f = open(sys.argv[1])
raw = f.read()

lines = lib.get_dat(raw)

je_dict = dict([])

sys.stderr.write("Start making dict\n")

for line in lines:
	if line[1] in je_dict:
		je_dict[line[1]].add(line[2].lower())
	else:
		je_dict[line[1]] = set([line[2].lower()])

sys.stderr.write("Finished making dict\n")

for jw, ew in sorted(je_dict.items(), key=lambda entry: len(entry[1]), reverse=True):
	print jw + '\t' + str(len(ew)) + '\t' + lib.collapse_string(list(ew), '\t')
	

