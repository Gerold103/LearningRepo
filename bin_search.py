def __bin_search_iml(array, val, left, right, key = lambda x: x, _cmp = cmp):
	if left == right: return left
	if (right - left == 1):
		if key(array[right]) - key(val) == 0:
			res = right
		else:
			res = left
		return res
	middle = left + int((right - left) / 2)
	# print right
	if key(array[middle]) == key(val): return middle
	else:
		comp = _cmp(key(array[middle]), key(val))
		if comp > 0:
			return __bin_search_iml(array, val, left, middle, key, _cmp)
		else:
			return __bin_search_iml(array, val, middle, right, key, _cmp)

def bin_search(array, val, key = lambda x: x, _cmp = cmp):
	if len(array) < 1: return - 1
	return __bin_search_iml(array, val, 0, len(array) - 1, key, _cmp)

def b_search(array, val, key = lambda x: x, _cmp = cmp):
	if len(array) < 1: return -1
	n = bin_search(array, val, key, _cmp)
	if array[n] == val: return n
	return -1

def reversed_cmp(left, right): return -cmp(left, right)






#      0  1  2  3   4   5   6    7    8    9    10   11
# a = [1, 5, 8, 12, 43, 54, 112, 321, 456, 767, 931, 999]
#    0      1     2     3     4     5    6    7    8    9    10  11
a = [12121, 5435, 4543, 3223, 1221, 999, 435, 422, 234, 111, 0, -5]
print b_search(a, 1221, _cmp = reversed_cmp)
