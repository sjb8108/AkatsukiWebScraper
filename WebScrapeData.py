from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
def webScraper(startEndTuple):
    playerDictionary = {}
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.pw/u/" + str(id) + "?mode=0&rx=0"
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
                print(url)
                if nameElements[0] == "[[":
                    username = nameElements[2]
                print(username)
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex+1])
                ppIndex += 1
                theUser = AkatsukiWebScrape.UserInfo(url,0,0, pp, convertThousandsStringToInt(userTable[ppIndex+3]),
                            convertThousandsStringToInt(userTable[ppIndex+6]),convertThousandsStringToInt(userTable[ppIndex+8]),
                            convertThousandsStringToInt(userTable[ppIndex+18]),convertAccuracyToFloat(userTable[ppIndex+20]),
                            convertThousandsStringToInt(userTable[ppIndex+23]), getTopFiveScores(), getMostPlayed())
                print(theUser)
            elif userTable[0] == "Clan" and userTable[1] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(url)
                if nameElements[0] == "[[":
                    username = nameElements[2]
                print(username)
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    theUser = AkatsukiWebScrape.UserInfo(url, 0, 0, pp,convertThousandsStringToInt(userTable[5]),
                                        convertThousandsStringToInt(userTable[8]),convertThousandsStringToInt(userTable[10]),
                                        convertThousandsStringToInt(userTable[20]),convertAccuracyToFloat(userTable[22]),
                                        convertThousandsStringToInt(userTable[25]),getTopFiveScores(), getMostPlayed())
                    print(theUser)
            elif userTable[6] == "Clan" and userTable[7] != "PP":
                username = ""
                for x in range(1, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(url)
                if nameElements[0] == "[[":
                    username = nameElements[2]
                print(username)
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                ppIndex+=1
                if (pp > 0):
                    theUser = AkatsukiWebScrape.UserInfo(url, convertRankingToInt(userTable[2]), convertRankingToInt(userTable[5]), pp,
                                    convertThousandsStringToInt(userTable[ppIndex+3]),convertThousandsStringToInt(userTable[ppIndex+6]),
                                    convertThousandsStringToInt(userTable[ppIndex+8]),convertThousandsStringToInt(userTable[ppIndex + 18]),
                                    convertAccuracyToFloat(userTable[ppIndex+20]),convertThousandsStringToInt(userTable[ppIndex+23]),
                                    getTopFiveScores(), getMostPlayed())
                    print(theUser)
            elif userTable[6] == "Clan" and userTable[7] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                print(url)
                if nameElements[0] == "[[":
                    username = nameElements[2]
                print(username)
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    theUser = AkatsukiWebScrape.UserInfo(url, convertRankingToInt(userTable[2]), convertRankingToInt(userTable[5]),
                                        pp, convertThousandsStringToInt(userTable[11]),convertThousandsStringToInt(userTable[14]),
                                        convertThousandsStringToInt(userTable[16]),convertThousandsStringToInt(userTable[26]),
                                        convertAccuracyToFloat(userTable[28]),convertThousandsStringToInt(userTable[31]),
                                        getTopFiveScores(), getMostPlayed())
                    print(theUser)
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

def convertAccuracyToFloat(accuracyNumber):
    return float(accuracyNumber[0:len(accuracyNumber)-1])

def convertRankingToInt(rankNumber):
    return int(rankNumber[1:len(rankNumber)])
def getTopFiveScores():
    return []

def getMostPlayed():
    return []
def findPPIndex(infoData):
    for index in range(len(infoData)):
        if infoData[index] == "PP":
            try:
                int(infoData[index + 1])
                return index
            except ValueError:
                if infoData[index + 1].find("0") == -1 and infoData[index + 1].find("1") == -1\
                        and infoData[index + 1].find("2") == -1 and infoData[index + 1].find("3") == -1\
                        and infoData[index + 1].find("4") == -1 and infoData[index + 1].find("5") == -1 \
                        and infoData[index + 1].find("6") == -1 and infoData[index + 1].find("7") == -1 \
                        and infoData[index + 1].find("8") == -1 and infoData[index + 1].find("9") == -1:
                    continue
                else:
                    return index
