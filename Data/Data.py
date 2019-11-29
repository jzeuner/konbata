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

    def __init__(self, value, children=None):
        """
        Initiates the current DataNode.

        Parameters
        ----------
        value: str
            If value is no string, it gets transfomred in its string
            representation.
        children: list, optional
            list of DataNodes
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

        self.element = True
        self.tag = False
        self.attribute = False

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

    def is_element(self):
        """
        Returns if the node is a element.

        True: node is element
        False: node is tag or attribute

        Returns
        -------
        is_element: bool
            True is returned, if node is a element.
        """

        return self.element

    def is_tag(self):
        """
        Returns if the node is a tag.

        True: node is tag
        False: node is element or attribute

        Returns
        -------
        is_tag: bool
            True is returned, if node is a tag.
        """

        return self.tag

    def is_attribute(self):
        """
        Returns if the node is a attribute.

        True: node is attribute
        False: node is element or tag

        Returns
        -------
        is_attribute: bool
            True is returned, if node is a attribute.
        """

        return self.attribute

    def merge(self, node, delimiter=" "):
        """
        Merges the data, with the data of the merge node.

        Parameters
        ----------
        node: DataNode
        delimiter: str, optional
            for example: delimiter=';'
        """

        if not isinstance(delimiter, str):
            raise TypeError('Merge needs a delimiter of type str')

        self.data += delimiter + str(node)

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

    def generate_string_representation(self, i=0):
        """
        Generates string representation of the DataNode.

        Returns
        -------
        NodeRepresentation: str
        """

        TAB = "    "

        output = i*TAB + str(self) + "\n"

        if self.is_leaf():
            return output

        for children in self.children:
            output += children.generate_string_representation(i=i+1) + "\n"

        return output

    def __str__(self):
        """
        String Data of DataNode
        """

        return str(self.data)


class TagNode(DataNode):
    """
    Class that represents a TagNode.
    """

    def __init__(self, value, children=None):
        super().__init__(value, children)
        self.element = False
        self.tag = True


class AttributeNode(DataNode):
    """
    Class that represents an AttributeNode.
    """

    def __init__(self, key, value, children=None):
        super().__init__(value, children)

        if not isinstance(key, str):
            self.key = str(key)
        else:
            self.key = key

        self.element = False
        self.attribute = True

    def __str__(self):
        """
        String Data of AttributeNode
        """

        return str(self.key) + '="' + str(self.data) + '"'


class DataTree:
    """
    Class that represents the tree.

    Each tree has a root DataNode, that is the entry point of the trees data.
    """

    def __init__(self, tree_type=None):
        """
        Initiates the current DataTree.

        Parameters
        ----------
        tree_type: str
        """

        self.root = DataNode('FileRoot')
        self.tree_type = tree_type

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

        if not isinstance(num, int):
            raise TypeError('num must be an positive not zero integer')

        if num <= 0:
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

        if not isinstance(num, int):
            raise TypeError("""num must be an positive not zero integer,
                                that is greater than the height of the tree""")

        if num > self.height():
            raise ValueError("""num must be an positive not zero integer,
                                that is greater than the height of the tree""")

        for child in self.root.children:
            child.minimize_height(self.height(), 2)

        if num > 1:
            self.minimize_height(num-1)

        if num == 1 and self.height() == 2:
            self.root.minimize_height()

    def generate_string_representation(self):
        """
        Generates string representation of the DataTree.

        Returns
        -------
        TreeRepresentation: str
        """

        if self.root.is_leaf():
            return ""

        output = ""

        for children in self.root.children:
            output += children.generate_string_representation() + "\n"

        return output
