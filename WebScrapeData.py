from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape

def webScraper(startEndTuple):
    playerDictionary = {}
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
            if checkForUserExceptions(url) == True:
                pass
            elif userTable[0] == "Clan" and userTable[1] != "PP":
                username = ""
                for x in range(1, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex+1])
                if (pp > 0):
                    print(username)
                    print(userTable)
                    print(pp)
            elif userTable[0] == "Clan" and userTable[1] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    print(username)
                    print(userTable)
                    print(pp)
            elif userTable[6] == "Clan" and userTable[7] != "PP":
                username = ""
                for x in range(1, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    print(username)
                    print(userTable)
                    print(pp)
            elif userTable[6] == "Clan" and userTable[7] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    print(username)
                    print(userTable)
                    print(pp)
            else:
                pass

def convertThousandsStringToInt(thousandNumber):
    stringWithoutCommas = ""
    for character in thousandNumber:
        if character == ",":
            pass
        else:
            stringWithoutCommas+=character
    return int(stringWithoutCommas)

def findPPIndex(infoData):
    index = 0
    for info in infoData:
        if info == "PP":
            return index
        else:
            index+=1

def checkForUserExceptions(url):
    if url == "https://akatsuki.pw/u/50615?mode=0&rx=1":
        return True