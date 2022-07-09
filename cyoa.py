import sys
import time

def path1():
    print()
    print("This is path number 1")
    print("Pick a color: [1]red, [2]blue, [3]green")
    colorChoice = input("> ")
    if colorChoice == "1":
        print('red is dead!')
        endGame();
    elif colorChoice == "2":
        print('blue is for bling')
    elif colorChoice == "3":
        print("money money")

def path2():
    print()
    print("This is path number 2. It is still under construction")
    print()

def path3():
    print()
    print("This is path number 3, a it is in construction")
    print()

def startGame():
    print('game started')
    print('choose a path')
    print("[1]path1, [2]path2, [3]path3")
    firstPath = input("> ")
    if firstPath == "1":
        path1()
    elif firstPath == "2":
        path2()
    elif firstPath == "3":
        path3()


def endGame():
    print()
    print()
    print('Game Over')

def intro():
    print("")
    print("")
    print("================================================")
    print("")
    print("  -Welcome to a choose your own adventure game- ")
    print("")
    print("================================================")
    print("")
    print("")
    playgame = input("Do you want to start the game?(Y/n) ").lower()
    if playgame == 'n':
        print("Ok, maybe later")
        return
    else:
        startGame()
 
intro()