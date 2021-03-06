import threading
import requests
import json
import time
from datetime import datetime, timedelta
from requests.api import request
import speedtest
import psutil
import os
import pygame
import urllib.request
import alsaaudio

time.sleep(30)

r_data = []
r_download = []
r_startDate = []
r_endDate = []
music_finish = {}
count = 0

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
pygame.mixer.init(44100,-16,8129)


def getserial():
    # Extract serial from cpuinfo file
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
    

class RequestThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global r_data
        global r_download
        global r_startDate
        global r_endDate

        while not self.stopped.wait(240.0):
            try:
                url = 'http://128.199.247.96:3000/api/music/getmusicloop/'+getserial()
                #url = 'http://128.199.247.96:3000/api/music/getmusicloop/10000000588a85c2'
                r = requests.get(url,allow_redirects=True)
                # print('playlistresq:'+r.text)
                with open("music.json", "w") as output:
                    json.dump(r.json(), output)

                with open('music.json') as f:
                    r_off = json.load(f)

                r_data = r_off['data']
                r_download = r_off['download']
                r_startDate = r_off['startDate']
                r_endDate = r_off['endDate']
                r_volume = r_off['volume']
                volume = alsaaudio.Mixer('Speaker')
                current_volume = volume.getvolume()
                volume.setvolume(int(r_volume))
                print('Requested')
                print('Volume =', current_volume)
            except:
                print("Request fail...")


class BreakChange(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global count
        while not self.stopped.wait(600):
            count = 1
        return count


def download_music(r_download):
    if str(r_download) == "True":
            if os.path.isdir('playlist') == False:
                os.mkdir('playlist')
            try:
                url = 'https://api.dv8automate.com/api/music/'+getserial()
                #url = 'https://api.dv8automate.com/api/music/10000000588a85c2'
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
                print('Downloaded')
            except:
                print('Download fail...')
    else:
        print('Not download')
        return None


def delete_music():
    try:
        url = 'http://128.199.247.96:3000/api/music/getmusicloop/'+getserial()
        #url = 'http://128.199.247.96:3000/api/music/getmusicloop/10000000588a85c2'
        delete_r = requests.get(url,allow_redirects=True)

        for i in delete_r.json()['delete']:
            try:
                os.remove('playlist/'+i)
            except OSError:
                pass
        print('Deleted')
    except:
        print("Not delete")


def send_feedback():
    #print('firstFeedback')##
    path = '/'
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    #print(music_finish)##

    try:
        spd_test = speedtest.Speedtest()
        netSpeed = spd_test.download()
    except:
        netSpeed = '0'
        print('Speed test error...')##

    try:
        #print('url try')##
        url = 'https://api.dv8automate.com/api/player/box/feedback/'
        myobj = {
                'serialNumber':getserial(), #100000000ec590a2str(getserial())
                'freeSpace':str(gigabytes_avail),
                'statusBox':'Online',
                'speedNet':netSpeed/1000000,
                'startPlayTime':s_date,
                'currentVolume':100,
                'playlist':str(music_finish)
                }
        x = requests.post(url, data = myobj)
        print('Send feedback')
    except:
        print('Send feedback fail...')


class FeedbackSend(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(300.0):#3600
            send_feedback()
            

def loop60(x):
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
    
    net = True
    while net:
        if urllib.request.urlopen('http://google.com'):
            net = False
    
    try: 
        url = 'http://128.199.247.96:3000/api/music/getmusicloop/'+getserial()
        #url = 'http://128.199.247.96:3000/api/music/getmusicloop/10000000588a85c2'
        r = requests.get(url,allow_redirects=True)
       # print('playlistresq:'+r.text)
        with open("music.json", "w") as output:
            json.dump(r.json(), output)

        with open('music.json') as f:
            r_off = json.load(f)

        r_data = r_off['data']
        r_download = r_off['download']
        r_startDate = r_off['startDate']
        r_endDate = r_off['endDate']
        r_volume = r_off['volume']
        volume = alsaaudio.Mixer()
        current_volume = volume.getvolume()
        volume.setvolume(int(r_volume))
        print('volume =', current_volume)
    except:
        with open('music.json') as f:
            r_off = json.load(f)
        # print("load playlist from json without internet")##
        
    r_data = r_off['data']
    r_download = r_off['download']
    r_startDate = r_off['startDate']
    r_endDate = r_off['endDate']

    start_date= datetime.strptime(r_startDate,'%Y-%m-%d')
    end_date= datetime.strptime(r_endDate,'%Y-%m-%d')
    date_interval = end_date - start_date
    date_list = []

    for single_date in (start_date + timedelta(n) for n in range(date_interval.days+1)):
        date_list.append(single_date.strftime('%Y-%m-%d'))

    delete_music()
    download_music(r_download)

    stopFlag = threading.Event()
    request_thread = RequestThread(stopFlag)
    request_thread.start()

    break_thread = BreakChange(stopFlag)
    feedback_thread = FeedbackSend(stopFlag)
    feedback_thread.start()

    music_list=[]
    b = 0

    time_now = datetime.now()
    s_hour = int(time_now.strftime('%H'))
    s_mins = time_now.strftime('%M')
    s_date = time_now.strftime("%d/%m/%Y, %H:%M:%S")
    
    b_interval = loop60(int(s_mins))

    if b_interval[2] == True:
        s_hour = s_hour + 1
        start_break = (6*s_hour)+b_interval[0]
    else:
        start_break = (6*s_hour)+b_interval[0]

    if 'break'+str(start_break+b) == 'break145':
        start_break = 1
        for l in r_data['break'+str(start_break+b)]:
            music_list.append(l['sound'])
    else:
        for m in r_data['break'+str(start_break+b)]:
            music_list.append(m['sound'])

    #print('-----------')##
    #print('break'+str(start_break))
    #print(music_list)##
    music_finish = {'break'+str(start_break+b):[]}
    music_finish['time'+str(start_break+b)] = []
    #print('-----------')##

    music_finish['break'+str(start_break+b)].append(music_list[0])
    pygame.mixer.music.load("playlist/" + music_list.pop(0))
    music_finish['break'+str(start_break+b)].append(music_list[0])
    pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    
    waiting = True
    while waiting:
        time.sleep(0.5)
        tsm = int(datetime.now().strftime('%M'))
        tss = int(datetime.now().strftime('%S'))
        for i in date_list:
            if tss == 0 and tsm%10 == 0 and i == time_now.strftime('%Y-%m-%d'):
                waiting = False
                break
            
    pygame.mixer.music.play()
    music_finish['time'+str(start_break+b)].append(datetime.now().strftime("%H:%M:%S"))
    break_thread.start()

    while True:
        time.sleep(1)
        if count == 1:
            pygame.mixer.music.stop()
            b = b + 1
            music_list = []
            #music_finish['break'+str(start_break+b)] = []

            
            if 'break'+str(start_break+b) == 'break145':
                start_break=1
                b=0
                for k in r_data['break'+str(start_break+b)]:
                    music_list.append(k['sound'])    
            else:
                for j in r_data['break'+str(start_break+b)]:
                    music_list.append(j['sound'])
                    
            music_finish['break'+str(start_break+b)] = []
            music_finish['time'+str(start_break+b)] = []

            #print('-----------')##
            #print('-----------')##
            #print('break'+str(start_break+b))##
            #print(music_list)##

            music_finish['break'+str(start_break+b)].append(music_list[0])
            pygame.mixer.music.load("playlist/" + music_list.pop(0))
            #music_finish['break'+str(start_break+b)].append(music_list[0])
            #pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
    
            pygame.mixer.music.play()
            count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                music_finish['time'+str(start_break+b)].append(datetime.now().strftime("%H:%M:%S"))
                if len ( music_list ) > 0:
                    music_finish['break'+str(start_break+b)].append(music_list[0])
                    pygame.mixer.music.queue("playlist/" + music_list.pop(0))
                    
                    #print('-----------')##
                    #print('-----------')##
                    #print(music_finish)##
