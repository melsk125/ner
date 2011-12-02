import sys
import lib
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-l", action="store_true", dest="lowercase", default=False, help="force lowercase")

options, args = parser.parse_args()

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

lines = lib.get_dat(raw)

je_dict = dict([])

sys.stderr.write("Start making dict\n")

for line in lines:
    if options.lowercase == True:
        add_text = line[2].lower()
    else:
        add_text = line[2]
    
	if line[1] in je_dict:
		je_dict[line[1]].add(add_text)
	else:
		je_dict[line[1]] = set([add_text])

sys.stderr.write("Finished making dict\n")

for jw, ew in sorted(je_dict.items(), key=lambda entry: len(entry[1]), reverse=True):
	print jw + '\t' + str(len(ew)) + '\t' + lib.collapse_string(list(ew), '\t')
	

