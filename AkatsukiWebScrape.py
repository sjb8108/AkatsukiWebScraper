import time
from dataclasses import dataclass
import WebScrapeData
import DataAnalyzation
import pickle
#Ideas:
#me when new ideas needed
#1. Refactor WebScrapeData.py (Done)
#2. Set rate limit tests on web scraping from akatsuki api
#3. Akatsuki vs Osu leaderboard
@dataclass
class UserInfo:
    userURL: str
    userName: str
    userID: int
    clanName: str
    clanTag: str
    followers: int
    country: str
    registerDate: str
    lastDateOnline: str
    profileImageLink: str
    gamemodes: dict
@dataclass()
class GamemodeInfo:
    globalRank: int
    countryRank: int
    totalPerforamcePoints: int
    rankedScore: int
    totalScore: int
    playCount: int
    totalHits: int
    accuracy: float
    maxCombo: int
    replaysWatched: int
    level: float
    bestScores: list
    mostPlayedScores: list
    totalFirstPlaces: int
    firstPlaceScores: list
    mostRecentScores: list
    pinnedScores: list
@dataclass()
class ScoreInfo:
    websiteLink: str
    songArtist: str
    songName: str
    songDiff: str
    rankStatus: str
    approachRate: float
    od: float
    playScore: int
    playCombo: int
    playPerformancePoints: float
    playAcc: float
    play300: int
    play100: int
    play50: int
    playMiss: int
    mods: str
    rank: str
    datePlayed: str
    completed: bool
@dataclass()
class MostScoreInfo:
    websiteLink: str
    songArtist: str
    songName: str
    songDiff: str
    rankedStatus: int
    amountPlayed: int
def startAndEndID():
    print("To start we will need to get an starting ID and ending ID")
    time.sleep(2)
    print("Note the starting and ending ID must have a maximum difference of 1000")
    time.sleep(2)
    print("Another note the the minim ID is 1000, and the maximum is 112855")
    time.sleep(2)
    startID = int(input("Enter the starting ID: "))
    endID = int(input("Entering the ending ID: "))
    while (startID < 0) or (startID > endID) or (startID < 1000) or (endID > 128000):
        print("Not sufficent id inputs, try again!")
        startID = input("Enter the starting ID: ")
        endID = input("Entering the ending ID: ")
    return (int(startID), int(endID))
def populateFile(idTuple):
    playersDict = WebScrapeData.webScraper(idTuple)
    f = open("Data/Data111000_116000.txt", "wb")
    pickle.dump(playersDict, f)
    f.close()
    fileLoad = open("Data/Data111000_116000.txt", "rb")
    dictionary = pickle.load(fileLoad)
    return dictionary
def getAllData():
    startNum = 1000
    endingNum = 6000
    allData = {}
    counter = 0
    while (counter <= 22):
        file = "Data\Data"+str(startNum)+"_"+str(endingNum)+".txt"
        fileLoad = open(file, 'rb')
        dataDict = pickle.load(fileLoad)
        allData.update(dataDict)
        fileLoad.close()
        startNum+=5000
        endingNum+=5000
        counter+=1
    return allData
def fixBuggedUsernames(dict):
    for person in dict:
        persons = str(person)
        ascii = (ord(persons[0:1]))
        if (ascii > 127):
            dict = WebScrapeData.fixUsername(persons, dict)
        elif (ascii == 32 or ascii == 33 or ascii == 45 or ascii == 91 or ascii == 93 or ascii == 95):
            pass
        elif ((ascii >= 48 and ascii <= 57) or (ascii >= 65 and ascii <= 90) or (
                ascii >= 97 and ascii <= 122)):
            pass
        else:
            dict = WebScrapeData.fixUsername(persons, dict)
    return dict
def main():
    print("Welcome to the Akatsuki Web Scraper!")
    time.sleep(2)
    idTuple = startAndEndID()
    dict = WebScrapeData.webScraper(idTuple)
    print("All data collected is from a private osu server I play on.")
    time.sleep(3)
    print("This data was collected in early march so the data collected is different to the data on the website")
    time.sleep(5)
    print("Once the data is loaded in you will be presented with a list of actions that you can do.")
    time.sleep(4)
    print("Choose the letter associated with action.")
    time.sleep(2)
    print("At the end of each action you can choose to do a different action or stop the program.")
    time.sleep(3)
    print("Enough of me rambling lets go collect and analyze some data!")
    time.sleep(2)
    print("Getting and Loading data...")
    dict = getAllData()
    dict = fixBuggedUsernames(dict)
    print("All data collected!")
    time.sleep(2)
    DataAnalyzation.choosingActions(dict)

if __name__ == '__main__':
    main()
