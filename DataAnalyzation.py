import time

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
        action = input("Enter an action letter: ")
        checkAction(action)
        while (checkAction(action) == False):
            print("Incorrect Input, try again")
            action = input("Enter an action letter: ")
            checkAction(action)
        print("Cool")

def checkAction(action):
    if (len(action) > 1):
        return False
    else:
        action = action.upper()
        if (ord(action) >= 65 and ord(action) <= 74):
            return True
        return False