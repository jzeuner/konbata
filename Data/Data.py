"""
Internal Data structure

Basically a tree
"""
class DataNode:

	def __init__(self, value, tag=None, children=None, attribute=None):
		self.data = value
		self.children = children

		self.tag = tag
		self.attribute = attribute


	def add(self, node):
		if self.children == None:
			self.children = []
		self.children += [node]


	def height(self):
		if self.children == None:
			return 1
		else:
			return 1 + max([x.height() for x in children])


class DataTree:

	def __init__(self, type):
		self.root = DataNode('File')
		self.type = type

	def height(self):
		return self.root.height()
