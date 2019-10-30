"""

    Konbata is a python libary, that allows you to covert a file.

    Python Version 3

    How to use:
    konbata(input_filename, output_filename)

"""

import argparse
import sys
import os
from Formats.FormatLoader import getFormats


class Konbata:
    """
    Class that represents the Konbata libary

    Gets used when the konbata function is called.
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
        formats = getFormats([in_type, out_type])

        self.input_type = formats[0]
        self.output_type = formats[1]

        # TODO check for usefull types
        self.delimiter = delimiter
        self.options = options

        self.content = None

    def format(self, in_path, out_path, delimiter=None):
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
        delimiter: str, optional
            delimiter that should be used in output format
        """

        in_filename = in_path + '.' + self.input_type.name

        if os.path.isfile(in_filename) is False:
            raise OSError('No such file: %s' % in_filename)
            exit()

        out_filename = out_path + '.' + self.output_type.name

        self.content = self.input_type.load(in_filename, delimiter)

        self.output_type.parse(self.content, out_filename, delimiter)

    def save(self, out_paths=[], out_types=[]):
        """
        Saves the previous formatted internal content to the additional
        file file_path.

        Warning: The function also overrides the output file!

        Parameters
        ----------
        output_path: str
            Complete path to the output file
        output_type: str
            .TYPE_NAME, e.g. .csv
        """

        if self.content is None:
            raise Exception("Content cannot be empty, call format before.")
            exit()

        # TODO: Right now, the function also overrides file.
        # May think of a good solution.

        # TODO Check for empty array or that len =! len

        for i in range(len(out_paths)):
            out_filename = out_paths[i] + '.' + out_types[i]

            format = getFormats([out_types[i]])[0]
            format.parse(self.content, out_filename)

    def show(self, showInternalData=True, showInputData=False,
             showOutputData=False):
        """
        Function to show the string representation of the data.

        Parameters
        ----------
        showInternalData: bool, optional
            Default: True, if true displays internal data as string
        showInputData: bool, optional
            Default: False, if true displays input data as string
        showOutputData: bool, optional
            Default: False, if true displays output data as string
        """

        if showInternalData:
            print(self.content.generate_string_representation())

        if showInputData:
            pass

        if showOutputData:
            pass

    def get(self, getInternalData=True, getInputData=False,
            getOutputData=False):
        """
        Function to get the representation of the data.

        Parameters
        ----------
        getInternalData: bool, optional
            Default: True, if true displays internal data as string
        getInputData: bool, optional
            Default: False, if true displays input data as string
        getOutputData: bool, optional
            Default: False, if true displays output data as string

        Returns
        ----------
        content: DataTree | str
            if internalData returns a DataTree or None if nothing formatted
            else returns string of inout/output data
        """
        # TODO: Extend this function in a usefull way
        if getInternalData:
            return self.content

        if getInputData:
            pass

        if getOutputData:
            pass


def konbata(input_filename, output_filename, m_save=False,
            m_save_filename=None, m_show=False, m_get=False, delimiter=None,
            options=None):
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
    m_save: bool
        If True: Saves the content in the additional file m_save_filename
        Default: False
    m_save_filename: str
        Writes the content into the file m_save_filename if m_save is true
    m_show: bool
        If True: Represents the content as a String in the Terminal
        Default: False
    m_get: bool
        If True: Returns the content as internal Data Structure
    delimiter: str, optional
        TODO: add
    options: list, optional
        TODO: add
    """

    (input_path, input_type) = os.path.splitext(input_filename)
    (output_path, output_type) = os.path.splitext(output_filename)

    k = Konbata(input_type, output_type, options)
    k.format(input_path, output_path, delimiter)

    if m_save:
        k.save(*os.path.splitext(m_save_filename))
    if m_show:
        k.show()
    if m_get:
        return k.get()


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Kanoban requires Python Version >= 3")

    parser = argparse.ArgumentParser()

    # In/Output File Path
    parser.add_argument("input_file", type=str, help="Path of input file")
    parser.add_argument("output_file", type=str, help="Path of output file")

    # Modes of the kanoban function
    # TODO add an additional file to save to
    parser.add_argument("-sa", "--save", action="store_true",
                        help="Store output file")
    parser.add_argument("-sh", "--show", action="store_true",
                        help="Show output file")
    parser.add_argument("-g", "--get", action="store_true",
                        help="Get output file")

    # Additional optional Options
    parser.add_argument("-del", "--delimiter", type=str,
                        help="Set delimiter ';'")
    parser.add_argument("-opt", "--options", type=str,
                        help="Path of option file")

    args = parser.parse_args()

    konbata(args.input_file, args.output_file,
            m_save=args.save, m_show=args.show, m_get=args.get,
            delimiter=args.delimiter, options=args.options)
