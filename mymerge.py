from bubble import bubble_sort

def merge_sort(filename, comp = cmp, key = None):
	files = []
	cur_line = []
	f = open(filename, 'r')
	RAMSIZE = 10
	for line in f:
		if line.isspace(): continue
		cur_line.append(line)
		if len(cur_line) == RAMSIZE:
			bubble_sort(cur_line, comp, key)
			if files == None:
				temp_f = open('tmp_0.txt', 'w')
			else:
				temp_f = open('tmp_' + str(len(files)) + '.txt', 'w')
			for i in cur_line:
				temp_f.write(i)
			temp_f.close()
			files.append(temp_f)
			cur_line = []
	if cur_line:
		bubble_sort(cur_line, comp, key)
		if files == None:
			temp_f = open('tmp_0.txt', 'w')
		else:
				temp_f = open('tmp_' + str(len(files)) + '.txt', 'w')
		for i in cur_line:
				temp_f.write(i)
		temp_f.close()
		files.append(temp_f)
	f.close()
	f2 = open('mysort.txt', 'w')
	buffers = []
	for i in range(len(files)): 
		files[i] = open('tmp_' + str(i) + '.txt', 'r')
	for line in files: 
		buffers.append(line.readline())
	while files:
		min_n = 0
		for i in range(1, len(buffers)):
			if comp(buffers[min_n], buffers[i]) > 0:
				min_n = i
		f2.write(buffers[min_n])
		t = files[min_n].readline()
		if t == '':
			del files[min_n]
			del buffers[min_n]
		else:
			buffers[min_n] = t
	f2.close()

merge_sort('sort_file.txt', key=int)
print 'hell, yeah'

