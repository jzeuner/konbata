"""

    Konbata is a python libary, that allows you to covert a file.

    Python Version 3

    To use:
    konbata(input_filename, output_filename)

"""

import argparse
import sys
import os
from Formats.format import Format, getFormats

DEBUG = False # Set True to activate debug mode

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
        in_type:
        out_type:
        delimiter: , optional
        options: , optional
        """

        # Uses the Format class to get and check the data types of the files
        formats = getFormats([in_type, out_type])

        self.input_type = formats[0]
        self.output_type = formats[1]

        self.delimiter = delimiter
        self.options = options

        self.content = None


    def format(self, input_path, output_path, delimiter=None):
        """
        Transforms the input format into the output format.
        Then stores the content in the Konbata output variable.
        By loading the input file into the internal data structure.
        And then parsing the internal structure into the output format.

        Parameters
        ----------
        input_path:
        output_path:
        delimiter: , optional
        """

        if DEBUG: print(self.input_type.name, self.output_type.name)

        input_filename = input_path + '.' + self.input_type.name
        if os.path.isfile(input_filename) == False:
            raise OSError('No such file: %s' % input_filename)
            exit()

        output_filename = output_path + '.' + self.output_type.name

        # TODO: Catch errors
        input_file = open(input_filename, 'r')

        self.content = self.input_type.load(file, delimiter)
        input_file.close()

        output_file = open(output_filename, 'w')

        self.output_type.parse(self.content, output_file, delimiter)
        output_file.close()


    def save(self, file_path, file_type):
        """
        Saves the previous formatted internal content to the additional file file_path.

        Warning: The function also overrides the output file!

        Parameters
        ----------
        file_path: str
            Complete path to the output file
        """

        if self.content == None:
            raise Exception("Content cannot be empty, call format before.")
            exit()

        # TODO: Right now, the function also overrides file. May think of a good solution.

        output_filename = file_path + '.' + file_type

        output_file = open(output_filename, 'w')

        format = getFormats([file_type])[0]
        format.parse(self.content, output_file)

        output_file.close()


    def show(self):
        """
        TODO
        """
        # TODO: Think of a good way to transform the internal structure into string
        print(self.content)


    def get(self):
        """
        TODO
        """
        # TODO: Extend this function in a usefull way
        return self.content


def konbata(input_filename, output_filename, m_save=False, m_save_filename=None, m_show=False,
            m_get=False, delimiter=None, options=None):
    """
    konbata: transforms the input_file into the output_file

    Therefore it transforms the file format. It uses an internal data structure to do so.

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
        (additional_output_path, additional_output_type) = os.path.splitext(m_save_filename)
        k.save(additional_output_path, additional_output_type)
    if m_show: k.show()
    if m_get: return k.get()


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
    print(args)
    konbata(args.input_file, args.output_file,
            m_save=args.save, m_show=args.show, m_get=args.get,
            delimiter=args.delimiter, options=args.options)
