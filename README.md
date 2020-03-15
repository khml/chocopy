# chocopy

chocopy is a toy REPL tool.

## Dependencies
- Python3.7 and more

## Usage

write a tinny script

```python
# python example.py

import chocopy

def func1():
    return True


def func2():
    return 1


def func3():
    return "Hello"

def main():
    chocopy.InteractiveShell([func1, func2, func3]).run()


if __name__ == '__main__':
    main()

```

run this script

```
$ python example.py
>>> help
func1
func2
func3
exit
help
result
>>> func1
True
>>> result
True
>>> func2
1
>>> result
1
>>> exit

```