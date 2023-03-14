from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
def webScraper(startEndTuple):
    playerDictionary = {}
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.pw/u/" + str(id) + "?mode=0&rx=0"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        page = requests.get(url, allow_redirects=False, headers=headers)
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
                if (pp > 0):
                    weirdTupple = getScores(id, "first")
                    theUser = AkatsukiWebScrape.UserInfo(url,None,None, pp, convertThousandsStringToInt(userTable[ppIndex+3]),
                                convertThousandsStringToInt(userTable[ppIndex+6]),convertThousandsStringToInt(userTable[ppIndex+8]),
                                convertThousandsStringToInt(userTable[ppIndex+18]),convertAccuracyToFloat(userTable[ppIndex+20]),
                                convertThousandsStringToInt(userTable[ppIndex+23]), weirdTupple[1], getScores(id, "best"),
                                getMostPlayed(id), weirdTupple[0])
                    playerDictionary[username] = theUser
                    print(theUser)
            elif userTable[0] == "Clan" and userTable[1] == "PP":
                username = ""
                for x in range(0, len(nameElements)):
                    username = username + nameElements[x] + " "
                username = username[0:len(username) - 1]
                if int(id) == 50615:
                    userTable.pop(0)
                    userTable.pop(0)
                    username = "Kat_"
                if int(id) == 78485:
                    userTable.pop(0)
                    username = "pea_old"
                if int(id) == 80388:
                    userTable.pop(0)
                    userTable.pop(0)
                    username = "[ MYSTIK ]"
                print(url)
                if nameElements[0] == "[[":
                    username = nameElements[2]
                print(username)
                ppIndex = findPPIndex(userTable)
                pp = convertThousandsStringToInt(userTable[ppIndex + 1])
                if (pp > 0):
                    weirdTupple = getScores(id, "first")
                    theUser = AkatsukiWebScrape.UserInfo(url, None, None, pp,convertThousandsStringToInt(userTable[5]),
                                        convertThousandsStringToInt(userTable[8]),convertThousandsStringToInt(userTable[10]),
                                        convertThousandsStringToInt(userTable[20]),convertAccuracyToFloat(userTable[22]),
                                        convertThousandsStringToInt(userTable[25]),weirdTupple[1], getScores(id, "best"),
                                        getMostPlayed(id), weirdTupple[0])
                    playerDictionary[username] = theUser
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
                    weirdTupple = getScores(id, "first")
                    theUser = AkatsukiWebScrape.UserInfo(url, convertRankingToInt(userTable[2]), convertRankingToInt(userTable[5]), pp,
                                    convertThousandsStringToInt(userTable[ppIndex+3]),convertThousandsStringToInt(userTable[ppIndex+6]),
                                    convertThousandsStringToInt(userTable[ppIndex+8]),convertThousandsStringToInt(userTable[ppIndex + 18]),
                                    convertAccuracyToFloat(userTable[ppIndex+20]),convertThousandsStringToInt(userTable[ppIndex+23]),
                                    weirdTupple[1], getScores(id, "best"), getMostPlayed(id), weirdTupple[0])
                    playerDictionary[username] = theUser
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
                    weirdTupple = getScores(id, "first")
                    theUser = AkatsukiWebScrape.UserInfo(url, convertRankingToInt(userTable[2]), convertRankingToInt(userTable[5]),
                                        pp, convertThousandsStringToInt(userTable[11]),convertThousandsStringToInt(userTable[14]),
                                        convertThousandsStringToInt(userTable[16]),convertThousandsStringToInt(userTable[26]),
                                        convertAccuracyToFloat(userTable[28]),convertThousandsStringToInt(userTable[31]),
                                        weirdTupple[1], getScores(id, "best")[0], getMostPlayed(id), weirdTupple[0])
                    print(theUser)
                    playerDictionary[username] = theUser
            else:
                continue
    return playerDictionary
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
def getScores(id, type):
    url = "https://akatsuki.pw/api/v1/users/scores/"+str(type)+"?mode=0&p=1&l=10&rx=0&id="+str(id)+"&uid="+str(id)+"&actual_id=0"
    page = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    scoresList = soup.text.split()
    try:
        index = scoresList.index("\"total\":")
        firsts = str(scoresList[index + 1])
        firsts = int(firsts[0:len(firsts) - 1])
    except ValueError:
        firsts = 0
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
            if score[x] == "\"count_300\":":
                num300 = str(score[x + 1])
                num300 = int(num300[0:len(num300) - 1])
            if score[x] == "\"count_100\":":
                num100 = str(score[x + 1])
                num100 = int(num100[0:len(num100) - 1])
            if score[x] == "\"count_50\":":
                num50 = str(score[x + 1])
                num50 = int(num50[0:len(num50) - 1])
            if score[x] == "\"count_miss\":":
                numMiss = str(score[x + 1])
                numMiss = int(numMiss[0:len(numMiss) - 1])
        if len(allScores) == 0:
            return None
        else:
            userScores.append(AkatsukiWebScrape.ScoreInfo(beatMapURL, artist, name, diff, scorePlay, combo, totalPP, acc,
                                                          num300, num100, num50, numMiss))
    return (userScores, firsts)

def getMostPlayed(id):
    url = "https://akatsuki.pw/api/v1/users/most_played?id="+str(id)+"&rx=0&mode=0"
    page = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    scoresList = soup.text.split()
    idkWhatToCallThis2 = str("\"playcount\":")
    ender = "}"
    allScores = []
    userMostScores = []
    for x in range(len(scoresList)):
        if idkWhatToCallThis2 == str(scoresList[0]):
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
            if score[x] == "\"playcount\":":
                count = str(score[x + 1])
                count = int(count[0:len(count) - 1])
        if len(allScores) == 0:
            return None
        elif len(userMostScores) >= 10:
            break
        else:
            userMostScores.append(AkatsukiWebScrape.MostScoreInfo(beatMapURL, count, artist, name, diff))
    return userMostScores