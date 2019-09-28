"""
Internal data structure for the Konbata libary.

Main idea is a data structure that can store data (of any file format)
in form of a tree. One of the main goals here is to create a DataTree.
This tree should be manipulated and serve as comfortable structure.
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
        value: str
            If value is no string, it gets transfomred in its string
            representation.
        tag: str, optional
            TODO
        children: list, optional
            list of DataNodes
        attribute: list, optional
            TODO list of additional options
        """

        if not isinstance(value, str):
            # The given value is no string and therefore gets transformed in
            # its string representation
            self.data = str(value)
        else:
            self.data = value

        # leaf is set to false in the add function
        self.leaf = True
        self.children = None

        if children and isinstance(children, list):
            for child in children:
                self.add(child)
        elif isinstance(children, DataNode):
            # Allow calls with option like children=DataNode('1')
            self.add(children)

        self.tag = tag
        self.attribute = attribute

    def add(self, node):
        """
        Adds the node to the end of the children list.

        If node dont has children, it initiates the children list.
        Changes leaf status of DataNode.

        Parameters
        ----------
        node: DataNode
        """

        if not isinstance(node, DataNode):
            raise TypeError('Node must be type of DataNode')

        if self.children is None:
            self.children = []
            self.leaf = False
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

        if self.children is None:
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
            True is returned, if node is a leaf. (False for inner nodes)
        """

        return self.leaf

    def merge(self, node, delimiter=" "):
        """
        Merges the data, with the data of the merge node.

        Parameters
        ----------
        node: DataNode
        delimiter: str, optional
            for example: delimiter=';'
        """

        # TODO: extend merging when we know more about the strucutre of other
        # file formats

        if not isinstance(delimiter, str):
            raise TypeError('Merge needs a delimiter of type str')

        self.data += delimiter + node.data

    def remove_children(self):
        """
        Removes all children of a node and returns this list of children.

        Sets children attribute of the node back to None and sets leaf to True.

        Returns
        -------
        children: list
            If node has no children, None is returned.
        """

        children = self.children

        self.children = None
        self.leaf = True

        return children

    def minimize_height(self, tree_height=None, cur_height=1):
        """
        Minimize the height of this Node structure by one.
        Only possible if node height is not one.

        Parameters
        ----------
        tree_height: int, optional
        cur_height: int, optional
            default one
        """

        if tree_height is None:
            tree_height = self.height()

        # Find merge children with node and remember
        new_children = []

        if self.children:
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

        if not self.is_leaf():
            for child in self.children:
                child.minimize_height(tree_height, cur_height+1)


class DataTree:
    """
    Class that represents the tree.

    Each tree has a root DataNode, that is the entry point of the trees data.
    """

    def __init__(self, type=None):
        """
        Initiates the current DataTree.

        Parameters
        ----------
        type: str
        """

        self.root = DataNode('FileRoot')
        self.type = type

    def height(self):
        """
        Returns the height of the tree.

        This function considers height, as the node count!
        Therefore, if empty: height() => 1
        Because there is at least the root.

        Returns
        -------
        height: int
        """

        return self.root.height()

    def increase_height(self, num):
        """
        Increases the height of the tree structure by num.

        Parameters
        ----------
        num: int
        """

        if num <= 0 or not isinstance(num, int):
            raise ValueError('num must be an positive not zero integer')

        old_children = self.root.remove_children()

        placeholder_node = DataNode("")

        for child in old_children:
            placeholder_node.add(child)

        self.root.add(placeholder_node)

        if num > 1:
            self.increase_height(num-1)

    def minimize_height(self, num):
        """
        Minimize the height of this tree structure by num.
        Only possible if node height is greater than num.

        Parameters
        ----------
        num: int
            has to be greater than tree.height()
        """

        if num > self.height() or not isinstance(num, int):
            raise ValueError("""num must be an positive not zero integer,
                                that is greater than the height of the tree""")

        for child in self.root.children:
            child.minimize_height(self.height(), 2)

        if num > 1:
            self.minimize_height(num-1)

        if num == 1 and self.height() == 2:
            self.root.minimize_height()
