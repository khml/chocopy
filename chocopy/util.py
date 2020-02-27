# -*- coding:utf-8 -*-

import readline
import pprint
from collections import OrderedDict

from chocopy.completer import Completer


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


def interactive(functions):
    """
    :param functions: list or dict
    :return:
    """
    if isinstance(functions, list):
        table = make_func_table(functions)
    elif isinstance(functions, dict):
        table = functions
    else:
        raise TypeError

    table['exit'] = exit

    func_names = list(table.keys())
    func_names.extend(['exit', 'help'])

    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')
    readline.set_completer(Completer(func_names).complete)

    while True:
        command = input("> ").strip()

        if command == 'help':
            [print(name) for name in func_names]
            continue

        func, ok = find_func(command, table)

        if not ok:
            print("not found : {}".format(command))
            continue

        try:
            pprint.pprint(func())
        except Exception as e:
            print("Failed to exec command : {}".format(command))
            pprint.pprint(e)
