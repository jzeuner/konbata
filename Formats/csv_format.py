import format
import csv

from data import DataNode, DataTree

#===============================================================================
# Per data type there have to be two functions

def csv_toTree(file, delimiter, ignore_index=True):
	# TODO use cstore or rstore
	csv_reader = csv.reader(file, delimiter=delimiter)

	if len(csv_reader) < 0:
		# TODO EMPTY CSV
		pass

	tree = DataTree('csv')

	i = 0
	for row in csv_reader:
		row_node = DataNode('Row%s' % i)
		for col in row:
			col_node = DataNode(col)
			noder.add(col_node)
		tree.root.add(row_node)
		i += 1

	return tree

def csv_fromTree(tree):
	if tree.type == 'csv' or tree.height() == 3:
		# Table File Structure 1 to 1 dump possible
		pass
	else:
		# Height of tree needs to be flatten
		pass
