import sys

if len(sys.argv) < 2:
	f = sys.stdin
else:
	f = open(sys.argv[1])

g_in_line = False
g_word_count = 0

g_list = []

t_in_line = False
t_word_count = 0

t_list = []

w_list = []

for line in f:
	line = line.strip().split()
	w_list.append(line[0])
	if line[1] == 'B':
		if g_in_line:
			g_list.append(g_word_count)
			for i in range(g_word_count-1):
				g_list.append("I")
		g_in_line = True
		g_word_count = 1
	elif line[1] == 'I':
		g_word_count += 1
	else:
		if g_in_line:
			g_list.append(g_word_count)
			for i in range(g_word_count-1):
				g_list.append("I")
		g_in_line = False
		g_list.append("O")
	if line[2] == 'B':
		if t_in_line:
			t_list.append(t_word_count)
			for i in range(t_word_count-1):
				t_list.append("I")
		t_in_line = True
		t_word_count = 1
	elif line[2] == 'I':
		t_word_count += 1
	else:
		if t_in_line:
			t_list.append(t_word_count)
			for i in range(t_word_count-1):
				t_list.append("I")
		t_in_line = False
		t_list.append("O")
		

for i in range(len(g_list)):
	print w_list[i] + "\t" + str(g_list[i]) + "\t" + str(t_list[i])
