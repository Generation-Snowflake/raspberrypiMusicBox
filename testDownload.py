import requests
import json
url = 'http://128.199.247.96:3000/api/music/getmusicloop'  #playlist URL http://128.199.247.96:3000/api/music
r = requests.get(url,allow_redirects=True)

#r = str(r.content).split(",")  # split each song to list

# python_obj = json.loads(r.json())

dicTest = r.json()["loop1"]

for i in len(dicTest["break1"]):
    print(dicTest["break1"][i])

#{'loop1': 
# {'break1': [
# {'sound': 'Sunkissed.mp3', 'duration': '00:04.02'}, 
# {'sound': 'JustinBieber-Sorry.mp3', 'duration': '00:03.25'}, 
# {'sound': 'EdSheeran-ShapeofYou.mp3', 'duration': '00:04.23'}, 
# {'sound': 'EdSheeran-ShapeofYou.mp3', 'duration': '00:04.23'}, 
# {'sound': 'Maroon5-Sugar.mp3', 'duration': '00:05.01'}], 
# 'break2': [
# {'sound': 'OneRepublic-CountingStars.mp3', 'duration': '00:04.43'}, 
# {'sound': 'COVERALLYxTwoPopetorn-LikeImGonnaLoseYou.mp3', 'duration': '00:04.13'}, 
# {'sound': 'Anne-Marie-2002.mp3', 'duration': '00:03.14'}, 
# {'sound': 'TaylorSwift-YouBelongWithMe.mp3', 'duration': '00:03.48'}]}}



