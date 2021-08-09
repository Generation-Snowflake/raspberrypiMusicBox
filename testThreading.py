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
import pause

#---------- Show Run time----------
import time
start_time = time.time()
#----------------------------------

time.sleep(1)

r_old = {}
triger = ""
b_trg = False
a_trg = False
r_test = []
d_test = []
sd_test = []
ed_test = []
music_fin = {}
c = 0

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.mixer.init()


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

        while not self.stopped.wait(240.0):
            try:
                url = 'http://128.199.247.96:3000/api/music/getmusicloop'
                r = requests.get(url,allow_redirects=True)
                with open("music.json", "w") as output:
                    json.dump(r.json(), output)

                with open('music.json') as f:
                    r_off = json.load(f)

                r_test = r_off['data']
                d_test = r_off['download']
                sd_test = r_off['startDate']
                ed_test = r_off['endDate']
                # r_test = r.json()['data']
                # d_test = r.json()['download']
                # sd_test = r.json()['startDate']
                # ed_test = r.json()['endDate']

                # if triger == "":
                #     triger = str(r.json()['command'])
                # elif triger != str(r.json()['command']):
                #     #print('Triger')
                #     triger = str(r.json()['command'])
                #     a_trg = b_trg
                #     b_trg = not b_trg

                #return r
            except:
                print("some error...")


class BreakChange(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global c
        while not self.stopped.wait(600):
            c = 1
        return c


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
    else: return None


def send_feedback():
    path = '/'
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    print(music_fin)

    url = 'https://api.dv8automate.com/api/player/box/feedback'
    myobj = {
            'serialNumber':'10000000ce768306',
            'freeSpace':str(gigabytes_avail),
            'statusBox': 'offline',
            'speedNet':'spdTest',
            'startPlayTime':s_date,
            'currentVolume':100,
            'music':music_fin
            }
    requests.post(url, data = myobj)


class FeedbackSend(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(3600.0):#3600
            send_feedback()



def interval_loop60(x):
    if x == 0:
        x = 1
        s_mins = 0
        next = False
    elif x > 0 and x <= 10:
        x = 2
        s_mins = 10
        next = False
    elif x > 10 and x <= 20:
        x = 3
        s_mins = 20
        next = False
    elif x > 20 and x <= 30:
        x = 4
        s_mins = 30
        next = False
    elif x > 30 and x <= 40:
        x = 5
        s_mins = 40
        next = False
    elif x > 40 and x <= 50:
        x = 6
        s_mins = 50
        next = False
    else: 
        x = 1
        s_mins = 0
        next = True
    return [x,s_mins,next]


if __name__ == "__main__":

    url = 'http://128.199.247.96:3000/api/music/getmusicloop'
    r = requests.get(url,allow_redirects=True)
    
    with open("music.json", "w") as output:
        json.dump(r.json(), output)

    with open('music.json') as f:
        r_off = json.load(f)

    r_test = r_off['data']
    d_test = r_off['download']
    sd_test = r_off['startDate']
    ed_test = r_off['endDate']

    print(d_test)##
    print('-----------')##
    print(sd_test)##
    print('-----------')##
    print(ed_test)##
    print('-----------')##

    download_music(d_test)
    #send_feedback()

    stopFlag = threading.Event()
    thread = NineThread(stopFlag)
    thread.start()

    break_thread = BreakChange(stopFlag)
    feedback_thread = FeedbackSend(stopFlag)
    feedback_thread.start()

    # stopFlag = threading.Event()
    # thread2 = ClockThread(stopFlag)
    # thread2.start()
    #print('ssss')
    #timee = my_queue.get()
    #print(timee)

    music_list=[]
    b = 0

    time_now = datetime.now()
    s_hour = int(time_now.strftime('%H'))
    s_mins = time_now.strftime('%M')
    s_sec = time_now.strftime('%S')
    s_day = int(time_now.strftime('%d'))
    s_month = int(time_now.strftime('%m'))
    s_year = int(time_now.strftime('%Y'))
    s_date = time_now.strftime("%d/%m/%Y, %H:%M:%S")
    
    b_interval = interval_loop60(int(s_mins))

    
    #print(r_test['loop1'])##

    # for i in r_test['loop'+hour][(b_interval[0])]:##
    #     print(i)##

    if b_interval[2] == True:
        s_hour = s_hour + 1
        start_break = (6*s_hour)+b_interval[0]
    else:
        start_break = (6*s_hour)+b_interval[0]

    print('-----------')##
    print('break'+str(start_break))
    music_fin = {'break'+str(start_break):[]}
    print('-----------')##

    #for i in range (start_break,144):###
    for j in r_test['break'+str(start_break)]:
        music_list.append(j['sound'])
                
    print(music_list)
    print('-----------')##
    print('-----------')##


    #-----------directory for pi--------------
    # music_fin['break'+str(start_break)].append(music_list[0])
    # pygame.mixer.music.load("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))
    # music_fin['break'+str(start_break)].append(music_list[0])
    # pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

    #-----------directory form pc--------------
    music_fin['break'+str(start_break)].append(music_list[0])
    pygame.mixer.music.load("playlist/" + music_list.pop(0))
    music_fin['break'+str(start_break)].append(music_list[0])
    pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    print(music_fin)
    print('-----------')##
    
    # pause.until(datetime(s_year, s_month, s_day, s_hour, b_interval[1]))

    pygame.mixer.music.play()
    break_thread.start()
    print("Play first")
    running = True
    while running:
        if c == 1:
            pygame.mixer.music.stop()
            b = b + 1
            music_list = []
            print(music_list)
            for j in r_test['break'+str(start_break+b)]:
                music_list.append(j['sound'])
            music_fin['break'+str(start_break+b)] = []
            print('-----------')##
            print('-----------')##
            print('break'+str(start_break+b))##
            print(music_list)##
            music_fin[list(music_fin.keys())[-1]].append(music_list[0])
            pygame.mixer.music.load("playlist/" + music_list.pop(0))
            #pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
            pygame.mixer.music.play()
            c = 0
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:    
                if len ( music_list ) > 0:
                    #-----------directory for pi--------------  
                    # music_fin['break'+str(start_break)].append(music_list[0])     
                    #pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

                    #-----------directory form pc--------------
                    music_fin[list(music_fin.keys())[-1]].append(music_list[0])
                    pygame.mixer.music.queue("playlist/" + music_list.pop(0))
                    print('-----------')##
                    print('-----------')##
                    print(music_fin)##

               # print('aa')
    print("--- %s seconds ---" % (time.time() - start_time)) #show time ##