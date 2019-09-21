"""
Internal Data structure

Basically a tree.
"""

class DataNode:
	"""
	TODO
	"""

	def __init__(self, value, tag=None, children=None, attribute=None):
		"""
		TODO
		"""

		self.data = value
		# TODO: check for datatype of list of DataNode
		# TODO: add option to set children=DataNode(1)
		if children == None:
			self.is_leaf = True
		else:
			self.is_leaf = False

		self.children = children

		self.tag = tag
		self.attribute = attribute



	def add(self, node):
		"""
		TODO
		"""

		if self.children == None:
			self.children = []
			self.is_leaf = True
		self.children += [node]


	def height(self):
		"""
		TODO
		"""

		if self.children == None:
			return 1
		else:
			return 1 + max([x.height() for x in self.children])


	def is_leaf(self):
		"""
		TODO
		"""

		return self.is_leaf


	def merge_node(self, child):
		"""
		TODO
		"""

		self.data = self.data + ", " + child.data


	def minimize_height(self, tree_height, cur_height):
		"""
		TODO
		"""

		self.children[:] = (child for child in self.children
							if not(child.is_leaf and ((tree_height - cur_height) == 1))
							else self.merge_node(child))

		for child in self.children:
			child.minimize_height(self, tree_height, cur_height+1)


class DataTree:
	"""
	TODO
	"""

	def __init__(self, type=None):
		"""
		TODO
		"""

		self.root = DataNode('File')
		self.type = type


	def height(self):
		"""
		TODO
		"""

		return self.root.height()


	def minimize_height(self, num):
		"""
		TODO
		"""

		if num > self.height:
			# TODO error
			pass

		for child in self.root.children:
			child.minimize_height(self.height, 2)

		if num > 1:
			self.minimize_height(self, num-1)
