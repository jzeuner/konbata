"""
	Loader and Parser for the csv format.

	CSV files have different options (a Dialect)
	also see https://docs.python.org/3/library/csv.html#csv.Dialect
		delimiter
		doublequote
		escapechar
		lineterminator
		quotechar
		quoting
		skipinitialspace
		strict
"""

import csv
from Data.Data import DataNode, DataTree


def csv_toTree(file, delimiter, ignore_index=True, options=None):
	"""
	TODO
	"""

	# TODO add option column or row store
	csv_reader = csv.reader(file, delimiter=delimiter)

	if csv_reader.line_num <= 0:
		# TODO EMPTY CSV
		pass

	tree = DataTree(type='csv')

	i = 0
	for row in csv_reader:
		row_node = DataNode('Row%s' % i)
		for col in row:
			col_node = DataNode(col)
			row_node.add(col_node)
		tree.root.add(row_node)
		i += 1

	return tree


def csv_fromTree(tree, file, options=None):
	"""
	TODO
	"""
	# TODO case empty tree ... or no tree
	print(tree.height())
	if tree.type != 'csv' or tree.height() != 3:
		# Height of tree needs to be flatten or need to be increased
		if tree.height() > 3:
			tree.minimize_height(tree.height()-3)
		elif tree.height() < 3:
			print('increase', 3-tree.height())
			tree.increase_height(3-tree.height())

	# Here we have a tree of the right shape
	# TODO add option append
	csv_writer = csv.writer(file)

	for row_node in tree.root.children:
		csv_writer.writerow([col_node.data for col_node in row_node.children])
