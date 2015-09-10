def simple_search(array, val,  key = lambda x: x):
	for i in range(len(array)):
		if (key(array[i]) == val): return i
	return -1

def __find_best_impl(array, val, key, left, right, _cmp):
	if (left == right): return left
	if (right - left == 1):
		min_d = abs(key(array[left]) - val)
		min_n = left
		if (abs(key(array[right]) - val) < min_d):
			min_n = right
		return min_n
	middle = left + int((right - left) / 2)
	if (key(array[middle]) == val): return middle
	else:
		cmp_r = _cmp(key(array[middle]), val)
		if (cmp_r > 0):
			return __find_best_impl(array, val, key, left, middle, _cmp)
		else:
			return __find_best_impl(array, val, key, middle, right, _cmp)

def find_best(array, val, key = lambda x: x, _cmp = cmp):
	if (len(array) < 1): return -1
	return __find_best_impl(array, val, key, 0, len(array) - 1, _cmp)


def binary_search(array, val, key = lambda x: x, _cmp = cmp):
	if (len(array) < 1): return -1
	n = find_best(array, val, key, _cmp)
	if (array[n] == val): return n
	else: return -1

def default_hash(ob, d = 4):
	return abs(hash(ob)) % d

class BucketDict(object):
	def __init__(self, buckets_num = 4, hash_ = default_hash):
		self.buckets = []
		self.hash = hash_
		self.buckets_num = buckets_num
		for i in range(4): self.buckets.append([])
	
	def add_key(self, key, val):
		n = self.hash(key, self.buckets_num)
		l = self.buckets[n]
		l.append((key, val))
		l.sort(key = lambda x: (x[0]))

	def find_key(self, key):
		n = self.hash(key, self.buckets_num)
		l = self.buckets[n]
		i = binary_search(l, key, lambda x: x[0])
		if (i == -1): return None
		else: return l[i][1]


# def insert_to_sorted(array, val, key = lambda x: x, cmp_ = cmp):


class OwnSet(object):

	def __init__(self):
		self.obs = []

	def add_key(self, val):
		if binary_search(self.obs, val) != -1:
			print self.obs
			return
		else:
			best_n = find_best(self.obs, val)
			if (best_n == -1): self.obs.append(val)
			else:
				if (self.obs[best_n] > val):
					self.obs.insert(best_n, val)
				else:
					self.obs.insert(best_n + 1, val)
		print self.obs

	def contains(self, val):
		return (binary_search(self.obs, val) == -1)

	def remove(self, val):
		n = binary_search(self.obs, val)
		if (n != -1):
			self.obs.pop(n)
		print self.obs


test = [34, 56, 0, 21, 35, 67, 89, 4, 7, 42, 69]

test = [0, 4, 7, 21, 34, 35, 42, 56, 67, 69, 89] #11

test2 = [0]
test3 = [0, 1]
test4 = []
test5 = [0, 1, 2]

s = OwnSet()
s.add_key(3)
s.add_key(6)
s.add_key(10)
s.add_key(10)
s.add_key(5)
s.add_key(3)

s.remove(3)
s.remove(10)
