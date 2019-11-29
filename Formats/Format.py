"""
    Format Class that represents hierarcical file format.

    With individual functions, the format can be parsed into the internal
    data representation or such an representation can be reloaded into the
    individual format.
"""

import types


class Format:
    """
    Class that can represent and handle different file formats.

    For the set format, it can load a file into an internal data structure.
    And also parse the previous created internal structure into the set ouptut
    format.
    """

    def __init__(self, name, delimiters=[], loader=None, parser=None,
                 pre_open=True):
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
        pre_open: bool, optional
            default: if true parser and loader functions are getting an opened
            file; Else the path to the file is submitted
        """

        self.name = name
        self.delimiters = delimiters

        if not isinstance(loader, types.FunctionType):
            raise TypeError('loader must be a function')

        if not isinstance(parser, types.FunctionType):
            raise TypeError('parser must be a function')

        self.loader = loader
        self.parser = parser

        self.pre_open = pre_open

    def load(self, path, delimiter=None):
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
            delimiter = self.delimiters[0]

        if not isinstance(delimiter, str):
            raise TypeError('delimiter must be a str')

        if not self.pre_open:
            return self.loader(path, delimiter)

        in_file = open(path, 'r')

        output = self.loader(in_file, delimiter)

        in_file.close()

        return output

    def parse(self, content, path, delimiter=None):
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
            delimiter = self.delimiters[0]

        if not isinstance(delimiter, str):
            raise TypeError('delimiter must be a str')

        if not self.pre_open:
            self.parser(content, path, delimiter)
            return

        out_file = open(path, 'w', newline='')

        self.parser(content, out_file, delimiter)

        out_file.close()
