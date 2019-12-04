"""
    Loader and Parser for the xml format.

    Version: 0.01-alpha

"""

from xml.dom import minidom
from konbata.Data.Data import DataNode, DataTree
from konbata.Formats.Format import Format

def xml_toTree(file, delimiter, options=None):
    """
    Function transforms a xml file into a DataTree.

    Parameters
    ----------
    file: file
        open input file in at least read mode

    Returns
    -------
    tree: DataTree
    """

    # TODO: Second Parser with the import xml.etree.ElementTree as ET class

    xml_reader = minidom.parse(file)
    xml_reader.normalize()

    tree = DataTree(tree_type='xml')

    if xml_reader.hasChildNodes():

        for node in xml_reader.childNodes:
            childNode = help_xml_toTree(node)
            tree.root.add(childNode)

    return tree


def help_xml_toTree(xml_node):
    """
    Helps xml_ToTree function, walks through xml recursive

    Parameters
    ----------
    xml_node: ElementType1

    Returns
    -------
    node: DataNode
    """

    if xml_node.hasChildNodes():
        tree_node = DataNode(xml_node.localName)
        for node in xml_node.childNodes:
            tree_node.add(help_xml_toTree(node))
        return tree_node

    # TODO Add Attributes
    node = None
    if xml_node.nodeType == xml_node.TEXT_NODE:
        # TODO: guess xml_node.nodeValue == xml_node.data
        node = DataNode(xml_node.nodeValue.replace('\n ', ''))
    elif xml_node.nodeType == xml_node.ELEMENT_NODE:
        # TODO: guess xml_node.tagName == xml_node.localName
        node = DataNode(xml_node.localName)
    else:
        # TODO: Implement the other nodeTypes
        print('Warning: NodeType not supported yet')
        node = DataNode(xml_node.localName)
    return node


def xml_fromTree(tree, file, options=None):
    """
    Function transforms a DataTree into a xml file.

    Parameters
    ----------
    tree: DataTree
    file: file
        open output file in at least write mode
    options: list, optional
    """

    # TODO

    pass

xml_format = Format('xml', ['/n'], xml_toTree, xml_fromTree)
