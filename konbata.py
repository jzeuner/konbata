"""
TODO
"""
import argparse
import sys
import os
from Formats.format import Format, getFormats


class Konbata:
    """
    TODO
    """
    def __init__(self, in_type, out_type, delimiter=None, options=None):
        """
        TODO
        """
        # Check for invalid/not supported data types
        formats = getFormats([in_type, out_type])

        self.input_type = formats[0]
        self.output_type = formats[1]

        self.delimiter = delimiter
        self.options = options

        self.output = None


    def format(self, input_path, output_path, delimiter=None):
        """
        TODO
        """
        print(self.input_type.name, self.output_type.name)
        input_filename = input_path + '.' + self.input_type.name
        if os.path.isfile(input_filename) == False:
            raise OSError('No such file: %s' % input_filename)
            exit()

        file = open(input_filename, 'r')
        content = self.input_type.load(file, delimiter)
        file.close()
        self.output = self.output_type.parse(content, delimiter)


    def save(self, file_path):
        file = open(file_path, 'w+')
        file.write(self.output)
        file.close()


    def show(self):
        """
        TODO
        """
        # TODO: Think of a good way to transform the internal structure into string
        print(self.output)


    def get(self):
        """
        TODO
        """
        # TODO: Extend this function in a usefull way
        return self.output


def konbata(input_filename, output_filename, m_save=False, m_show=False,
            m_get=False, delimiter=None, options=None):
    """
    Convertes one file into another

    input_filename: File Input
    output_filename: File Output

    TODO: Add more complex/better description
    """

    (input_path, input_type) = os.path.splitext(input_filename)
    (output_path, output_type) = os.path.splitext(output_filename)

    c = Konbata(input_type, output_type, options)
    c.format(input_path, output_path, delimiter)

    c.save(output_path + output_type)

    if m_show:
        c.show()
    if m_get:
        return c.get()


if __name__ == '__main__':
    """
    TODO
    """
    parser = argparse.ArgumentParser()
    # In/Output
    parser.add_argument("input_file", type=str, help="Path of input file")
    parser.add_argument("output_file", type=str, help="Path of output file")

    # Mode
    parser.add_argument("-sa", "--save", action="store_true",
                        help="Store output file")
    parser.add_argument("-sh", "--show", action="store_true",
                        help="Show output file")
    parser.add_argument("-g", "--get", action="store_true",
                        help="Get output file")
    # Options
    parser.add_argument("-del", "--delimiter", type=str,
                        help="Set delimiter ';'")
    parser.add_argument("-opt", "--options", type=str,
                        help="Path of option file")

    args = parser.parse_args()
    print(args)
    konbata(args.input_file, args.output_file,
            m_save=args.save, m_show=args.show, m_get=args.get,
            delimiter=args.delimiter, options=args.options)
