"""
    Loader and Parser for the txt format.
"""

from konbata.Data.Data import DataNode, DataTree
from konbata.Formats.Format import Format


def txt_toTree(file, delimiter=None, options=None):
    """
    Function transforms a txt file into a DataTree.

    Parameters
    ----------
    file: file
        open input file in at least read mode
    delimiter: TODO
    options: list, optional

    Returns
    -------
    tree: DataTree
    """

    tree = DataTree(tree_type='txt')

    # TODO add more options
    for row in file.readlines():
        tree.root.add(DataNode(row))

    return tree


def txt_fromTree(tree, file, options=None):
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

    if tree.height() != 2 or tree.tree_type != 'txt':
        if tree.height() > 2:
            tree.minimize_height(tree.height()-2)
        elif tree.height() < 2:
            tree.increase_height(2-tree.height())

    for row_node in tree.root.children:
        file.write(row_node.data)
        file.write('\n')


txt_format = Format('txt', [';', ','], txt_toTree, txt_fromTree)
