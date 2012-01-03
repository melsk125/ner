import sys
import re

from optparse import OptionParser

optionParser = OptionParser()

optionParser.add_option("-g", dest="tagfile", action="store", type="string", metavar="TAGFILE")

optionParser.add_option("-c", dest="contextual", action="store_true", default=False)

optionParser.add_option("-p", dest="pontus", action="store_true", default=False)

optionParser.add_option("-j", dest="jcorr", action="store_true", default=False)

options, args = optionParser.parse_args()

tagfile = options.tagfile
contextual = options.contextual
pontus = options.pontus
jcorr = options.jcorr

if tagfile:
    sys.stderr.write("g\n")
if contextual:
    sys.stderr.write("c\n")
if pontus:
    sys.stderr.write("p\n")
if jcorr:
    sys.stderr.write("j\n")

if len(args) < 2:
    sys.stderr.write("Please input t5 and crf.out files\n")
    exit(1)

ft5 = open(args[0])
fcrf = open(args[1])

fgtag = 0

if tagfile:
    fgtag = open(tagfile)

i = 0

for line_t5 in ft5:
    i += 1
    if i % 100000 == 0:
        sys.stderr.write(str(i) + "\t")
    line_t5 = line_t5.strip()
    line_t5 = re.split("\t", line_t5)
    line_crf = fcrf.readline().strip()
    line_crf = re.split("\t", line_crf)
    out = ""
    if tagfile:
        line_gtag = fgtag.readline().strip()
        line_gtag = re.split("\t", line_gtag)
        out = line_gtag[1]
    else:
        out = line_t5[0]
    for item in line_crf[1:]:
        if contextual:
            out += "\t" + item
    for item in line_t5[1:]:
        if item.startswith("f[01]=") and not contextual:
            out += "\t" + item
        elif item.startswith("f[") and not item.startswith("f[01]=") and pontus:
            out += "\t" + item
        elif item.startswith("POS=") and not contextual:
            out += "\t" + item
        elif not item.startswith("f[") and not item.startswith("POS=") and jcorr:
            out += "\t" + item
    print out
    if "__EOS__" in line_crf:
        print






