import copy

class TreeNode(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.left = None
		self.right = None

	def set_key(self, key, val):
		if (key > self.key):
			if (self.right == None):
				self.right = TreeNode(key, val)
			else:
				self.right.set_key(key, val)
		elif key == self.key: self.val = val
		else:
			if (self.left == None):
				self.left = TreeNode(key, val)
			else:
				self.left.set_key(key, val)

	def find_val(self, key):
		if (key == self.key): return self.val
		if (key > self.key):
			if (self.right == None): return None
			return self.right.find_val(key)
		else:
			if (self.left == None): return None
			return self.left.find_val(key)

	def items(self):
		res = dict()
		res[self.key] = self.val
		if (self.right == None) and (self.left == None): return res
		if (self.left != None):
			res.update(self.left.items())
		if (self.right != None):
			res.update(self.right.items())
		return res

	@staticmethod
	def create_tree(keys, values):
		if (len(keys) != len(values)) or (len(keys) == 0): return None
		res = TreeNode(keys[0], values[0])
		for i in range(1, len(keys)): res.set_key(keys[i], values[i])
		return res

	@staticmethod
	def from_file(file_name):
		f = open(file_name, 'r')
		keys = f.readline().split('#$#')
		vals = f.readline().split('#$#')
		f.close()
		if (len(keys[-1]) == 0) or (keys[-1] == '\n'): del keys[-1]
		if (len(vals[-1]) == 0) or (vals[-1] == '\n'): del vals[-1]
		if (len(keys) != len(vals)) or (len(keys) == 0): return None

		for i in range(len(keys)):
			if (keys[i].find('#&#') == -1): continue
			keys[i] = keys[i].replace('#&#', '\n')
		for i in range(len(vals)):
			if (vals[i].find('#&#') == -1): continue
			vals[i] = vals[i].replace('#&#', '\n')

		return TreeNode.create_tree(keys, vals)

	def save(self, file_name):
		f = open(file_name, 'w')
		items = self.items()

		keys = items.keys()
		vals = items.values()

		for i in range(len(keys)):
			if keys[i].find('\n') == -1: continue
			keys[i] = keys[i].replace('\n', '#&#')

		for i in range(len(vals)):
			if vals[i].find('\n') == -1: continue
			vals[i] = vals[i].replace('\n', '#&#')

		f.write('#$#'.join(keys) + '#$#\n')
		f.write('#$#'.join(vals) + '#$#\n')

		f.close()

	def __getitem__(self, index):
		return self.find_val(index)