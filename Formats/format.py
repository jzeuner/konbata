from csv_format import csv_loader, csv_parser
from txt_format import txt_loader, txt_parser

# Supported File Formats

TYPES = {'.csv': ('csv', [';', ','], loader= csv_loader, parser=csv_parser),
         '.txt': ('txt', [';', ','], loader=txt_loader, parser=txt_parser)}

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
        file: str
        delimiter: list, optional

        Returns
        -------
        DataTree
        """

        if delimiter != None:
            return self.loader(file, delimiter)

        return self.loader(file, self.delimiters[0])


    def parse(self, content, delimiter=None):
        """
        Uses the parser function to parse the internal data structure into the format.

        Parameters
        ----------
        content: DataTree
        delimiter: list, optional

        """

        if delimiter != None:
            return self.parser(content, delimiter)

        return self.parser(content, self.delimiters[0])


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

    return [Format(TYPES[type_name]) for type_name in type_names]
