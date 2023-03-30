import time
import matplotlib.pyplot as plt
import numpy
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
            print()
            print(name)
            time.sleep(1)
            print("\tProfile Website Link: " + info.userURL)
            time.sleep(1)
            print("\tTotal Performace Points: " + str(info.totalPerforamcePoints))
            time.sleep(1)
            print("\tRanked Score: " + str(info.rankedScore))
            time.sleep(1)
            print("\tTotal Score: " + str(info.totalScore))
            time.sleep(1)
            print("\tBeatmaps Played: " + str(info.playCount))
            time.sleep(1)
            print("\tTotal Circles Hit: " + str(info.totalHits))
            time.sleep(1)
            print("\tAll Around Accuracy: " + str(info.accuracy)+"%")
            time.sleep(1)
            print("\tMax Combo: " + str(info.maxCombo))
            time.sleep(1)
            print("\tAmount of First Places on Beatmaps: " + str(info.totalFirstPlaces))
            time.sleep(1)
            print("\tTop Plays (in terms of how much Performance Point were awarded): ")
            time.sleep(1)
            x_values = []
            y_values = []
            listOfBestScores = info.bestScores
            for i in range(0, len(listOfBestScores)):
                score = listOfBestScores[i]
                x_values.append("#" + str(10-i))
                y_value = score.playPerformancePoints
                y_values.append(y_value)
                print("\t\t" + score.songArtist + " - " + score.songName + " [" + score.songDiff + "]")
                time.sleep(1)
                print("\t\t\tOsu Beatmap Link: " + score.websiteLink)
                time.sleep(1)
                print("\t\t\tPerformace Points Awarded: " + str(score.playPerformancePoints))
                time.sleep(1)
                print("\t\t\tScore Earned: " + str(score.playScore))
                time.sleep(1)
                print("\t\t\tTop Combo: " + str(score.playCombo))
                time.sleep(1)
                print("\t\t\tPlay Accuracy: " + str(score.playAcc) + "%")
                time.sleep(1)
                print("\t\t\tAmount of 300's: " + str(score.play300))
                time.sleep(1)
                print("\t\t\tAmount of 100's: " + str(score.play100))
                time.sleep(1)
                print("\t\t\tAmount of 50's: " + str(score.play50))
                time.sleep(1)
                print("\t\t\tMiss Count: " + str(score.playMiss))
                time.sleep(1)
            time.sleep(1)
            y_values.reverse()
            plt.title("Top Plays")
            typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
            if typeOfGraph == "Bar":
                plt.xlabel("Performance Points")
                plt.ylabel("Top Play Number")
                plt.barh(x_values, y_values, color="aquamarine")
                plt.show()
            else:
                plt.xlabel("Top Play Number")
                plt.ylabel("Performance Points")
                plt.plot(x_values, y_values, color="red")
                plt.show()
            print("\tMost Played Beatmaps: ")
            time.sleep(1)
            listOfMostPlayed = info.mostPlayedScores
            for i in range(0, len(listOfMostPlayed)):
                score = listOfMostPlayed[i]
                print("\t\t" + score.songArtist + " - " + score.songName + " [" + score.songDiff + "]")
                time.sleep(1)
                print("\t\t\tOsu Beatmap Link: " + score.websiteLink)
                time.sleep(1)
                print("\t\t\tAmount Played: " + str(score.amountPlayed))
                time.sleep(1)
            time.sleep(1)
            print("\tFirst Place Maps")
            time.sleep(1)
            listOfFirstPlace = []
            listOfFirstPlace = info.firstPlaceScores
            if len(listOfFirstPlace) == 0:
                print("\tThis user has not first places")
            else:
                for i in range(0 , len(listOfFirstPlace)):
                    score = listOfFirstPlace[i]
                    print("\t\t" + score.songArtist + " - " + score.songName + " [" + score.songDiff + "]")
                    time.sleep(1)
                    print("\t\t\tOsu Beatmap Link: " + score.websiteLink)
                    time.sleep(1)
                    print("\t\t\tPerformace Points Awarded: " + str(score.playPerformancePoints))
                    time.sleep(1)
                    print("\t\t\tScore Earned: " + str(score.playScore))
                    time.sleep(1)
                    print("\t\t\tTop Combo: " + str(score.playCombo))
                    time.sleep(1)
                    print("\t\t\tPlay Accuracy: " + str(score.playAcc) + "%")
                    time.sleep(1)
                    print("\t\t\tAmount of 300's: " + str(score.play300))
                    time.sleep(1)
                    print("\t\t\tAmount of 100's: " + str(score.play100))
                    time.sleep(1)
                    print("\t\t\tAmount of 50's: " + str(score.play50))
                    time.sleep(1)
                    print("\t\t\tMiss Count: " + str(score.playMiss))
                    time.sleep(1)
        except:
            print("That name does not exist or that user has no data")
            time.sleep(2)
        finally:
            keepLookingUp = input("Would you like to keep looking up usernames, Yes or No? ")
def actionB(dict):
    print("This action will print out a top 50 list of the user that have the highest ranked score")
    time.sleep(4)
    dict_sorted = sorted(dict.items(), key=lambda x: x[1].rankedScore, reverse=True)
    x_values = []
    y_values = []
    for i in range(0, 50):
        time.sleep(1)
        print(str(50-i) + ".")
        if (50-i <= 10):
            x_value = str(dict_sorted[50-i-1][0])
            y_value = float(dict_sorted[50-i-1][1].rankedScore / 1000000000)
            x_values.append(x_value)
            y_values.append(y_value)
        print("\t" + dict_sorted[50-i-1][0])
        print("\tRanked Score: " + str(dict_sorted[50-i-1][1].rankedScore))
    typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
    if typeOfGraph == "Bar":
        plt.rc('ytick', labelsize=6)
        plt.xlabel("Ranked Score (In Billions)")
        plt.ylabel("User")
        plt.title("Top 10 Users by Ranked Score")
        plt.barh(x_values,y_values, color="aquamarine")
        plt.show()
    else:
        plt.rc('xtick', labelsize=6)
        plt.xlabel("User")
        plt.ylabel("Ranked Score (In Billions)")
        plt.title("Top 10 Users by Ranked Score")
        plt.plot(x_values, y_values, color="red")
        plt.show()
def actionC(dict):
    # Make a graph with top 10
    print("This action will print out a top 50 list of the user that have the highest total score")
    time.sleep(4)
    dict_sorted = sorted(dict.items(), key=lambda x: x[1].totalScore, reverse=True)
    x_values = []
    y_values = []
    for i in range(0, 50):
        time.sleep(1)
        print(str(50 - i) + ".")
        if (50 - i <= 10):
            x_value = str(dict_sorted[50 - i - 1][0])
            y_value = float(dict_sorted[50 - i - 1][1].totalScore / 1000000000)
            x_values.append(x_value)
            y_values.append(y_value)
        print("\t" + dict_sorted[50 - i - 1][0])
        print("\tTotal Score: " + str(dict_sorted[50 - i - 1][1].totalScore))
    typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
    if typeOfGraph == "Bar":
        plt.rc('ytick', labelsize=6)
        plt.xlabel("Total Score Score (In Billions)")
        plt.ylabel("User")
        plt.title("Top 10 Users by Total Score")
        plt.barh(x_values, y_values, color="aquamarine")
        plt.show()
    else:
        plt.rc('xtick', labelsize=6)
        plt.xlabel("User")
        plt.ylabel("Total Score (In Billions)")
        plt.title("Top 10 Users by Total Score")
        plt.plot(x_values, y_values, color="red")
        plt.show()
def actionD(dict):
    # Make a graph with top 10
    print("This action will print out a top 50 list of the user that have the highest play count")
    time.sleep(4)
    dict_sorted = sorted(dict.items(), key=lambda x: x[1].playCount, reverse=True)
    x_values = []
    y_values = []
    for i in range(0, 50):
        time.sleep(1)
        print(str(50 - i) + ".")
        if (50 - i <= 10):
            x_value = str(dict_sorted[50 - i - 1][0])
            y_value = float(dict_sorted[50 - i - 1][1].playCount)
            x_values.append(x_value)
            y_values.append(y_value)
        print("\t" + dict_sorted[50 - i - 1][0])
        print("\tPlay Count: " + str(dict_sorted[50 - i - 1][1].playCount))
    typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
    if typeOfGraph == "Bar":
        plt.rc('ytick', labelsize=6)
        plt.xlabel("Play Count")
        plt.ylabel("User")
        plt.title("Top 10 Users by Play Count")
        plt.barh(x_values, y_values, color="aquamarine")
        plt.show()
    else:
        print("Note: Two usernames do overlap, those being verbo irregular and BLEACH FAN")
        plt.rc('xtick', labelsize=6)
        plt.xlabel("User")
        plt.ylabel("Play Count")
        plt.title("Top 10 Users by Play Count")
        plt.plot(x_values, y_values, color="red")
        plt.show()
def actionE(dict):
    # Make a graph with top 10
    print("This action will print out a top 50 list of the user that have the highest amount of Performance Points")
    time.sleep(4)
    dict_sorted = sorted(dict.items(), key=lambda x: x[1].totalPerforamcePoints, reverse=True)
    x_values = []
    y_values = []
    for i in range(0, 50):
        time.sleep(1)
        print(str(50 - i) + ".")
        if (50 - i <= 10):
            x_value = str(dict_sorted[50 - i - 1][0])
            y_value = float(dict_sorted[50 - i - 1][1].totalPerforamcePoints)
            x_values.append(x_value)
            y_values.append(y_value)
        print("\t" + dict_sorted[50 - i - 1][0])
        print("\tPerformance Points: " + str(dict_sorted[50 - i - 1][1].totalPerforamcePoints))
    typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
    if typeOfGraph == "Bar":
        plt.rc('ytick', labelsize=6)
        plt.xlabel("Performance Points")
        plt.ylabel("User")
        plt.title("Top 10 Users by Performance Points")
        plt.barh(x_values, y_values, color="aquamarine")
        plt.show()
    else:
        plt.rc('xtick', labelsize=6)
        plt.xlabel("User")
        plt.ylabel("Performance Points")
        plt.title("Top 10 Users by Performance Points")
        plt.plot(x_values, y_values, color="red")
        plt.show()
def actionF(dict):
    # Make a graph with top 10
    print("This action will print out a top 50 list of the user that have the highest amount of first places on beatmaps")
    time.sleep(4)
    dict_sorted = sorted(dict.items(), key=lambda x: x[1].totalFirstPlaces, reverse=True)
    x_values = []
    y_values = []
    for i in range(0, 50):
        time.sleep(1)
        print(str(50 - i) + ".")
        if (50 - i <= 10):
            x_value = str(dict_sorted[50 - i - 1][0])
            y_value = float(dict_sorted[50 - i - 1][1].totalFirstPlaces)
            x_values.append(x_value)
            y_values.append(y_value)
        print("\t" + dict_sorted[50 - i - 1][0])
        print("\tAmount of First Places: " + str(dict_sorted[50 - i - 1][1].totalFirstPlaces))
    typeOfGraph = input("What type of graph would you like to see, Bar or Line: ")
    if typeOfGraph == "Bar":
        plt.rc('ytick', labelsize=6)
        plt.xlabel("Amount of First Places")
        plt.ylabel("User")
        plt.title("Top 10 Users by Total First Places")
        plt.barh(x_values, y_values, color="aquamarine")
        plt.show()
    else:
        plt.rc('xtick', labelsize=6)
        plt.xlabel("User")
        plt.ylabel("Amount of First Places")
        plt.title("Top 10 Users by Total First Places")
        plt.plot(x_values, y_values, color="red")
        plt.show()
def actionG(dict):
    print()
def actionH(dict):
    print()
def actionI(dict):
    print()
def actionJ(dict):
    print()