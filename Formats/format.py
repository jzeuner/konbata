from .csv_format import csv_toTree, csv_fromTree
from .txt_format import txt_toTree, txt_fromTree

import types

# Supported File Formats

TYPES = {'.csv': ('csv', [';', ','], csv_toTree, 'f', csv_fromTree, 'f'),
         '.txt': ('txt', [';', ','], txt_toTree, 'f', txt_fromTree, 'f')}


class Format:
    """
    Class that can represent and handle different file formats.

    For the set format, it can load a file into an internal data structure.
    And also parse the previous created internal structure into the set ouptut
    format.
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
            loader function that loads a file of the format into an internal
            data structure
        parser: function
            parser function that parses an internal data structure into a file
            of the format
        """

        self.name = name
        self.delimiters = delimiters

        if not isinstance(loader, types.FunctionType):
            raise TypeError('loader must be a function')

        if not isinstance(parser, types.FunctionType):
            raise TypeError('parser must be a function')

        self.loader = loader
        self.parser = parser

    def load(self, file, delimiter=None):
        """
        Uses the loader function to load a file into the internal data
        structure.

        Parameters
        ----------
        file: file
        delimiter: str, optional
            If delimiter is none the first format delimiter is used

        Returns
        -------
        content: DataTree
        """

        if delimiter is None:
            return self.loader(file, self.delimiters[0])

        if not isinstance(delimiter, str):
            raise TypeError('delimiter must be a str')

        return self.loader(file, delimiter)

    def parse(self, content, file, delimiter=None):
        """
        Uses the parser function to parse the internal data structure into the
        format.

        Parameters
        ----------
        content: DataTree
        file: file
        delimiter: str, optional
            If delimiter is none the first format delimiter is used
        """

        if delimiter is None:
            self.parser(content, file, self.delimiters[0])
        else:
            if not isinstance(delimiter, str):
                raise TypeError('delimiter must be a str')

            self.parser(content, file, delimiter)


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
        each type is a str and looks like this '.type'

    Returns
    -------
    types: list
        list of Type Objects
    """

    if not isinstance(type_names, list):
        raise TypeError('type_names must be a list')

    checkTypes(type_names)

    return [Format(*TYPES[type_name]) for type_name in type_names]
