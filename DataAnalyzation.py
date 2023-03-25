import time
import matplotlib
def choosingActions(dict):
    print("NOTE: A more detailed description of what data you will be seeing with be shown when picking an action")
    time.sleep(4)
    keepGoing = "Yes"
    while (keepGoing == "Yes"):
        print("Action A: Name Lookup")
        print("Action B: Most Ranked Score")
        print("Action C: Most Total Score")
        print("Action D: Most Play Count")
        print("Action E: Most Performance Points")
        print("Action F: Most First Places")
        print("Action G: Song Lookup in Top Plays")
        print("Action H: Most Played Map")
        print("Action I: Most Total Beatmap Plays")
        print("Action J: Most Beatmaps in Top Plays")
        action = input("Enter an action letter: ").upper()
        checkAction(action)
        while (checkAction(action) == False):
            print("Incorrect Input, try again")
            action = input("Enter an action letter: ").upper()
            checkAction(action)
        if action == "A":
            actionA(dict)
        if action == "B":
            actionB(dict)
        if action == "C":
            actionC(dict)
        if action == "D":
            actionD(dict)
        if action == "E":
            actionE(dict)
        if action == "F":
            actionF(dict)
        if action == "G":
            actionG(dict)
        if action == "H":
            actionH(dict)
        if action == "I":
            actionI(dict)
        if action == "J":
            actionJ(dict)
        keepGoing = input("Would you like to continue, Yes or No? ")


def checkAction(action):
    if (len(action) > 1):
        return False
    else:
        action = action.upper()
        if (ord(action) >= 65 and ord(action) <= 74):
            return True
        return False

def actionA(dict):
    print("Type the name the of a user and you will either get infomation about them or a message saying that the user doesnt exist")
    time.sleep(5)
    keepLookingUp = "Yes"
    while (keepLookingUp == "Yes"):
        try:
            name = input("Enter the username you would like to look up: ")
            info = dict[name]
        except:
            print("That name does not exist or that user has no data")
            time.sleep(2)
            keepLookingUp = input("Would you like to keep looking up usernames, Yes or No? ")
def actionB(dict):
    print()
def actionC(dict):
    print()
def actionD(dict):
    print()
def actionE(dict):
    print()
def actionF(dict):
    print()
def actionG(dict):
    print()
def actionH(dict):
    print()
def actionI(dict):
    print()
def actionJ(dict):
    print()