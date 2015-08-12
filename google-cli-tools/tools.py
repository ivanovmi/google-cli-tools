#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

from pprint import PrettyPrinter


class MyPrettyPrinter(PrettyPrinter):
    """
    That class print results in CLI with russian charset
    """
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return object.encode('utf8'), True, False
        return PrettyPrinter.format(self, object, context, maxlevels, level)


def swap_key_values(my_dict):
    """
    That function swap key and value in one dictionary
    :param my_dict: dictionary
    :return: new dictionary, where values = keys, and keys = values
    """
    return dict(zip(my_dict.values(), my_dict.keys()))
