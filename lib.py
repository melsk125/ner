import re

def collapse(list):
	ret = []
	for el in list:
		ret.extend(el)
	return ret

def get_dat(raw):
	lines = re.split('\n', raw)[:-1]
	lines = [re.split('\t', line) for line in lines]
	return lines

def get_eterms(lines):
	return collapse([line[4+int(line[2]):4+int(line[2])+int(line[3])] for line in lines])

def get_freq(raw):
	lines = re.split('\n', raw)[:-1]
	lines = [re.split('\t', line) for line in lines]
	d = dict([(e[0],int(e[1])) for e in lines])
	return d


