"""
    FormatLoader functions, that serve as interface to check and get formats.
"""

from .csv_format import csv_format
from .txt_format import txt_format
from .xlsx_format import xlsx_format

TYPES = {'.csv': csv_format,
         '.txt': txt_format,
         '.xlsx': xlsx_format}


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

    return [TYPES[type_name] for type_name in type_names]
