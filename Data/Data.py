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
		self.children = children

		self.tag = tag
		self.attribute = attribute


	def add(self, node):
		"""
		TODO
		"""

		if self.children == None:
			self.children = []
		self.children += [node]


	def height(self):
		"""
		TODO
		"""

		if self.children == None:
			return 1
		else:
			return 1 + max([x.height() for x in self.children])


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
