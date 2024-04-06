from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
import math
import mods
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
        monthString = "January"
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
        if globalRank is None:
            globalRank = -1
        countryRank = singleGamemodeDict['country_leaderboard_rank']
        if countryRank is None:
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
        bestScore = {gamemodeKey: bestScoreList}

    return None
def getBestScores(id, mode, type):
    url = "https://akatsuki.gg/api/v1/users/scores/best?mode="+str(mode)+"&l=50&rx="+str(type)+"&id="+str(id)
    scoresDic = requests.get(url).json()
    if scoresDic['scores'] is None:
        pass
    else:
        for i in range(0, len(scoresDic['scores'])):
            score = scoresDic['scores'][i]
            websiteLink = "https://osu.ppy.sh/beatmapsets/" + str(score['beatmap']['beatmapset_id']) + "#osu/" + str(score['beatmap']['beatmap_id'])
            songInfo = getSongInfo(score['beatmap']['song_name'])
            songArtist = songInfo[0]
            songName = songInfo[1]
            songDiff = songInfo[2]
            modNumber = score['mods']
            modsCombo = mods.Mods(modNumber).short

def getSongInfo(beatmap):
    songArray = beatmap.split(" ")
    songArtist = ""
    songName = ""
    songDiff = ""
    songInfo = []
    i = 0
    while(True):
        songArtist += (songArray[i] + " ")
        i+=1
        if(songArray[i] == "-"):
            songArtist = songArtist[:-1]
            songInfo.append(songArtist)
            break
    i+=1
    while(True):
        songName += (songArray[i] + " ")
        i+=1
        if(songArray[i][0] == "["):
            songName = songName[:-1]
            songInfo.append(songName)
            break
    while(True):
        songDiff += (songArray[i] + " ")
        i+=1
        if(i >= len(songArray)):
            songDiff = songDiff[1:-2]
            songInfo.append(songDiff)
    return songInfo
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