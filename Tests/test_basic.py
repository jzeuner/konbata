"""
    Basic Test Suite for the Konbata.py Project
"""

import unittest
import os
from io import StringIO

from konbata.konbata import Konbata
from konbata.Data.Data import DataNode, TagNode, AttributeNode, DataTree
from konbata.Formats.Format import Format
from konbata.Formats.csv_format import csv_toTree, csv_fromTree
from konbata.Formats.txt_format import txt_toTree, txt_fromTree
from konbata.Formats.xlsx_format import xlsx_toTree, xlsx_fromTree

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
        self.assertEqual(result.children, None)

    def test_complex_DataNode1(self):
        """
        Test a complex DataNode with all possible attributes

        Single child
        """

        data = ('1', DataNode('child'))

        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.children, [data[1]])
        self.assertEqual(result.height(), 2)

    def test_complex_DataNode2(self):
        """
        Test a complex DataNode with all possible attributes

        List of childs
        """

        data = ('1', [DataNode('child')])

        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.children, data[1])
        self.assertEqual(result.height(), 2)

    def test_complex_DataNode3(self):
        """
        Test a complex DataNode with all possible attributes
        """

        data = ('1', None)
        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.children, None)

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

    def test_is_element_DataNode(self):
        """
        Test is_element function of DataNode.
        """
        t1 = DataNode(1)
        self.assertEqual(t1.is_element(), True)

    def test_is_tag_DataNode(self):
        """
        Test is_tag function of DataNode.
        """
        t1 = DataNode(1)
        self.assertEqual(t1.is_tag(), False)

    def test_is_attribute_DataNode(self):
        """
        Test is_attribute function of DataNode.
        """
        t1 = DataNode(1)
        self.assertEqual(t1.is_attribute(), False)

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

    def test_generate_string_representation_DataNode(self):
        """
        TODO
        """
        pass

    def test___str___DataNode(self):
        """
        Test __str__ function of DataNode.
        """

        t1 = DataNode("1")
        self.assertEqual(str(t1), "1")


class TestTagNode(unittest.TestCase):

    def test_simple_TagNode(self):
        """
        Test a simple TagNode with only a value attribute
        """

        tag = "1"
        result = TagNode(tag)

        self.assertEqual(result.data, tag)
        self.assertEqual(result.children, None)

    def test_complex_TagNode1(self):
        """
        Test a complex TagNode with all possible attributes

        Single child
        """

        data = ('1', DataNode('child'))

        result = TagNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.children, [data[1]])
        self.assertEqual(result.height(), 2)

    def test_is_element_TagNode(self):
        """
        Test is_element function of TagNode.
        """
        t1 = TagNode(1)
        self.assertEqual(t1.is_element(), False)

    def test_is_tag_TagNode(self):
        """
        Test is_tag function of TagNode.
        """
        t1 = TagNode(1)
        self.assertEqual(t1.is_tag(), True)

    def test_is_attribute_TagNode(self):
        """
        Test is_attribute function of TagNode.
        """
        t1 = TagNode(1)
        self.assertEqual(t1.is_attribute(), False)

    def test_valid_other_functions_TagNode(self):
        """
        Test if TagNode has same functions as DataNode.

        Functionallity is tested in TestDataNode
        """

        t1 = TagNode(1)

        # add()
        t1.add(DataNode('2'))
        self.assertIsNotNone(t1.children)

        # height()
        self.assertIsNotNone(t1.height())

        # is_leaf()
        self.assertIsNotNone(t1.is_leaf())

        # remove_children()
        self.assertIsNotNone(t1.remove_children())

        # minimize_height()
        t1.minimize_height()

        # generate_string_representation()
        self.assertIsNotNone(t1.generate_string_representation())

        # __str__()
        self.assertIsNotNone(str(t1))


class TestAttributeNode(unittest.TestCase):

    def test_simple_AttributeNode(self):
        """
        Test a simple AttributeNode with only a value attribute
        """

        key, value = "1", "2"
        result = AttributeNode(key, value)

        self.assertEqual(result.key, key)
        self.assertEqual(result.data, value)
        self.assertEqual(result.children, None)

    def test_complex_AttributeNode1(self):
        """
        Test a complex AttributeNode with all possible attributes

        Single child
        """

        data = ("1", "2", DataNode('child'))

        result = AttributeNode(*data)

        self.assertEqual(result.key, data[0])
        self.assertEqual(result.data, data[1])
        self.assertEqual(result.children, [data[2]])
        self.assertEqual(result.height(), 2)

    def test_complex_AttributeNode2(self):
        """
        Test a complex AttributeNode with all possible attributes

        No String key and value
        """

        data = (1, 2, DataNode('child'))

        result = AttributeNode(*data)

        self.assertEqual(result.key, str(data[0]))
        self.assertEqual(result.data, str(data[1]))
        self.assertEqual(result.children, [data[2]])
        self.assertEqual(result.height(), 2)

    def test_is_element_AttributeNode(self):
        """
        Test is_element function of AttributeNode.
        """
        t1 = AttributeNode("1", "2")
        self.assertEqual(t1.is_element(), False)

    def test_is_tag_AttributeNode(self):
        """
        Test is_tag function of AttributeNode.
        """
        t1 = AttributeNode("1", "2")
        self.assertEqual(t1.is_tag(), False)

    def test_is_attribute_AttributeNode(self):
        """
        Test is_attribute function of AttributeNode.
        """
        t1 = AttributeNode("1", "2")
        self.assertEqual(t1.is_attribute(), True)

    def test_valid_other_functions_AttributeNode(self):
        """
        Test if AttributeNode has same functions as DataNode.

        Functionallity is tested in TestDataNode
        """

        t1 = AttributeNode("1", "2")

        # add()
        t1.add(DataNode('2'))
        self.assertIsNotNone(t1.children)

        # height()
        self.assertIsNotNone(t1.height())

        # is_leaf()
        self.assertIsNotNone(t1.is_leaf())

        # remove_children()
        self.assertIsNotNone(t1.remove_children())

        # minimize_height()
        t1.minimize_height()

        # generate_string_representation()
        self.assertIsNotNone(t1.generate_string_representation())

        # __str__()
        self.assertIsNotNone(str(t1))

    def test___str___AttributeNode(self):
        """
        Test __str__ function of AttributeNode.
        """

        t1 = AttributeNode("1", "2")
        self.assertEqual(str(t1), '1="2"')


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

        self.assertEqual(t1.tree_type, 'type')

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

    def test_generate_string_representation_DataTree(self):
        """
        TODO
        """
        pass


class TestFormats(unittest.TestCase):

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
        self.assertEqual(tree.tree_type, 'csv')
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

        tree = DataTree(tree_type='csv')
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

    def test_txt_toTree(self):
        """
        Test the txt to DataTree function.
        """

        with open(PATH_INPUT_FILES + 'input_test.txt', 'r') as inputfile:
            tree = txt_toTree(inputfile)

        inputfile.close()

        self.assertIsNotNone(tree)
        self.assertEqual(tree.tree_type, 'txt')
        self.assertEqual(tree.height(), 2)

        self.assertIsNotNone(tree.root.children)

        for child in tree.root.children:
            self.assertIsNotNone(child.data)
            self.assertEqual(child.height(), 1)

    def test_txt_fromTree(self):
        """
        Test the DataTree to txt function.
        """

        # Prepare DataTree
        row0 = DataNode('Row0')
        row1 = DataNode('Row1')
        row2 = DataNode('Row2')
        row3 = DataNode('Row3')
        row4 = DataNode('Row4')

        tree = DataTree(tree_type='txt')
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

    def test_xlsx_toTree(self):
        """
        Test the xlsx to DataTree function.
        """

        tree = xlsx_toTree(PATH_INPUT_FILES + 'input_test.xlsx')

        self.assertIsNotNone(tree)
        self.assertEqual(tree.tree_type, 'xlsx')
        self.assertEqual(tree.height(), 4)

        self.assertIsNotNone(tree.root.children)

        for child in tree.root.children:
            self.assertIsNotNone(child.children)
            self.assertEqual(child.height(), 3)
            self.assertEqual(len(child.children), 4)

    def test_xlsx_fromTree(self):
        """
        Test the DataTree to xlsx function.
        """

        # TODO: Test for right output

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

        tree = DataTree(tree_type='xlsx')
        tree.root.add(row0)
        tree.root.add(row1)
        tree.root.add(row2)
        tree.root.add(row3)
        tree.root.add(row4)

        f = open(PATH_INPUT_FILES + 'output_test.xlsx', "w+")
        f.close()

        xlsx_fromTree(tree, PATH_INPUT_FILES + 'output_test.xlsx')

        os.remove(PATH_INPUT_FILES + 'output_test.xlsx')


class TestKonbata(unittest.TestCase):

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

    def test_fail_checkFormats(self):
        """
        Test if error got raised for not supported or empty type name.
        """

        k = Konbata('.csv', '.txt', ";", ['1', '2'])

        self.assertRaises(TypeError, lambda: k.check_types(['.qqr']))
        self.assertRaises(TypeError, lambda: k.check_types(['.qqr', '.https']))

    def test_checkFormats(self):
        """
        Test supported types.
        """

        k = Konbata('.csv', '.txt', ";", ['1', '2'])

        try:
            k.check_types([])
            k.check_types(['.csv'])
            k.check_types(['.txt'])
            k.check_types(['.csv', '.txt'])
        except TypeError:
            self.fail()

    def test_fail_get_formats(self):
        """
        Test the get_formats function with not supported types.
        """

        k = Konbata('.csv', '.txt', ";", ['1', '2'])

        self.assertRaises(TypeError, lambda: k.get_formats(['.qqr']))
        self.assertRaises(TypeError, lambda: k.get_formats(['.qqr', '.https']))

    def test_get_formats(self):
        """
        Test the get_formats function with supported types.
        """

        k = Konbata('.csv', '.txt', ";", ['1', '2'])

        result = k.get_formats(['.txt', '.csv'])

        self.assertEqual(type(result), type([]))
        self.assertEqual(len(result), 2)

        for r in result:
            self.assertIsNotNone(r.loader)
            self.assertIsNotNone(r.parser)

    def test_format_Konbata(self):
        """
        TODO find a good way to test this
        """
        pass

    def test_show_Konbata(self):
        """
        TODO
        """
        pass

    def test_get_Konbata(self):
        """
        TODO
        """
        pass

    def test_konbata(self):
        """
        TODO
        """
        pass


if __name__ == '__main__':
    unittest.main()
