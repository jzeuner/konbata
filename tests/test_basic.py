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


class TestDataTree(unittest.TestCase):
    # TODO
    pass

class TestFormats(unittest.TestCase):
    # format
    pass

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
