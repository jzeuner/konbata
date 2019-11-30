"""

    Konbata is a python libary, that allows you to covert a file.

    Python Version 3

    How to use:
    usage: konbata.py [-h] [-sh] [-g] [-del DELIMITER] [-opt OPTIONS]
                  input_file output_file

    positional arguments:
      input_file            Path of input file
      output_file           Path of output file

    optional arguments:
      -h, --help            show this help message and exit
      -sh, --show           Show output file
      -g, --get             Get output file
      -del DELIMITER, --delimiter DELIMITER
                            Set input delimiter: -del ';'
      -opt OPTIONS, --options OPTIONS
                            Additional Options

"""

import argparse
import sys
import os

from konbata.Formats.csv_format import csv_format
from konbata.Formats.txt_format import txt_format
from konbata.Formats.xlsx_format import xlsx_format


TYPES = {'.csv': csv_format,
         '.txt': txt_format,
         '.xlsx': xlsx_format}


class Konbata:
    """
    Class that represents the Konbata libary

    Get used when the konbata function is called.
    Interface that should be used by the user.
    """

    def __init__(self, in_type, out_type, delimiter=None, options=None):
        """
        Initiates the current call of the konbata libary.

        Parameters
        ----------
        in_type: str
            .TYPE_NAME, e.g. .csv
        out_type: str
            .TYPE_NAME, e.g. .csv
        delimiter: str, optional
            Delimiter that should be used for encoding, e.g. ';'
        options: , optional
            TODO
        """

        # Uses the Format class to get and check the data types of the files
        formats = self.get_formats([in_type, out_type])

        self.input_type = formats[0]
        self.output_type = formats[1]

        # TODO check for usefull types
        self.delimiter = delimiter
        self.options = options

        self.content = None

    def convert(self, in_path, out_path):
        """
        Transforms the input format into the output format.
        Then stores the content in the Konbata output variable.
        By loading the input file into the internal data structure.
        And then parsing the internal structure into the output format.

        Parameters
        ----------
        input_path: str
            path to file without file type ending
        output_path: str
            path to file without file type ending
        """

        in_filename = in_path + '.' + self.input_type.name

        if os.path.isfile(in_filename) is False:
            raise OSError('No such file: %s' % in_filename)

        out_filename = out_path + '.' + self.output_type.name

        self.content = self.input_type.load(in_filename, self.delimiter)

        self.output_type.parse(self.content, out_filename)

    def show(self):
        """
        Function to show the string representation of the intern data.
        """

        print(self.content.generate_string_representation())

    def get(self):
        """
        Function to get the representation of the intern data.

        Returns
        ----------
        content: DataTree
        """

        return self.content

    def check_types(self, type_names=None):
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

    def get_formats(self, type_names=None):
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

        self.check_types(type_names)

        return [TYPES[type_name] for type_name in type_names]


def konbata(input_filename, output_filename,
            m_show=False, m_get=False, delimiter=None, options=None):
    """
    konbata: transforms the input_file into the output_file

    Therefore it transforms the file format. It uses an internal data structure
    to do so.

    Parameters
    ----------
    input_filename: str
        Complete path of the input file
    output_filename: str
        Complete path of the output file
    m_show: bool
        If True: Represents the content as a String in the Terminal
        Default: False
    m_get: bool
        If True: Returns the content as internal Data Structure
    delimiter: str, optional
        Delimiter of the input file
    options: list, optional
        TODO: add
    """

    (input_path, input_type) = os.path.splitext(input_filename)
    (output_path, output_type) = os.path.splitext(output_filename)

    k = Konbata(input_type, output_type, delimiter, options)
    k.convert(input_path, output_path)

    if m_show:
        k.show()

    if m_get:
        return k.get()


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Kanoban requires Python Version >= 3")

    PARSER = argparse.ArgumentParser()

    # In/Output File Path
    PARSER.add_argument("input_file", type=str, help="Path of input file")
    PARSER.add_argument("output_file", type=str, help="Path of output file")

    # Additional functions
    PARSER.add_argument("-sh", "--show", action="store_true",
                        help="Show output file")
    PARSER.add_argument("-g", "--get", action="store_true",
                        help="Get output file")

    # Additional Options
    PARSER.add_argument("-del", "--delimiter", type=str, default=None,
                        help="Set input delimiter: -del ';'")
    PARSER.add_argument("-opt", "--options", type=str, default=None,
                        help="Additional Options")

    ARGS = PARSER.parse_args()

    konbata(ARGS.input_file, ARGS.output_file,
            m_show=ARGS.show, m_get=ARGS.get,
            delimiter=ARGS.delimiter, options=ARGS.options)
