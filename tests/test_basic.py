# TODO

import unittest

from Data.Data import DataNode, DataTree
from Formats.format import Format, checkTypes, getFormats
from konbata import Konbata, konbata

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
        """

        data = (1, "tag", [DataNode('child')], 'attribute')
        result = DataNode(*data)

        self.assertEqual(result.data, data[0])
        self.assertEqual(result.tag, data[1])
        self.assertEqual(result.children, data[2])
        self.assertEqual(result.attribute, data[3])

        self.assertEqual(result.height(), 2)


    def test_complex_DataNode2(self):
        """
        Test a complex DataNode with all possible attributes
        """

        data = (1, "tag", None, 'attribute')
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

        t1 = DataNode(1)
        t2 = DataNode(2, children=[DataNode(21)])

        t1.add(DataNode(11))
        t1.add(DataNode(12))

        t2.add(DataNode(22))
        t2.add(DataNode(23))

        self.assertEqual(len(t1.children), 2)
        self.assertEqual(len(t2.children), 3)

        self.assertEqual(t1.height(), 2)
        self.assertEqual(t2.height(), 2)


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
        TODO
        """
        pass


    def test_merge_DataNode(self):
        """
        TODO
        """
        pass


    def test_minimize_height_DataNode(self):
        """
        TODO
        """
        pass


class TestDataTree(unittest.TestCase):

    def test_root_DataTree(self):
        """
        Test root Node of DataTree.
        """

        t1 = DataTree()

        self.assertEqual(t1.height(), 1)
        self.assertIsNotNone(t1.root)
        self.assertEqual(t1.root.data, 'File')


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


    def test_minimize_height_DataTree(self):
        """
        TODO
        """
        pass


class TestFormats(unittest.TestCase):

    def test_fail_checkFormats(self):
        """
        Test if error got raised for not supported or empty type name.
        """

        self.assertRaises(TypeError, lambda:checkTypes(['.qqr']))
        self.assertRaises(TypeError, lambda:checkTypes(['.qqr', '.https']))


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

        self.assertRaises(TypeError, lambda:getFormats(['.qqr']))
        self.assertRaises(TypeError, lambda:getFormats(['.qqr', '.https']))


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

        self.assertRaises(Exception, Format('Fail'), 'parser and loader are needed')
        self.assertRaises(Exception, Format('Fail', loader='loader', parser='parser'), 'parser and loader cant be strings')

        def test1():
            pass

        def test2():
            pass

        result = Format('test_format', loader=test1, parser=test2)
        self.assertIsNotNone(result.loader)
        self.assertIsNotNone(result.parser)


class TestCsvFormat(unittest.TestCase):
    # csv_format TODO
    pass

class TestTxtFormat(unittest.TestCase):
    # TODO
    pass

class TestXmlFormat(unittest.TestCase):
    # TODO
    pass


class TestKonbata(unittest.TestCase):
    # TODO
    pass

if __name__ == '__main__':
    unittest.main()
