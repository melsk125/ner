import lib
import sys
import re
import string

from optparse import OptionParser

optionParser = OptionParser()

options, args = optionParser.parse_args()

if len(args) == 0:
    raw = sys.stdin.read()
else:
    f = open(args[0])
    raw = f.read()

f.close()

lines = lib.get_dat_sgml(raw)

sys.stderr.write(str(len(lines)) + " entries\n")

sys.stderr.write("Reading all keywords\n")

all_keywords = set([])

for line in lines:
    line_dict = dict(line)
    if "EKYWD" in line_dict and "EABST" in line_dict:
        keywords = re.split("\t", line_dict["EKYWD"])
        all_keywords.update(set(keywords))

sys.stderr.write("All keywords: " + str(len(all_keywords)) + "\n")

d = dict()

for keyword in all_keywords:
    d[keyword] = (0, 0, 0, 0)   # global appearance, local appearance,
                                # glocal count, local count

sys.stderr.write("Start taking statistics\n")

for i in range(len(lines)):
    if i % 100 == 0:
        sys.stderr.write(str(i) + "/" + str(len(lines)) + "\n")
    line = dict(lines[i])
    if "EKYWD" in line and "EABST" in line:
        abstract = line["EABST"]
        keywords = re.split("\t", line["EKYWD"])
        for keyword in all_keywords:
            if keyword in abstract:
                ga, la, gc, lc = d[keyword]
                ga += 1
                gc += string.count(abstract, keyword)
                if keyword in keywords:
                    la += 1
                    lc += string.count(abstract, keyword)
                d[keyword] = (ga, la, gc, lc)

for keyword in all_keywords:
    line = keyword
    ga, la, gc, lc = d[keyword]
    line += "\t" + str(ga) + "\t" + str(la) + "\t" + str(gc) + "\t" + str(lc)
    if ga != 0 and la != 0 and gc != 0 and lc != 0:
        print line








