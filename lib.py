import re

def collapse(list):
	ret = []
	for el in list:
		ret.extend(el)
	return ret

def get_line_sgml(line):
    line = re.findall(r"<(\w+)>(.+)</\1>", line)
    return line

def get_dat_sgml(raw):
    lines = re.split('\n', raw)[:-1]
    lines = [re.findall(r"<(\w+)>(.+)</\1>", line) for line in lines]
    return lines

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

def get_multidict(raw):
	lines = re.split('\n', raw)[:-1]
	lines = [re.split('\t', line) for line in lines]
	d = dict([(e[0], [int(s) for s in e[1:]]) for e in lines])
	return d

def collapse_string(list, ch):
	ret = ''
	for item in list:
		ret += item
		ret += ch
	ret = ret[:-1]
	return ret

def min2(a, b):
    if a < b:
        return a
    else:
        return b

def levenshtein(str1, str2):
    rownum = len(str1)+1
    colnum = len(str2)+1
    mat = [[0 for col in range(colnum)] for row in range(rownum)]
    for i in range(rownum):
        for j in range(colnum):
            if i==0:
                mat[i][j] = j
            elif j==0:
                mat[i][j] = i
            else:
                if str1[i-1]==str2[j-1]:
                    diag = mat[i-1][j-1]
                else:
                    diag = mat[i-1][j-1]+1
                mat[i][j] = min2(diag,
                                min2(mat[i-1][j]+1,
                                     mat[i][j-1]+1))
    return mat[rownum-1][colnum-1]

