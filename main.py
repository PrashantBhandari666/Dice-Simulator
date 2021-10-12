# +-------------[ Dice Simulator ]-------------+
# |                                            |
# | This is a simple Python script to Simulate |
# |                  Dice.                     |
# +--------------------------------------------+
# |        Author - Prashant Bhandari          |
# +--------------------------------------------+

import random

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


def roll():
    value = True
    while (value):
        side = random.choice(dice)
        if side == 1:
            print(one)
            print("[ One ]".center(69, " "))
        elif side == 2:
            print(two)
            print("[ Two ]".center(69, " "))
        elif side == 3:
            print(three)
            print("[ Three ]".center(69, " "))
        elif side == 4:
            print(four)
            print("[ Four ]".center(69, " "))
        elif side == 5:
            print(five)
            print("[ Five ]".center(69, " "))
        else:
            print(six)
            print("[ Six ]".center(69, " "))
        print("".center(69, "="))
        print("[+] Press Enter to roll the dice")
        print("[+] Press 0 and Enter to exit")
        c = input()
        if c == "0":
            exit()
        else:
            roll()


def main():
    print(banner)
    value = True
    while (value):
        print(mainmenu)
        c = input("[+] Enter your Choice:")
        if c == "1":
            roll()
        if c == "2":
            exit()
        else:
            print("[ Invalid Choice ]".center(69, "-"))
        input()


if __name__ == "__main__":
    main()
