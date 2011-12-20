import lib
import re
import sys
import itertools

f = open(sys.argv[1])
lines = f.readlines()

sys.stderr.write("Read finished\n")

lines = [re.split("\t", line) for line in lines]
lines = [[entry.strip() for entry in line] for line in lines]
lines = [(line[0], line[2:]) for line in lines if len(line)>3]

distance_list = []

count = 0
size = len(lines)

for line in lines:
    if count % 100 == 0:
        sys.stderr.write(str(count) + "/" + str(size) + "\n")
    count += 1
    #    distance_list.append((line[0], sorted([(str1, str2, lib.levenshtein(str1, str2)) for str1, str2 in itertools.combinations(line[1], 2)], key=lambda entry: entry[2], reverse=True)))
    list = []
    for str1, str2 in itertools.combinations(line[1], 2):
        dist = lib.levenshtein(str1, str2)
        maxlen = max(len(str1), len(str2))
        normed = float(dist)/float(maxlen)
        list.append((str1, str2, dist, normed))
    distance_list.append((line[0], sorted(list, key=lambda entry: entry[3], reverse=True)))

for entry in distance_list:
    print entry[0] + "\t" + str(len(entry[1]))
    for p_entry in entry[1]:
        print p_entry[0] + "\t" + p_entry[1] + "\t" + str(p_entry[2]) + "\t" + str(p_entry[3])
