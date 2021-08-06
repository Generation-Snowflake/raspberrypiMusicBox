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

#---------- Show Run time----------
import time
start_time = time.time()
#----------------------------------


time.sleep(1)

pygame.init()
pygame.mixer.init()
r_old = {}
triger = ""
b_trg = False
a_trg = False
r_test = []
d_test = []
sd_test = []
ed_test = []



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
        global d_test
        global sd_test
        global ed_test

        while not self.stopped.wait(60.0):
            try:
                url = 'http://128.199.247.96:3000/api/music/getmusicloop'
                r = requests.get(url,allow_redirects=True)
                r_test = r.json()['data']
                d_test = r.json()['download']
                sd_test = r.json()['startDate']
                ed_test = r.json()['endDate']

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


def download_music(d_test):
    if str(d_test) == "True":
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


def interval_loop60(x):
    if x == 0:
        x = '1'
        s_mins = 0
        next = False
    elif x > 0 and x <= 10:
        x = '2'
        s_mins = 10
        next = False
    elif x > 10 and x <= 20:
        x = '3'
        s_mins = 20
        next = False
    elif x > 20 and x <= 30:
        x = '4'
        s_mins = 30
        next = False
    elif x > 30 and x <= 40:
        x = '5'
        s_mins = 40
        next = False
    elif x > 40 and x <= 50:
        x = '6'
        s_mins = 50
        next = False
    else: 
        x = '1'
        s_mins = 0
        next = True
    return [x,s_mins,next]


if __name__ == "__main__":

    url = 'http://128.199.247.96:3000/api/music/getmusicloop'
    r = requests.get(url,allow_redirects=True)
    r_test = r.json()['data']
    d_test = r.json()['download']
    sd_test = r.json()['startDate']
    ed_test = r.json()['endDate']

    print(d_test)##
    print('-----------')##
    print(sd_test)##
    print('-----------')##
    print(ed_test)##
    print('-----------')##

    download_music(d_test)

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
    loop_list=[]##
    music_list3=[]##
    music_list4=[]##
    music_list5=[]##
    music_list6=[]##

    time_now = datetime.now()
    hour = time_now.strftime('%H')
    mins = time_now.strftime('%M')
    
    b_interval = interval_loop60(int(mins))

    print(('break'+b_interval[0]))##

    print('-----------')##
    #print(r_test['loop1'])##

    # for i in r_test['loop'+hour][(b_interval[0])]:##
    #     print(i)##
    if b_interval[2] == True:
        loop_count = int(hour)+1
    else:
        loop_count = int(hour)


    for i in range (loop_count,24):
        if str(i) == str(loop_count):
            for j in range(int(b_interval[0]),7):
                for l in r_test['loop'+str(loop_count)]['break'+str(j)]:
                    music_list.append(l['sound']) 
        else:
            for k in r_test['loop'+str(i)]:
                for m in r_test['loop'+str(i)][str(k)]:
                    music_list.append(m['sound'])
                
    print(music_list)

    #-----------directory for pi--------------
    # pygame.mixer.music.load("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))
    # pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

    #-----------directory form pc--------------
    # pygame.mixer.music.load("playlist/" + music_list.pop(0))
    # pygame.mixer.music.queue ("playlist/" + music_list.pop(0))

    # pygame.mixer.music.set_endevent(pygame.USEREVENT)
    # pygame.mixer.music.play()
    # print("Play first")
    # running = True
    # while running:
    #     if a_trg != b_trg:
    #         pygame.mixer.music.stop()
    #         music_list=[]
    #         time.sleep(1)
    #         for i in r_test:#+str(j)
    #             music_list.append(i['sound'])

    #         #print('play again')
    #         print(music_list)
    #         #-----------directory for pi--------------
    #         #pygame.mixer.music.load("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

    #         #-----------directory form pc--------------
    #         pygame.mixer.music.load("playlist/" + music_list.pop(0))

    #         #pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    #         pygame.mixer.music.set_endevent(pygame.USEREVENT)
    #         pygame.mixer.music.play()
    #         print("Play again")
    #         a_trg = b_trg
    #     for event in pygame.event.get():

    #         if event.type == pygame.USEREVENT:    
    #             if len ( music_list ) > 0:
    #                 #-----------directory for pi--------------       
    #                 #pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

    #                 #-----------directory form pc--------------
    #                 pygame.mixer.music.queue("playlist/" + music_list.pop(0))

    #            # print('aa')
    print("--- %s seconds ---" % (time.time() - start_time)) #show time