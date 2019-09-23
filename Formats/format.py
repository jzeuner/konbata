from .csv_format import csv_toTree, csv_fromTree
from .txt_format import txt_toTree, txt_fromTree

# Supported File Formats

TYPES = {'.csv': ('csv', [';', ','], csv_toTree, csv_fromTree),
         '.txt': ('txt', [';', ','], txt_toTree, txt_fromTree)}

class Format:
    """
    Class that represents and handles different file formats.

    For the set format, it can load a file into an internal data structure.
    And also parse the previous created internal structure into the set ouptut format.
    """

    def __init__(self, name, delimiters=[], loader=None, parser=None):
        """
        Initiates the Format class.

        Parameters
        ----------
        name: str
            Name of the Format
        delimiters: list
            List of all supported delimiters
        loader: function
            loader function that loads a file of the format into an internal data structure
        parser: function
            parser function that parses an internal data structure into a file of the format
        """

        self.name = name
        self.delimiters = delimiters
        self.loader = loader
        self.parser = parser


    def load(self, file, delimiter=None):
        """
        Uses the loader function to load a file into the internal data structure.

        Parameters
        ----------
        file: file
        delimiter: list, optional

        Returns
        -------
        DataTree
        """

        if delimiter != None:
            return self.loader(file, delimiter)

        return self.loader(file, self.delimiters[0])


    def parse(self, content, file, delimiter=None):
        """
        Uses the parser function to parse the internal data structure into the format.

        Parameters
        ----------
        content: DataTree
        file: file
        delimiter: list, optional

        """

        if delimiter != None:
            self.parser(content, file, delimiter)
        else:
            self.parser(content, file, self.delimiters[0])


def checkTypes(type_names=[]):
    """
    Cheks if a list of types is supported by the tool.
    If not supported it raises a TypeError exception.

    Parameters
    ----------
    type_names: list
    """

    for type_name in type_names:
        if type_name not in TYPES:
            raise TypeError('Type %s not supported.' % type_name)
            exit()


def getFormats(type_names=[]):
    """
    Generates a list of formats to a list of type names.

    Parameters
    ----------
    type_names: list
    """

    checkTypes(type_names)

    return [Format(*TYPES[type_name]) for type_name in type_names]
