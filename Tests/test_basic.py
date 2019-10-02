"""
TODO Add more Test functions and Test cases
"""

import unittest
from io import StringIO

from konbata import Konbata
from Data.Data import DataNode, DataTree
from Formats.format import Format, checkTypes, getFormats
from Formats.csv_format import csv_toTree, csv_fromTree
from Formats.txt_format import txt_toTree, txt_fromTree

# Constants
PATH_INPUT_FILES = "./Tests/test_files/"


class TestDataNode(unittest.TestCase):

    def test_simple_DataNode(self):
        """
        Test a simple DataNode with only a value attribute
        """

        data = "1"
        result = DataNode(data)

        self.assertEqual(result.data, data)
        self.assertEqual(result.tag, None)
        self.assertEqual(result.children, None)
        self.assertEqual(result.attribute, None)

    def test_complex_DataNode1(self):
        """
        Test a complex DataNode with all possible attributes

        Single child
        """

        data = ('1', "tag", DataNode('child'), 'attribute')

        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.tag, data[1])
        self.assertEqual(result.children, [data[2]])
        self.assertEqual(result.attribute, data[3])
        self.assertEqual(result.height(), 2)

    def test_complex_DataNode2(self):
        """
        Test a complex DataNode with all possible attributes

        List of childs
        """

        data = ('1', "tag", [DataNode('child')], 'attribute')

        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.tag, data[1])
        self.assertEqual(result.children, data[2])
        self.assertEqual(result.attribute, data[3])
        self.assertEqual(result.height(), 2)

    def test_complex_DataNode3(self):
        """
        Test a complex DataNode with all possible attributes
        """

        data = ('1', "tag", None, 'attribute')
        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.tag, data[1])
        self.assertEqual(result.children, None)
        self.assertEqual(result.attribute, data[3])

        self.assertEqual(result.height(), 1)

    def test_add_DataNode(self):
        """
        Test add function of DataNode.
        """

        t1 = DataNode('1')
        t2 = DataNode('2', children=[DataNode(21)])

        t1.add(DataNode(11))
        t1.add(DataNode(12))

        t2.add(DataNode(22))
        t2.add(DataNode(23))

        self.assertEqual(len(t1.children), 2)
        self.assertEqual(len(t2.children), 3)

        self.assertEqual(t1.height(), 2)
        self.assertEqual(t2.height(), 2)

    def test_add_DataNode2(self):
        """
        Test add function of DataNode.

        Test fail of add function
        """

        t1 = DataNode('1')
        self.assertRaises(TypeError, lambda: t1.add("DataNode"))

    def test_height_DataNode(self):
        """
        Test height function of DataNode.
        """

        t1 = DataNode(1)
        self.assertEqual(t1.height(), 1)

        t1.add(DataNode(11))
        self.assertEqual(t1.height(), 2)

    def test_is_leaf_DataNode(self):
        """
        Test is_leaf function of DataNode.
        """

        t1 = DataNode(1)
        self.assertEqual(t1.is_leaf(), True)

        t2 = DataNode(2)
        t1.add(t2)
        self.assertEqual(t1.is_leaf(), False)
        self.assertEqual(t2.is_leaf(), True)

    def test_merge_DataNode(self):
        """
        Test merge function.

        With correct delimiter.
        """

        t1 = DataNode('1')
        t2 = DataNode('2')

        self.assertEqual(t1.data, "1")

        t1.merge(t2)

        self.assertEqual(t1.data, "1 2")

        t1.merge(t2, ";")

        self.assertEqual(t1.data, "1 2;2")

    def test_merge_DataNode2(self):
        """
        Test merge function.

        With wrong delimiter.
        """

        t1 = DataNode('1')
        t2 = DataNode('2')

        self.assertRaises(TypeError, lambda: t1.merge(t2, 3))

    def test_remove_children_DataNode(self):
        """
        Test remove_children function of DataNode.
        """

        # Test it with t1 having children
        t1 = DataNode('t1')
        t2 = DataNode('t2')

        t1.add(t2)

        self.assertEqual(t1.is_leaf(), False)
        self.assertEqual(t2.is_leaf(), True)
        self.assertIsNotNone(t1.children)

        result = t1.remove_children()

        self.assertIsNotNone(result)
        self.assertEqual(type(result), type([]))
        self.assertEqual(len(result), 1)
        self.assertEqual(t1.children, None)

        # Testing it with t1 having no children
        self.assertEqual(None, t1.remove_children())

    def test_minimize_height_DataNode(self):
        """
        Test minimize_height function of DataNode.
        """

        t1, t2, t3 = DataNode('1'), DataNode('2'), DataNode('3')

        t1.add(t2)
        t2.add(t3)

        self.assertEqual(t1.height(), 3)

        t1.minimize_height()
        self.assertEqual(t1.height(), 2)

        t1.minimize_height()
        self.assertEqual(t1.height(), 1)

        # TODO test call with tree_height and cur_height


class TestDataTree(unittest.TestCase):

    def test_root_DataTree(self):
        """
        Test root Node of DataTree.
        """

        t1 = DataTree()

        self.assertEqual(t1.height(), 1)
        self.assertIsNotNone(t1.root)
        self.assertEqual(t1.root.data, 'FileRoot')

    def test_simpleDataTree(self):
        """
        Test Creation of simple DataTree.
        """

        t1 = DataTree('type')

        self.assertEqual(t1.type, 'type')

        d1 = DataNode(1)
        d2 = DataNode(2)
        d3 = DataNode(3)

        t1.root.add(d1)
        d1.add(d2)
        d2.add(d3)

        self.assertEqual(t1.height(), 4)
        self.assertIsNotNone(t1.root.children)

    def test_height_DataTree(self):
        """
        Test height function of DataTree.
        """

        t1 = DataTree()

        self.assertEqual(t1.height(), 1)

        d1 = DataNode(1)
        d2 = DataNode(2)
        d3 = DataNode(3)
        d4 = DataNode(4)

        t1.root.add(d1)
        self.assertEqual(t1.height(), 2)
        d1.add(d2)
        self.assertEqual(t1.height(), 3)
        d2.add(d3)
        self.assertEqual(t1.height(), 4)
        t1.root.add(d4)
        self.assertEqual(t1.height(), 4)

    def test_increase_height_DataTree(self):
        """
        Test increase_height function of DataTree.
        """

        t1 = DataTree()

        self.assertEqual(t1.height(), 1)

        d1 = DataNode(1)
        d2 = DataNode(2)

        t1.root.add(d1)
        d1.add(d2)

        self.assertEqual(t1.height(), 3)

        t1.increase_height(1)

        self.assertEqual(t1.height(), 4)

        t1.increase_height(4)

        self.assertEqual(t1.height(), 8)

        self.assertRaises(TypeError, lambda: t1.increase_height('3'))
        self.assertRaises(ValueError, lambda: t1.increase_height(-4))

    def test_minimize_height_DataTree(self):
        """
        Test minimize_height function of DataTree.
        """

        t1 = DataTree()

        self.assertEqual(t1.height(), 1)

        d1 = DataNode(1)
        d2 = DataNode(2)
        d3 = DataNode(3)
        d4 = DataNode(4)

        t1.root.add(d1)
        d1.add(d2)
        d2.add(d3)
        d3.add(d4)

        self.assertEqual(t1.height(), 5)

        t1.minimize_height(1)
        self.assertEqual(t1.height(), 4)

        t1.minimize_height(3)
        self.assertEqual(t1.height(), 1)

        self.assertRaises(ValueError, lambda: t1.minimize_height(7))
        self.assertRaises(TypeError, lambda: t1.minimize_height('3'))


class TestFormats(unittest.TestCase):

    def test_fail_checkFormats(self):
        """
        Test if error got raised for not supported or empty type name.
        """

        self.assertRaises(TypeError, lambda: checkTypes(['.qqr']))
        self.assertRaises(TypeError, lambda: checkTypes(['.qqr', '.https']))

    def test_checkFormats(self):
        """
        Test supported types.
        """

        try:
            checkTypes([])
            checkTypes(['.csv'])
            checkTypes(['.txt'])
            checkTypes(['.csv', '.txt'])
        except TypeError:
            self.fail()

    def test_fail_getFormats(self):
        """
        Test the getFormats function with not supported types.
        """

        self.assertRaises(TypeError, lambda: getFormats(['.qqr']))
        self.assertRaises(TypeError, lambda: getFormats(['.qqr', '.https']))

    def test_getFormats(self):
        """
        Test the getFormats function with supported types.
        """
        result = getFormats(['.txt', '.csv'])

        self.assertEqual(type(result), type([]))
        self.assertEqual(len(result), 2)

        for r in result:
            self.assertIsNotNone(r.loader)
            self.assertIsNotNone(r.parser)

    def test_Format(self):
        """
        Test wrong use of Format creation and one creation with two functions.
        """

        self.assertRaises(TypeError, lambda: Format('Fail'))
        self.assertRaises(TypeError, lambda: Format('Fail',
                          loader='loader', parser='parser'))

        def test1():
            pass

        def test2():
            pass

        result = Format('test_format', loader=test1, parser=test2)
        self.assertIsNotNone(result.loader)
        self.assertIsNotNone(result.parser)


class TestCsvFormat(unittest.TestCase):

    def test_csv_toTree(self):
        """
        Test the csv to DataTree function.
        """

        with open(PATH_INPUT_FILES + 'input_test.csv', 'r') as inputfile:
            tree = csv_toTree(inputfile, ',')

        inputfile.close()

        self.assertIsNotNone(tree)
        self.assertEqual(tree.type, 'csv')
        self.assertEqual(tree.height(), 3)

        self.assertIsNotNone(tree.root.children)

        for child in tree.root.children:
            self.assertIsNotNone(child.children)
            self.assertEqual(child.height(), 2)
            self.assertEqual(len(child.children), 3)

    def test_csv_fromTree(self):
        """
        Test the DataTree to csv function.
        """

        # Prepare DataTree
        row0 = DataNode('Row0', children=[DataNode('Col1'), DataNode('Col2'),
                                          DataNode('Col3')])
        row1 = DataNode('Row1', children=[DataNode('Row11'), DataNode('Row12'),
                                          DataNode('Row13')])
        row2 = DataNode('Row2', children=[DataNode('Row21'), DataNode('Row22'),
                                          DataNode('Row23')])
        row3 = DataNode('Row3', children=[DataNode('Row31'), DataNode('Row32'),
                                          DataNode('Row33')])
        row4 = DataNode('Row4', children=[DataNode('Row41'), DataNode('Row42'),
                                          DataNode('Row43')])

        tree = DataTree(type='csv')
        tree.root.add(row0)
        tree.root.add(row1)
        tree.root.add(row2)
        tree.root.add(row3)
        tree.root.add(row4)

        # Run function
        outfile = StringIO()

        csv_fromTree(tree, outfile)

        outfile.seek(0)
        content = outfile.read()

        with open(PATH_INPUT_FILES + 'input_test.csv', 'r') as inputfile:
            real_content = inputfile.readlines()

        inputfile.close()

        self.assertEqual(content, ''.join(real_content).replace('\n', '\r\n'))


class TestTxtFormat(unittest.TestCase):
    # TODO

    def test_txt_toTree(self):
        """
        Test the txt to DataTree function.
        """

        with open(PATH_INPUT_FILES + 'input_test.txt', 'r') as inputfile:
            tree = txt_toTree(inputfile)

        inputfile.close()

        self.assertIsNotNone(tree)
        self.assertEqual(tree.type, 'txt')
        self.assertEqual(tree.height(), 2)

        self.assertIsNotNone(tree.root.children)

        for child in tree.root.children:
            self.assertIsNotNone(child.data)
            self.assertEqual(child.height(), 1)

    def test_txt_fromTree(self):
        """
        Test the DataTree to txt function.
        """

        """
        Test the DataTree to csv function.
        """

        # Prepare DataTree
        row0 = DataNode('Row0')
        row1 = DataNode('Row1')
        row2 = DataNode('Row2')
        row3 = DataNode('Row3')
        row4 = DataNode('Row4')

        tree = DataTree(type='txt')
        tree.root.add(row0)
        tree.root.add(row1)
        tree.root.add(row2)
        tree.root.add(row3)
        tree.root.add(row4)

        # Run function
        outfile = StringIO()

        txt_fromTree(tree, outfile)

        outfile.seek(0)
        content = outfile.read()

        with open(PATH_INPUT_FILES + 'input_test.txt', 'r') as inputfile:
            real_content = inputfile.readlines()

        inputfile.close()

        self.assertEqual(content, ''.join(real_content))


class TestXmlFormat(unittest.TestCase):
    # TODO
    pass


class TestXlsxFormat(unittest.TestCase):
    # TODO
    pass


class TestKonbata(unittest.TestCase):
    # TODO

    def test_simple_Konbata(self):
        """
        Test simple initialization of Konbata
        """

        result = Konbata('.csv', '.txt', None, None)

        self.assertIsNotNone(result.input_type)
        self.assertIsNotNone(result.output_type)

        self.assertEqual(result.delimiter, None)
        self.assertEqual(result.options, None)
        self.assertEqual(result.content, None)

    def test_complex_Konbata(self):
        """
        Test more complex initialization of Konbata
        """

        result = Konbata('.csv', '.txt', ";", ['1', '2'])

        self.assertIsNotNone(result.input_type)
        self.assertIsNotNone(result.output_type)

        self.assertEqual(result.delimiter, ";")
        self.assertEqual(result.options, ['1', '2'])
        self.assertEqual(result.content, None)

    def test_format_Konbata(self):
        """
        TODO find a good way to test this
        """
        pass

    def test_save_Konbata(self):
        """
        TODO find a good way to test this
        """
        pass

    def test_show_Konbata(self):
        """
        """
        pass

    def test_get_Konbata(self):
        """
        """
        pass

    def test_konbata(self):
        """
        """
        pass


if __name__ == '__main__':
    unittest.main()