from csv_format import csv_loader, csv_parser
from txt_format import txt_loader, txt_parser

csv = Format('csv', [';', ','],
             loader= csv_loader, parser=csv_parser)

txt = Format('txt', [';', ','],
             loader=txt_loader, parser=txt_parser)

TYPES = {'.csv': csv, '.txt': txt}

class Format:
    def __init__(self, name, delimiters=[], loader=None, parser=None):
        self.name = name
        self.delimiters = delimiters
        self.loader = loader
        self.parser = parser


    def load(self, file, delimiter=None):
        if delimiter != None:
            return self.loader(file, delimiter)

        return self.loader(file, self.delimiters[0])


    def parse(self, content, delimiter=None):
        if delimiter != None:
            return self.parser(content, delimiter)

        return self.parser(content, self.delimiters[0])


def checkTypes(type_names=[]):
    for type_name in type_names:
        if type_name not in TYPES:
            raise TypeError('Type %s not supported:' % type_name)
            exit()


def getFormats(type_names=[]):

    checkTypes(type_names)

    return [TYPES[type_name] for type_name in type_names]
