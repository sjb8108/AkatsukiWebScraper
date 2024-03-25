from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
import math
def webScraper(startEndTuple):
    playerDictionary = {}
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.gg/api/v1/users/full?id="+str(id)
        basicUserData = requests.get(url).json()
        if basicUserData['code'] == 200:
            userID = id
            userName = basicUserData['username']
            userURL = url
            clanName = basicUserData['clan']['name']
            clanTag = basicUserData['clan']['tag']
            followers = basicUserData['followers']
            country = basicUserData['country']
            registerDate = getDate(basicUserData['registered_on'])
            lastDateOnline = getDate(basicUserData['latest_activity'])
            gamemodes = getAllGamemodes(basicUserData['stats'], id)
        else:
            pass
    return playerDictionary

def getDate(stringDate):
    splitDate = stringDate.split("-")
    year = splitDate[0]
    month = int(splitDate[1])
    splitDay = splitDate[2].split("T")
    day = int(splitDay[0])
    timeSplit = splitDay[1].split(":")
    hour = int(timeSplit[0])
    minute = timeSplit[1]
    afternoon = False
    monthString = ""
    if(month == 1):
        monthString = "Janurary"
    elif(month == 2):
        monthString = "February"
    elif(month == 3):
        monthString = "March"
    elif(month == 4):
        monthString = "April"
    elif(month == 5):
        monthString = "May"
    elif(month == 6):
        monthString = "June"
    elif(month == 7):
        monthString = "July"
    elif(month == 8):
        monthString = "August"
    elif(month == 9):
        monthString = "September"
    elif(month == 10):
        monthString = "October"
    elif(month == 11):
        monthString = "November"
    else:
        monthString = "December"
    if(hour >= 0 or hour < 12):
        afternoon = False
    else:
        hour = hour - 12
        afternoon = True
    if(day % 10 == 1):
        if(afternoon):
            return " " + monthString + " " + str(day) + "st " + year + " at " + str(hour) + ":" + minute + " AM"
        else:
            return " " + monthString + " " + str(day) + "st " + year + " at " + str(hour) + ":" + minute + " PM"
    elif(day % 10 == 2):
        if (afternoon):
            return " " + monthString + " " + str(day) + "nd " + year + " at " + str(hour) + ":" + minute + " AM"
        else:
            return " " + monthString + " " + str(day) + "nd " + year + " at " + str(hour) + ":" + minute + " PM"
    elif(day % 10 ==3):
        if (afternoon):
            return " " + monthString + " " + str(day) + "rd " + year + " at " + str(hour) + ":" + minute + " AM"
        else:
            return " " + monthString + " " + str(day) + "rd " + year + " at " + str(hour) + ":" + minute + " PM"
    else:
        if (afternoon):
            return " " + monthString + " " + str(day) + "th " + year + " at " + str(hour) + ":" + minute + " AM"
        else:
            return " " + monthString + " " + str(day) + "th " + year + " at " + str(hour) + ":" + minute + " PM"

def getAllGamemodes(gamemodeStat, id):
    gamemodeArray = ["Standard", "Taiko", "CTB", "Mania",
                     "StandardRelax", "TaikoRelax", "CTBRelax", "ManiaRelax",
                     "StandardAuto", "TaikoAuto", "CTBAuto", "ManiaAuto"]
    gamemodeNameArray = ["std", "taiko", "ctb", "mania"]
    gamemodeDict = dict()
    count = 0
    type = 0
    for i in range(len(gamemodeArray)):
        gamemodeNameArrayIndex = i % 4
        mode = i % 4
        if(count == 4):
            type+=1
            count = 0
        else:
            count+=1
        gamemodeName = gamemodeNameArray[gamemodeNameArrayIndex]
        gamemodeKey = gamemodeArray[i]
        singleGamemodeDict = gamemodeStat[0][gamemodeName]
        globalRank = singleGamemodeDict['global_leaderboard_rank']
        if globalRank == None:
            globalRank = -1
        countryRank = singleGamemodeDict['country_leaderboard_rank']
        if countryRank == None:
            countryRank = -1
        totalPerformancePoints = singleGamemodeDict['pp']
        rankedScore = singleGamemodeDict['ranked_score']
        totalScore = singleGamemodeDict['total_score']
        playcount = singleGamemodeDict['playcount']
        totalHits = singleGamemodeDict['total_hits']
        accuracyFloat = float(singleGamemodeDict['accuracy'])
        accuracy = math.ceil((accuracyFloat*100)/100)
        maxCombo = singleGamemodeDict['max_combo']
        replaysWatched = singleGamemodeDict['replays_watched']
        levelFloat = float(singleGamemodeDict['level'])
        level = math.ceil((levelFloat*100)/100)
        bestScoreList = getBestScores(id, mode, type)
        bestScore = { gamemodeKey[i] : bestScoreList }

        print("test")

    return None
def getBestScores(id, mode, type):
    url = "https://akatsuki.gg/api/v1/users/scores/best?mode="+str(mode)+"&rx="+str(type)+"&id="+str(id)
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
                    if score[n].__contains__("u0026"):
                        name = name + "&" + " "
                    else:
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
            #Starting debugging here
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
            #Start debugging here
        if len(allScores) == 0:
            return None
        elif len(userMostScores) >= 10:
            break
        else:
            userMostScores.append(AkatsukiWebScrape.MostScoreInfo(beatMapURL, count, artist, name, diff))
    return userMostScores