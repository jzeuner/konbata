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
from konbata.Data.Data import DataNode, DataTree
from konbata.Formats.Format import Format


def csv_toTree(file, delimiter, ignore_index=True, options=None):
    """
    Function transforms a csv file into a DataTree.

    Parameters
    ----------
    file: file
        open input file in at least read mode
    delimiter: str
    ignore_index: bool, optional
    options: list, optional

    Returns
    -------
    tree: DataTree
    """

    # TODO add option column or row store
    csv_reader = csv.reader(file, delimiter=delimiter)

    tree = DataTree(tree_type='csv')

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
    Function transforms a DataTree into a csv file.

    Parameters
    ----------
    tree: DataTree
    file: file
        open output file in at least write mode
    options: list, optional
    """

    if not isinstance(tree, DataTree):
        raise TypeError('tree must be type of DataTree')

    if tree.tree_type != 'csv' or tree.height() != 3:
        # Height of tree needs to be flatten or need to be increased
        if tree.height() > 3:
            tree.minimize_height(tree.height()-3)
        elif tree.height() < 3:
            tree.increase_height(3-tree.height())

    # Here we have a tree of the right shape
    # TODO add option append
    csv_writer = csv.writer(file)

    for row_node in tree.root.children:
        csv_writer.writerow([col_node.data for col_node in row_node.children])


csv_format = Format('csv', [';', ','], csv_toTree, csv_fromTree)
