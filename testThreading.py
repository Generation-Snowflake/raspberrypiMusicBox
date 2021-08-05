import threading
import queue
import requests
import json
import time
from datetime import datetime
from requests.api import request
#import speedtest
#for check space 
import psutil
#from tqdm import tqdm
import os
import pygame

time.sleep(60)

pygame.init()
pygame.mixer.init()
r_old = {}
triger = ""
b_trg = False
a_trg = False
r_test = []



#my_queue = queue.Queue()

class NineThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global r_old
        global triger
        global b_trg  
        global a_trg
        global r_test
        #while True:
        while not self.stopped.wait(10.0):
            try:
                url = 'http://128.199.247.96:3000/api/music/getmusicloop'
                r = requests.get(url,allow_redirects=True)
                r_test = r.json()['loop1']['break1']
                #print("Loading")
                #print(r.text)
                #print(str(r.json()['command']))
                
                # if r_old == {}:
                #     r_old = r.text

                # elif r_old!=r.text:
                #     print('kn')
                #     r_old = r.text

                if triger == "":
                    triger = str(r.json()['command'])
                elif triger != str(r.json()['command']):
                    #print('Triger')
                    triger = str(r.json()['command'])
                    a_trg = b_trg
                    b_trg = not b_trg

                #return r
            except:
                print("some error...")
        #print(r.json())
        

class ClockThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1.0):
            time_start = datetime.now()
            hour = time_start.strftime("%H")
            min = time_start.strftime("%M")
            #my_queue.put(hour)
        return hour, min

def getserial():
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
                f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial

# def update_playlist():
#     try:
#         url = 'http://128.199.247.96:3000/api/music/getmusicloop'
#         r = requests.get(url,allow_redirects=True)
#     except ValueError:
#         print(ValueError)
#     print('nine')
#     return r

def download_music(r):
    if str(r.json()['download']) == "True":
        if os.path.isdir('playlist') == False:
            os.mkdir('playlist')

        url = 'http://128.199.247.96:3000/api/music'
        playlist = requests.get(url,allow_redirects=True)
        playlist = str(playlist.content).split(',')

        playlist_lst = str(playlist).split('"')
        playlist_lst.pop(playlist_lst.index("['b\\'["))
        playlist_lst.pop(playlist_lst.index("]\\'']"))

        for i,enum in enumerate(playlist_lst):
            if enum == "', '":
                playlist_lst.pop(i)

        for j in range (0,len(playlist_lst)):
            music = playlist_lst[j].split('/')
            music_download = requests.get(playlist_lst[j],allow_redirects=True)
            open('playlist/'+music[-1],('wb')).write(music_download.content)

def send_feedback():
    path = '/'
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024

    url = 'https://api.dv8automate.com/api/player/box/feedback'
    myobj = {
            'serialNumber':'10000000ce768306',
            'freeSpace':str(gigabytes_avail),
            'statusBox': 'offline',
            'speedNet':'spdTest',
            'startPlayTime':datetime.now(),
            'currentVolume':10
            }
    requests.post(url, data = myobj)

if __name__ == "__main__":

    #r = NineThread().run()
    url = 'http://128.199.247.96:3000/api/music/getmusicloop'
    r = requests.get(url,allow_redirects=True)
    r_test = r.json()['loop1']['break1']


    stopFlag = threading.Event()
    thread = NineThread(stopFlag)
    thread.start()

    # stopFlag = threading.Event()
    # thread2 = ClockThread(stopFlag)
    # thread2.start()
    #print('ssss')
    #timee = my_queue.get()
    #print(timee)

    music_list=[]
    music_list2=[]
    music_list3=[]
    music_list4=[]
    music_list5=[]
    music_list6=[]
    
    #print(thread.run().json()['loop1']['break1'])
   

    #for j in range (1,7):
    for i in r_test:#+str(j)  # thread.run().json()['loop1']['break1']
        music_list.append(i['sound'])


    #print('-----------')
    print(music_list)
    #pygame.mixer.music.load("01.Lotus_sVisa10(01-15Aug21).mp3")

    pygame.mixer.music.load("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))
    pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    print("Play first")
    running = True
    while running:
        if a_trg != b_trg:
            pygame.mixer.music.stop()
            music_list=[]
            time.sleep(1)
            for i in r_test:#+str(j)
                music_list.append(i['sound'])
<<<<<<< HEAD
	#print('play again')
            print(music_list)
            pygame.mixer.music.load("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))
=======
            print(music_list)
            pygame.mixer.music.load("playlist/" + music_list.pop(0))
>>>>>>> 11229e0280322a58182c2f757c0001de6ff216bd
            #pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            pygame.mixer.music.play()
            print("Play again")
            a_trg = b_trg
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT:    
                if len ( music_list ) > 0:       
                    pygame.mixer.music.queue ( "/home/pi/raspberrypiMusicBox/playlist/" +music_list.pop(0) )
               # print('aa')

    # pygame.mixer.music.load ( playlist.pop(0) )  # Get the first track from the playlist
    # pygame.mixer.music.queue ( playlist.pop(0) ) # Queue the 2nd song
    # pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
    # pygame.mixer.music.play()
    #time.sleep(10)
    #stopFlag.set()
    #
