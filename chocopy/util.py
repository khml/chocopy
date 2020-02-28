# -*- coding:utf-8 -*-

from collections import OrderedDict


def arg_names(func: callable):
    return func.__code__.co_varnames[:func.__code__.co_argcount]


def make_func_table(functions: list) -> dict:
    """
    :param functions: List[callable]
    :return:
    """
    table = OrderedDict()
    for func in functions:
        table[func.__name__] = func
    return table


def find_func(func_name: str, func_table: dict) -> list:
    func = func_table.get(func_name, None)

    if func is None:
        return [None, False]

    return [func, True]
