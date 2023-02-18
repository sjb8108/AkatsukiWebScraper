import time
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import WebScrapeData
#Ideas:
# make it So they can enter if they want standard, taiko, catch
#1. Have the user pick two numbers there difference has to be between 1000 DONE
#2. Webscrape data from akatsuki
#3. Put info scraped into a dictonary and create a class for info storage
#4. Do shit with it/Ask user info to access
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

def main():
    print("Welcome to the Akatsuki Web Scraper!")
    time.sleep(3)
    idTuple = startAndEndID()
    playersDict = WebScrapeData.webScraper(idTuple)

if __name__ == '__main__':
    main()
