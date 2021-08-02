import requests
from tqdm import tqdm
import os

if os.path.isdir('playlist') == False:
    os.mkdir('playlist')

url = 'http://128.199.247.96:3000/api/music'
playlist = requests.get(url,allow_redirects=True)
playlist = str(playlist.content).split(',')

playlist_lst = str(playlist).split('"')
playlist_lst.pop(playlist_lst.index("['b\'["))
playlist_lst.pop(playlist_lst.index("]\'']"))
for i,enum in enumerate(playlist_lst):
    if enum == "', '":
        playlist_lst.pop(i)

for j in tqdm(range (0,len(playlist_lst))):
    music = playlist_lst[j].split('/')
    music_download = requests.get(playlist_lst[j],allow_redirects=True)
    open('playlist/'+music[-1],('wb')).write(music_download.content)