import mymodule

def bubble_sort(array, cmp_ = cmp, key = None, reverse = False):
	for i in range(len(array)):
		for j in range(len(array) - i - 1):
			left = None
			right = None
			if (key != None):
				left = key(array[j])
				right = key(array[j + 1])
			else:
				left = array[j]
				right = array[j + 1]
			if cmp_(left, right) >= 0:
				array[j], array[j + 1] = array[j + 1], array[j]
	if (reverse == True): array.reverse()

RAM_SIZE = 10

def merge_sort(_file, cmp_ = cmp, key = None):
	files = []
	f = open(_file, 'r')
	cur_lines = []
	for line in f:
		if (line.isspace()): continue
		cur_lines.append(line)
		if len(cur_lines) == RAM_SIZE:
			bubble_sort(cur_lines, cmp_, key)
			tmp_f = None
			if (files == None):
				tmp_f = open('tmp_0.txt', 'w')
			else:
				tmp_f = open('tmp_' + str(len(files)) + '.txt', 'w')
			for l in cur_lines: tmp_f.write(l + '\n')
			tmp_f.close()
			files.append(tmp_f)
			cur_lines = []

	if (len(cur_lines) != 0):
		bubble_sort(cur_lines, cmp_, key)
		if (files == None):
			tmp_f = open('tmp_0.txt', 'w')
		else:
			tmp_f = open('tmp_' + str(len(files)) + '.txt', 'w')
		for l in cur_lines: tmp_f.write(l + '\n')
		tmp_f.close()
		files.append(tmp_f)
		cur_lines = []
	f.close()
	f2 = open(_file, 'w')

	buffers = []
	for i in range(len(files)): files[i] = open('tmp_' + str(i) + '.txt', 'r')
	for f in files:
		buffers.append(f.readline())

	while len(files) > 0:
		min_n = 0
		for i in range(1, len(buffers)):
			if (cmp_(buffers[min_n], buffers[i]) > 0): min_n = i
		f2.write(buffers[min_n] + '\n')
		t = files[min_n].readline()
		if (t == ''):
			files[min_n].close()
			del files[min_n]
			del buffers[min_n]
		else:
			buffers[min_n] = t
	f2.close()


arr = [45, 32, 67, -100, 3, 6, 9, 25, 0, 0, -6]

merge_sort('sort_file.txt')

print 'success'

#   \n = #&#
#	#$# - #$$#
#	#&# - #&&#

# root = mymodule.TreeNode(10, 'ten')
# root.add_key(-5, '-five')
# root.add_key(15, 'fifteen')
# root.add_key(5, 'five')
# root.add_key(3, 'three')
# root.add_key(6, 'six')
# root.add_key(12, 'twelve')
# root.add_key(8, 'eight')
# root.add_key(16, 'sixteen')

# print root[12]

# print root[3]

# print root.items()


# keys = ['Ivan', 'Vasiliy', 'Nikholay', 'Dmitry', 'Vladislav', 'Konstantin', 'Mikhail']
# values = [1, 2, 3, 4, 5, 6, 7]

# root = mymodule.TreeNode.create_tree(keys, values)

# print root['Ivan']

# print root['Konstantin']

# print root['Dmitry']

# print root.items()
