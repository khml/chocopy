# -*- coding:utf-8 -*-

import chocopy


def func1():
    return True


def func2():
    return "1"


def func3():
    return "Hello"


def func4():
    return "World"


def func5():
    return "What"


def main():
    chocopy.InteractiveShell([func1, func2, func3, func4, func5]).run()


if __name__ == '__main__':
    main()
