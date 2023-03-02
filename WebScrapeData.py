import time

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
                            convertThousandsStringToInt(userTable[ppIndex+23]), getTopFiveScores(id), getMostPlayed(id))
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
                                        convertThousandsStringToInt(userTable[25]),getTopFiveScores(id), getMostPlayed(id))
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
                                    getTopFiveScores(id), getMostPlayed(id))
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
                                        getTopFiveScores(id), getMostPlayed(id))
                    for score in theUser.scores:
                        print(score)
            else:
                pass
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
def getTopFiveScores(id):
    url = "https://akatsuki.pw/api/v1/users/scores/best?mode=0&p=1&l=10&rx=0&id="+str(id)+"&uid="+str(id)+"&actual_id=0"
    page = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    scoresList = soup.text.split()
    idkWhatToCallThis = str("\"score\":")
    ender = "}"
    allScores = []
    userScores = []
    for x in range(len(scoresList)):
        if idkWhatToCallThis == str(scoresList[0]):
            score = []
            score.append(str(scoresList[0]))
            scoresList.remove(scoresList[0])
            for x in range(len(scoresList)):
                if ender == str(scoresList[x]):
                    break
                else:
                    score.append(scoresList[x])
            allScores.append(score)
        else:
            scoresList.remove(scoresList[0])
    for score in allScores:
        for x in range(len(score)):
            if score[x] == "\"beatmapset_id\":":
                id = str(score[x+1])
                id = id[0:len(id)-1]
                beatMapURL = "https://osu.ppy.sh/beatmapsets/"+id
            if score[x] == "\"song_name\":":
                artist = ""
                name = ""
                diff = ""
                for j in range(x, score.index("\"ar\":")):
                    if score[j] == "-":
                        indexStart = j
                        for k in range(x+1, j):
                            artist = artist + score[k] + " "
                        artist = artist[1:len(artist)-1]
                    elif score[j].startswith("["):
                        indexEnd = j
                        for m in range(j, score.index("\"ar\":")):
                            diff = diff + score[m] + " "
                        diff = diff[1:len(diff)-4]
                for n in range(indexStart+1,indexEnd):
                    if score[n].startswith("\""):
                        break
                    name = name + score[n] + " "
                name = name[0:len(name)-1]
            if score[x] == "\"score\":":
                scorePlay = str(score[x + 1])
                scorePlay = int(scorePlay[0:len(scorePlay) - 1])
            if score[x] == "\"max_combo\":":
                combo = str(score[x + 1])
                combo = int(combo[0:len(combo) - 1])
            if score[x] == "\"pp\":":
                totalPP = str(score[x + 1])
                totalPP = float(totalPP[0:len(totalPP) - 1])
            if score[x] == "\"accuracy\":":
                acc = str(score[x + 1])
                acc = float(acc[0:len(acc) - 1])
        userScores.append(AkatsukiWebScrape.ScoreInfo(beatMapURL, artist, name, diff, scorePlay, combo, totalPP, acc))
    return userScores

def getMostPlayed(id):
    return []

