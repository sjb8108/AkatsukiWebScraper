from bs4 import BeautifulSoup
import requests
import AkatsukiWebScrape
def webScraper(startEndTuple):
    playerDictionary = {}
    for id in range(startEndTuple[0], startEndTuple[1]):
        url = "https://akatsuki.gg/api/v1/users/full?id="+str(id)
        basicUserData = requests.get(url).json()
        if basicUserData['code'] == 200:
            print("yep")
        else:
            pass
    return playerDictionary

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