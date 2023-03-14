import time
from dataclasses import dataclass
import WebScrapeData
import pickle #Thank god this exists
#Ideas:
# make it So they can enter if they want standard, taiko, catch
# see if they can fix the bug so i can ask if they want the relax mode of not (Please akatsuki devs)
#1. Have the user pick two numbers there difference has to be between 1000 DONE
#2. Webscrape data from akatsuki IN PROCESS
#3. Put info scraped into a dictonary and create a class for info storage. DONE BOZO
#4. Put into a csv file(Bruh moment to make it program fast) READY FOR NEED TO FIX #2
#4. Do shit with it/Ask user info to access (Will take alot of time cause theres alot to implement)
#5. Orangize it and make table and graphs with it (Will be poggers)

@dataclass
class UserInfo:
    userURL: str
    globalRank: int #if not present cause they havent played in awhile but still have pp, the value will be -1
    countryRank: int  #if not present cause they havent played in awhile but still have pp, the value will be -1
    totalPerforamcePoints: int
    rankedScore: int
    totalScore: int
    playCount: int
    totalHits: int
    accuracy: float
    maxCombo: int
    totalFirstPlaces: int
    bestScores: list
    mostPlayedScores: list
    firstPlaceScores: list #if more than ten than it will get the most recent 10 first place scores

@dataclass()
class ScoreInfo:
    websiteLink: str
    songArtist: str
    songName: str
    songDiff: str
    playScore: int
    playCombo: int
    playPerformancePoints: float
    playAcc: float
    play300: int
    play100: int
    play50: int
    playMiss: int

@dataclass()
class MostScoreInfo:
    websiteLink: int
    amountPlayed: int
    songArtist: str
    songName: str
    songDiff: int



def startAndEndID():
    print("To start we will need to get an starting ID and ending ID")
    time.sleep(2)
    print("Note the starting and ending ID must have a maxium difference of 1000")
    time.sleep(2)
    print("Another note the the minuim ID is 1000, and the maxium is 112855")
    time.sleep(2)
    startID = int(input("Enter the starting ID: "))
    endID = int(input("Entering the ending ID: "))
    while (endID-startID > 5000000) or (startID > endID) or (startID < 1000) or (endID > 116000):
        print("Not sufficent id inputs, try again!")
        startID = input("Enter the starting ID: ")
        endID = input("Entering the ending ID: ")
    return (int(startID), int(endID))

def populateFile(idTuple):
    playersDict = WebScrapeData.webScraper(idTuple)
    f = open("Data111000_1160000.txt", "wb")
    pickle.dump(playersDict, f)
    f.close()
    fileLoad = open("Data111000_1160000.txt", "rb")
    dictionary = pickle.load(fileLoad)
    return dictionary

def getAllData():
    startNum = 1000
    endingNum = 6000
    allData = {}
    while (endingNum != 46000):
        file = "Data"+str(startNum)+"_"+str(endingNum)+".txt"
        fileLoad = open(file, 'rb')
        dataDict = pickle.load(fileLoad)
        allData.update(dataDict)
        fileLoad.close()
        startNum+=5000
        endingNum+=5000
        return allData
def main():
    print("Welcome to the Akatsuki Web Scraper!")
    time.sleep(2)
    idTuple = startAndEndID()
    dict = populateFile(idTuple)
    #dict = getAllData()
    print(dict)


if __name__ == '__main__':
    main()
