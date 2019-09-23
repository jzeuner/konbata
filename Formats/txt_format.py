"""
"""

from Data.Data import DataNode, DataTree

# TXT
def txt_toTree(file, delimiter=None, options=None):
	"""
	"""

	tree = DataTree(type='txt')

	# TODO catch empty file

	# TODO add more options
	for row in file.readlines():
		tree.root.add(DataNode(row))

	return tree


def txt_fromTree(tree, file, options=None):
	""
	""

	# TODO case empty tree ... or no tree
	if tree.height() != 2 or tree.type != 'txt':
		if tree.height() > 2:
			tree.minimize_height(tree.height()-2)
		elif tree.height() < 2:
			tree.increase_height(2-tree.height())


	for row_node in tree.root.children:
		file.write(row_node.data)
		file.write('\n')
