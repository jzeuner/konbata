# TODO

import unittest

from data import DataNode, DataTree
from formats import Format, checkTypes, getFormats
from konbata import Konbata, konbata

class TestDataNode(unittest.TestCase):

    def test_simple_DataNode(self):
    """
    Test a simple DataNode with only a value attribute
    """
        data = "1"
        result = DataNode(data)

        self.assertEqual(DataNode.data, data)
        self.assertEqual(DataNode.tag, None)
        self.assertEqual(DataNode.children, None)
        self.assertEqual(DataNode.attribute, None)

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
