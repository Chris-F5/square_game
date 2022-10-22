import random, os, sys

DARK = u'\u2591'*2
LIGHT = u'\u2588'*2
LIGHT_HIGHLIGHT = u'[]'
DARK_HIGHLIGHT = u'[]'

def clear():
    os.system("clear")
def print_board(highlight = (0,0)):
    print()
    for y in range(8):
        rank = 8 - y
        print(" " + str(rank), end = "")
        for x in range(8):
            file = x + 1
            if (file + rank) % 2 == 1:
                if file == highlight[0] and rank == highlight[1]:
                    print(LIGHT_HIGHLIGHT, end = "")
                else:
                    print(LIGHT, end = "")
            else:
                if file == highlight[0] and rank == highlight[1]:
                    print(DARK_HIGHLIGHT, end = "")
                else:
                    print(DARK, end = "")
        print()
    print("  A B C D E F G H ")

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

clear()

try:
    while True:
        rank = random.randint(1,8)
        file = random.randint(1,8)
        square = letters[file - 1] + str(rank)
        print(square)
        ans = "l"
        if (rank + file) % 2 == 0:
            ans = "d"
        guess = input()
        if guess == ans:
            print("Correct ^_^")
        else:
            print("Incorrect !!!")
            print_board((file, rank))
            input("Press any key to continue...")
            clear()
except KeyboardInterrupt:
    print()
