import time

from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
import math
import mods
def webScraper(startEndTuple):
    playerDictionary = {}
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.gg/api/v1/users/full?id="+str(id)
        time.sleep(1)
        basicUserData = requests.get(url).json()
        if basicUserData['code'] == 200:
            userID = id
            userName = basicUserData['username']
            userURL = "https://akatsuki.gg/u/" + str(userID)
            clanName = basicUserData['clan']['name']
            clanTag = basicUserData['clan']['tag']
            followers = basicUserData['followers']
            country = basicUserData['country']
            registerDate = getDate(basicUserData['registered_on'])
            lastDateOnline = getDate(basicUserData['latest_activity'])
            gamemodes = getAllGamemodes(basicUserData['stats'], id)
            playerDictionary[id] = AkatsukiWebScrape.UserInfo(userURL, userName, userID, clanName,
                                                              clanTag, followers, country,
                                                              registerDate, lastDateOnline, gamemodes)
        else:
            pass
    return playerDictionary

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
        bestScoresList = getScores(id, mode, type, "best")
        mostPlayedScoresList = getMostPlayed(id, mode, type)
        firstPlaceInfo = getFirstPlaceInfo(id, mode, type, "first")
        totalFirstPlaces = firstPlaceInfo[0]
        firstPlaceScoresList = firstPlaceInfo[1]
        mostRecentScoresList = getScores(id, mode, type, "recent")
        pinnedScoresList = getScores(id, mode, type, "pinned")
        gamemodeDict[gamemodeKey] = AkatsukiWebScrape.GamemodeInfo(globalRank, countryRank, totalPerformancePoints,
                                                                   rankedScore, totalScore, playcount, totalHits,
                                                                   accuracy, maxCombo, replaysWatched, level,
                                                                   bestScoresList, mostPlayedScoresList, totalFirstPlaces,
                                                                   firstPlaceScoresList, mostRecentScoresList,
                                                                   pinnedScoresList)
    return gamemodeDict
def getScores(id, mode, type, scored):
    url = "https://akatsuki.gg/api/v1/users/scores/"+scored+"?mode="+str(mode)+"&l=50&rx="+str(type)+"&id="+str(id)
    time.sleep(1)
    scoresDic = requests.get(url).json()
    scoreList = []
    if scoresDic['scores'] is None:
        return None
    else:
        for i in range(0, len(scoresDic['scores'])):
            score = scoresDic['scores'][i]
            websiteLink = "https://osu.ppy.sh/beatmapsets/" + str(score['beatmap']['beatmapset_id']) + \
                          "#" + getMode(mode) +"/" + str(score['beatmap']['beatmap_id'])
            songInfo = getSongInfo(score['beatmap']['song_name'])
            songArtist = songInfo[0]
            songName = songInfo[1]
            songDiff = songInfo[2]
            rankedStatus = getRankStatus(score['beatmap']['ranked'])
            approachRate = score['beatmap']['ar']
            od = score['beatmap']['od']
            playScore = score['score']
            playCombo = score['max_combo']
            playPerformancePoints = score['pp']
            playAcc = score['accuracy']
            play300 = score['count_300'] + score['count_geki']
            play100 = score['count_100'] + score['count_katu']
            play50 = score['count_50']
            playMiss = score['count_miss']
            modNumber = score['mods']
            modsCombo = mods.Mods(modNumber).short
            rank = score['rank']
            datePlayed = getDate(score['time'])
            completed = True
            if(scored == "recent" or scored == "pinned"):
                complete = score['completed']
                if(complete == 0):
                    completed = False
                    rank = "F"
            scoreList.append(AkatsukiWebScrape.ScoreInfo(websiteLink, songArtist, songName,
                                                             songDiff, rankedStatus, approachRate,
                                                             od, playScore, playCombo, playPerformancePoints,
                                                             playAcc, play300, play100, play50, playMiss,
                                                             modsCombo, rank, datePlayed, completed))
        return scoreList

def getMostPlayed(id, mode, type):
    url = "https://akatsuki.gg/api/v1/users/scores/most_played?mode="+str(mode)+"&l=50&rx="+str(type)+"&id="+str(id)
    mostScoresDic = requests.get(url).json()
    mostScoresList = []
    if mostScoresDic['most_played_beatmaps'] is None:
        return None
    else:
        for i in range(0, len(mostScoresDic['most_played_beatmaps'])):
            score = mostScoresDic['most_played_beatmap'][i]
            websiteLink = "https://osu.ppy.sh/beatmapsets/" + str(score['beatmap']['beatmapset_id']) +\
                          "#"+ getMode(mode) +"/" + str(score['beatmap']['beatmap_id'])
            songInfo = getSongInfo(score['beatmap']['song_name'])
            songArtist = songInfo[0]
            songName = songInfo[1]
            songDiff = songInfo[2]
            rankedStatus = getRankStatus(score['beatmap']['ranked'])
            playcount = score['playcount']
            mostScoresList.append(AkatsukiWebScrape.MostScoreInfo(websiteLink, songArtist, songName,
                                                                  songDiff, rankedStatus, playcount))
        return mostScoresList

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

def getFirstPlaceInfo(id, mode, type, scored):
    url = "https://akatsuki.gg/api/v1/users/scores/first?mode="+str(mode)+"&l=50&rx="+str(type)+"&id="+str(id)
    firstPlaceScoresDic = requests.get(url).json()
    totalFirstPlaces = firstPlaceScoresDic['total']
    if totalFirstPlaces == 0:
        return (0, None)
    else:
        firstPlaceScores = getScores(id, mode, type, scored)
        return (totalFirstPlaces, firstPlaceScores)
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
            break
    return songInfo

def getRankStatus(status):
    if(status == 2):
        return "ranked"
    elif(status == 5):
        return "loved"
    elif(status == 3):
        return "Qualified"
    else:
        return "Unranked"

def getMode(mode):
    if (mode == 0):
        return "osu"
    elif (mode == 1):
        return "taiko"
    elif (mode == 2):
        return "fruits"
    else:
        return "mania"