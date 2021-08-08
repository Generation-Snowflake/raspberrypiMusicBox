from testThreading import send_feedback
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
c = 0


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


class BreakChange(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global c
        while not self.stopped.wait(10):
            c = 1
        return c
            # call a function


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

    pygame.init()
    pygame.mixer.init()
    # stopFlag = threading.Event()
    # thread2 = ClockThread(stopFlag)
    # thread2.start()
    #print('ssss')
    #timee = my_queue.get()
    #print(timee)
    stopFlag = threading.Event()
    break_thread = BreakChange(stopFlag)

    music_list=[]
    music_list_all=[]
    music_list3=[]##
    music_list4=[]##
    music_list5=[]##
    music_list6=[]##
    loop_count = 1

    with open('music.json') as f:
        r = json.load(f)

    r_test = r['data']
    d_test = r['download']
    sd_test = r['startDate']
    ed_test = r['endDate']

    print(d_test)##
    print('-----------')##
    print(sd_test)##
    print('-----------')##
    print(ed_test)##
    print('-----------')##

    time_now = datetime.now()
    s_hour = time_now.strftime('%H')
    s_mins = time_now.strftime('%M')

    b_interval = interval_loop60(int(s_mins))

    #------------------copy this---------------
    if b_interval[2] == True:
        loop_count = int(s_hour)+2
    elif int(s_hour) == 23:
        loop_count = 1
    else:
        loop_count = int(s_hour)+1
    #-------------------------------------------

    print('loop'+str(loop_count))
    print(('break'+b_interval[0]))##

    print('-----------')##

    for i in range (loop_count,24):
        if str(i) == str(loop_count):
            for j in range(int(b_interval[0]),7):
                for l in r_test['loop'+str(loop_count)]['break'+str(j)]:
                    music_list.append(l['sound'])
        else:
            for k in r_test['loop'+str(i)]:
                for m in r_test['loop'+str(i)][str(k)]:
                    music_list.append(m['sound'])

    #print(music_list)##

    pygame.mixer.music.load("playlist/" + music_list.pop(0))
    pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

   #pause.until(datetime(2021, 8, 7, (loop_count - 1), b_interval[1], 00))

    pygame.mixer.music.play()
    break_thread.start()######################################

    print("Play first")
    
    running = True
    while running:
        if c == 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
            c = 0

        for event in pygame.event.get():

            if event.type == pygame.USEREVENT:
                if len ( music_list ) > 0:
                    #-----------directory for pi--------------
                    #pygame.mixer.music.queue ("/home/pi/raspberrypiMusicBox/playlist/" + music_list.pop(0))

                    #-----------directory form pc--------------
                    pygame.mixer.music.queue("playlist/" + music_list.pop(0))

            # print('aa')
    print("--- %s seconds ---" % (time.time() - start_time)) #show time ##
