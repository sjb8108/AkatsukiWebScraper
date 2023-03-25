import time
from dataclasses import dataclass
import WebScrapeData
import DataAnalyzation
import pickle #Thank god this exists
#Ideas:
# make it So they can enter if they want standard, taiko, catch
# see if they can fix the bug so i can ask if they want the relax mode of not (Please akatsuki devs)
#fix bug with song diffs having unquie character for example user 70993
#1. Have the user pick two numbers there difference has to be between 1000 DONE
#2. Webscrape data from akatsuki IN PROCESS
#3. Put info scraped into a dictonary and create a class for info storage. DONE BOZO
#4. Put into a csv file(Bruh moment to make it program fast) IN PROCESS
#4. Do shit with it/Ask user info to access (Will take alot of time cause theres alot to implement)
#5. Orangize it and make table and graphs with it (Will be poggers)

@dataclass
class UserInfo:
    userURL: str
    globalRank: int #if not present cause they havent played in awhile but still have pp, the value will be None
    countryRank: int  #if not present cause they havent played in awhile but still have pp, the value will be None
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
    #idTuple = startAndEndID() used to get data but not needed in final project
    #dict = populateFile(idTuple) used to get data but not needed in final project
    print("All data collected is from a private osu server I play on.")
    time.sleep(3)
    print("Once the data is loaded in you will be presented with a list of actions that you can do.")
    time.sleep(4)
    print("Choose the letter associated with action.")
    time.sleep(2)
    print("At the end of each action you can choose to do a different action or stop the program.")
    time.sleep(3)
    print("Enough of me rambling lets go collect and analzye some data!")
    time.sleep(2)
    print("Getting and Loading data...")
    dict = getAllData()
    dict = fixBuggedUsernames(dict)
    print("All data collected!")
    time.sleep(2)
    DataAnalyzation.choosingActions(dict)



if __name__ == '__main__':
    main()
