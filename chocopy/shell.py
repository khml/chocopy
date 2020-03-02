# -*- coding:utf-8 -*-

import readline
import pprint

from chocopy.completer import Completer
from chocopy.util import make_func_table, find_func

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')


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

    readline.set_completer(None)
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


class InteractiveShell:
    def __init__(self, functions, completer=None):
        self._table = {}
        self._commands = []
        self._return_value = None
        self._make_table(functions)

        self._completer = completer or Completer(self._commands).complete
        self._completer = completer or Completer(self._commands).complete
        readline.set_completer(self._completer)

    def _make_table(self, functions):
        if isinstance(functions, list):
            table = make_func_table(functions)
        elif isinstance(functions, dict):
            table = functions
        else:
            raise TypeError
        self._table = table

        self._table['exit'] = exit
        self._table['eval'] = self._eval
        self._commands = list(self._table.keys())
        self._commands.extend(['help', 'result', 'return'])

    def _help(self):
        [print(name) for name in self._commands]

    def _print_return_value(self):
        pprint.pprint(self._return_value)

    def _eval(self):
        _return_value = None
        while True:
            command = str(input('eval > '))
            if command == 'return':
                return _return_value
            try:
                _return_value = eval(command)
            except Exception as e:
                print(e)

    def run(self):
        while True:
            command = input('> ').strip()

            if command == 'help':
                self._help()
                continue

            if command == 'result':
                self._print_return_value()
                continue

            func, ok = find_func(command, self._table)

            if not ok:
                print("not found : {}".format(command))
                continue

            try:
                self._return_value = func()
                self._print_return_value()
            except Exception as e:
                print("Failed to exec command : {}".format(command))
                pprint.pprint(e)
