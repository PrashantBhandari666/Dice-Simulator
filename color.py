# +----------------------------------------------------------------------+
# | This module contains some function to print text in different color. |
# +----------------------------------------------------------------------+
#                      Author : Prashant Bhandari

def prBlack(text):
    print('\033[30m', text, '\033[0m', sep='')


def prRed(text):
    print('\033[31m', text, '\033[0m', sep='')


def prGreen(text):
    print('\033[32m', text, '\033[0m', sep='')


def prYellow(text):
    print('\033[33m', text, '\033[0m', sep='')


def prBlue(text):
    print('\033[34m', text, '\033[0m', sep='')


def prMagenta(text):
    print('\033[35m', text, '\033[0m', sep='')


def prCyan(text):
    print('\033[36m', text, '\033[0m', sep='')


def prGray(text):
    print('\033[90m', text, '\033[0m', sep='')


if __name__ == '__main__':
    # Examples of color
    prBlack("Hello World")
    prRed("Hello World")
    prGreen("Hello World")
    prYellow("Hello World")
    prBlue("Hello World")
    prMagenta("Hello World")
    prCyan("Hello World")
    prGray("Hello World")
