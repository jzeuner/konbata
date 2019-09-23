"""
Internal data structure for the Konbata libary.

Main idea is a data structure that can store data in form of a tree.
The DataTree should be manipulated and serve as comfortable structure.
"""

class DataNode:
	"""
	Class that represents the Node of a tree.

	These nodes actually store Data or serve as internal meta data nodes.
	So the node is an inner node or it is a leaf.
	"""

	def __init__(self, value, tag=None, children=None, attribute=None):
		"""
		Initiates the current DataNode.

		Parameters
        ----------
		value:
		tag: , optional
		children: , optional
		attribute: , optional
		"""

		# Check that data/value is not empty
		self.data = value
		# TODO: check for datatype of list of DataNode
		# TODO: add option to set children=DataNode(1)

		if children == None:
			self.leaf = True
		else:
			self.leaf = False

		self.children = children

		self.tag = tag
		self.attribute = attribute



	def add(self, node):
		"""
		Adds the node to the end of the children list.

		If node dont has children, it initiates the children list.

		Parameters
        ----------
		node: DataNode
		"""

		# TODO: check for the datatype of node

		if self.children == None:
			self.children = []
			self.leaf = True
		self.children += [node]


	def height(self):
		"""
		Returns the height of the node.

		This function considers height, as the node count!
		Therefore, if no children: height() => 1

		Returns
        -------
		height: int
		"""

		if self.children == None:
			return 1
		else:
			return 1 + max([x.height() for x in self.children])


	def is_leaf(self):
		"""
		Returns if the node is a leaf.

		True: node is leaf
		False: node is inner

		Returns
        -------
		is_leaf: bool
		"""

		return self.leaf


	def merge(self, node):
		"""
		Merges the data, with the data of the merge node.

		Parameters
        ----------
		node: DataNode
		"""

		# TODO: extend merging
		# by other attributes, by finding a good way to merge
		print("merge", node.data)
		self.data += ", " + node.data


	def remove_children(self):
		"""
		TODO
		"""

		children = self.children

		self.children = None
		self.leaf = True

		return children


	def minimize_height(self, tree_height, cur_height):
		"""
		Minimize the height of this Node structure by one.

		Parameters
        ----------
		tree_height: int
		cur_height: int
		"""

		# Find merge children with node and remember
		new_children = []

		for child in self.children:
			if child.is_leaf() and ((tree_height - cur_height) == 1):
				self.merge(child)
			else:
				new_children += [child]

		if new_children != []:
			self.children = new_children
		else:
			self.children = None
			self.leaf = True

		#self.children[:] = (child for child in self.children if not(child.is_leaf and ((tree_height - cur_height) == 1)) else self.merge(child))
		if not self.is_leaf():
			for child in self.children:
				child.minimize_height(tree_height, cur_height+1)


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


	def increase_height(self, num):
		"""
		"""

		if num < 0:
			# TODO
			pass

		old_children = self.root.remove_children()

		placeholder_node = DataNode('')

		for child in old_children:
			placeholder_node.add(child)

		self.root.add(placeholder_node)

		if num > 1:
			self.increase_height(num-1)


	def minimize_height(self, num):
		"""
		TODO
		"""

		if num > self.height():
			# TODO error
			print("minimize_height", self.height(), num)
			pass

		for child in self.root.children:
			child.minimize_height(self.height(), 2)

		if num > 1:
			self.minimize_height(num-1)
