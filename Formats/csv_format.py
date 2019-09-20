"""
	Loader and Parser for the csv format
"""

import csv

from Data.Data import DataNode, DataTree

#===============================================================================
# Per data type there have to be two functions

def csv_toTree(file, delimiter, ignore_index=True, options=None):
	"""
	TODO
	"""

	# TODO add option column or row store
	csv_reader = csv.reader(file, delimiter=delimiter)

	if len(csv_reader) < 0:
		# TODO EMPTY CSV
		pass

	tree = DataTree(type='csv')

	i = 0
	for row in csv_reader:
		row_node = DataNode('Row%s' % i)
		for col in row:
			col_node = DataNode(col)
			noder.add(col_node)
		tree.root.add(row_node)
		i += 1

	csv_reader.close()

	return tree


def csv_fromTree(tree, file, options=None):
	"""
	TODO
	"""

	if tree.type != 'csv' or tree.height() != 3:
		# Height of tree needs to be flatten or need to be increased
		pass

	# Here we have a tree of the right shape
	# TODO add option append
	csv_writer = csv.writer(file)

	for row_node in tree.root.children:
		csv_writer.writerow([col_node.data for col_node in row_node.children])

	csv_writer.close()
