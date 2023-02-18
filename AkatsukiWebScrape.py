import time
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
#1. Have the user pick two numbers there difference has to be between 10000 DONE
#2. Webscrape data from akatsuki
#3. Put info scraped into a dictonary and create a class for info storage
#4. Do shit with it
#5. Orangize it and make table and graphs with it
#6. Make it so people can do multiple times
#7. At the end ask user if they want all data of all user and
#let them know it will take awhile but will be worth it
@dataclass
class UserInfo:
    globalRank: int
    countryRank: int
    totalPerforamcePoints: int
    rankedScore: int
    totalScore: int
    playCount: int
    totalHits: int
    accuracy: float
    maxCombo: int
    scores: list

@dataclass()
class ScoreInfo:
    websiteLink: str
    songArtist: str
    songName: str
    songDiff: str
    playScore: int
    playCombo: int
    playMods: str
    playPerformancePoints: int
    playAcc: float

def startAndEndID():
    print("To start we will need to get an starting ID and ending ID")
    time.sleep(2)
    print("Note the starting and ending ID must have a maxium difference of 1000")
    time.sleep(2)
    print("Another note the the minuim ID is 1000, and the maxium is 110000")
    time.sleep(2)
    startID = int(input("Enter the starting ID: "))
    endID = int(input("Entering the ending ID: "))
    while (endID-startID > 1000) or (startID > endID) or (startID < 1000) or (endID > 110000):
        print("Not sufficent id inputs, try again!")
        startID = input("Enter the starting ID: ")
        endID = input("Entering the ending ID: ")
    return (int(startID), int(endID))

def webScraper(startEndTuple):
    playerDictionary = {}
    #for id in range(1001, 1002):
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.pw/u/" + str(id) + "?mode=0&rx=1"
        page = requests.get(url, allow_redirects=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        nameElements = soup.find("h1", style="white-space: nowrap !important;")
        if nameElements is None:
            pass
        else:
            nameElements = soup.find("h1", style="white-space: nowrap !important;").text.strip().split()
            userTable = soup.find("table", class_="ui very basic two column compact table nopad").text.strip().split()
            if userTable[0] == "Clan" and userTable[1] != "PP":
                username = ""
                for x in range(1, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(username)
                print(userTable)
            elif userTable[0] == "Clan" and userTable[1] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(username)
                print(userTable)
            elif userTable[6] == "Clan" and userTable[7] != "PP":
                username = ""
                for x in range(1, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(username)
                print(userTable)
            elif userTable[6] == "Clan" and userTable[7] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(username)
                print(userTable)
            else:
                pass

def main():
    print("Welcome to the Akatsuki Web Scraper!")
    time.sleep(3)
    idTuple = startAndEndID()
    playersDict = webScraper(idTuple)

main()
