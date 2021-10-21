# +-------------------------[ Dice Simulator ]-----------------------+
# |                                                                  |
# |        This is a simple Python program to Simulate Dice.         |
# +------------------------------------------------------------------+
# |                    Author : Prashant Bhandari                    |
# |                   ============================                   |
# +------------------------------------------------------------------+

import os
import random
import platform
from color import prRed, prGreen, prYellow, prBlue

dice = [1, 2, 3, 4, 5, 6]

banner = """
  _____  _             _____ _                 _       _             
 |  __ \(_)           / ____(_)               | |     | |            
 | |  | |_  ___ ___  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 | |  | | |/ __/ _ \  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 | |__| | | (_|  __/  ____) | | | | | | | |_| | | (_| | || (_) | |   
 |_____/|_|\___\___| |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                 - Prashant Bhandari
"""

mainmenu = """
                        ╔════════════════════╗
                        ║        MENU        ║
                        ╠════════════════════╣
                        ║     [1] Start      ║
                        ║     [2] Exit       ║
                        ╚════════════════════╝
"""

one = """
                            ╔═══════════╗
                            ║           ║
                            ║           ║
                            ║     o     ║
                            ║           ║
                            ║           ║
                            ╚═══════════╝
"""

two = """
                            ╔═══════════╗
                            ║           ║
                            ║  o        ║
                            ║           ║
                            ║        o  ║
                            ║           ║
                            ╚═══════════╝
"""

three = """
                            ╔═══════════╗
                            ║ o         ║
                            ║           ║
                            ║     o     ║
                            ║           ║
                            ║         o ║
                            ╚═══════════╝
"""

four = """
                            ╔═══════════╗
                            ║ o       o ║
                            ║           ║
                            ║           ║
                            ║           ║
                            ║ o       o ║
                            ╚═══════════╝
"""

five = """
                            ╔═══════════╗
                            ║ o       o ║
                            ║           ║
                            ║     o     ║
                            ║           ║
                            ║ o       o ║
                            ╚═══════════╝
"""

six = """
                            ╔═══════════╗
                            ║ o       o ║
                            ║           ║
                            ║ o       o ║
                            ║           ║
                            ║ o       o ║
                            ╚═══════════╝
"""


def clrscr():
    ops = platform.system()
    if ops == "Windows":
        os.system("cls")
    elif ops == "Linux":
        os.system("clear")
    elif ops == "Darwin":
        os.system("clear")
    else:
        prBlue("[ Operating System not supported ]".center(69, "-"))



def roll():
    value = True
    while (value):
        clrscr()
        side = random.choice(dice)
        if side == 1:
            prGreen(one)
            prYellow("[ One ]".center(69, " "))
        elif side == 2:
            prGreen(two)
            prYellow("[ Two ]".center(69, " "))
        elif side == 3:
            prGreen(three)
            prYellow("[ Three ]".center(69, " "))
        elif side == 4:
            prGreen(four)
            prYellow("[ Four ]".center(69, " "))
        elif side == 5:
            prGreen(five)
            prYellow("[ Five ]".center(69, " "))
        else:
            prGreen(six)
            prYellow("[ Six ]".center(69, " "))
        prRed("".center(69, "="))
        prRed("[+] Press Enter to roll the dice")
        prRed("[+] Press 0 and Enter to exit")
        c = input()
        if c == "0":
            exit()
        else:
            roll()


def main():
    clrscr()
    prGreen(banner)
    value = True
    while (value):
        prRed(mainmenu)
        prRed("[+] Enter your Choice:")
        c = input()
        if c == "1":
            roll()
        if c == "2":
            exit()
        else:
            prBlue("[ Invalid Choice ]".center(69, "-"))
        input()


if __name__ == "__main__":
    main()
