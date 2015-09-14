def __bin_search_iml(array, val, left, right, key = lambda x: x, _cmp = cmp):
	if len(array) < 1: return -1
	if (right - left == 1):
		if array[right] - val == 0:
			res = right
		else:
			res = left
		return res
	middle = left + int((right - left) / 2)
	# print right
	if key(array[middle]) == key(val): return middle
	if key(val) > key(array[middle]):
		return __bin_search_iml(array, val, middle, right, key, _cmp)
	else:
		return __bin_search_iml(array, val, left, middle, key, _cmp)

def bin_search(array, val, key, _cmp):
	if len(array) < 1: return - 1
	return __bin_search_iml(array, val, 0, len(array) - 1, key, _cmp)

def b_search(array, val, key = lambda x: x, _cmp = cmp):
	if len(array) < 1: return -1
	n = bin_search(array, val, key, _cmp)
	if array[n] == val: return n
	return -1
#    0  1  2  3   4   5   6    7    8    9    10   11
a = [1, 5, 8, 12, 43, 54, 112, 321, 456, 767, 931, 999]
print b_search(a, 112)
