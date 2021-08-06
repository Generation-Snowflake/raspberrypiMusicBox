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


if __name__ == "__main__":

    # stopFlag = threading.Event()
    # thread2 = ClockThread(stopFlag)
    # thread2.start()
    #print('ssss')
    #timee = my_queue.get()
    #print(timee)

    music_list=[]
    music_list_all=[]
    music_list3=[]##
    music_list4=[]##
    music_list5=[]##
    music_list6=[]##

    with open('music.json') as f:
        data = json.load(f)

    print(data['data'])


    # for i in range (loop_count,24):
    #     if str(i) == str(loop_count):
    #         for j in range(int(b_interval[0]),7):
    #             for l in r_test['loop'+str(loop_count)]['break'+str(j)]:
    #                 music_list.append(l['sound']) 
    #     else:
    #         for k in r_test['loop'+str(i)]:
    #             for m in r_test['loop'+str(i)][str(k)]:
    #                 music_list.append(m['sound'])
                
    # print(music_list)


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

    #         print(music_list)

    #         pygame.mixer.music.load("playlist/" + music_list.pop(0))
    #         #pygame.mixer.music.queue ("playlist/" + music_list.pop(0))
    #         pygame.mixer.music.set_endevent(pygame.USEREVENT)
    #         pygame.mixer.music.play()
    #         print("Play again")
    #         a_trg = b_trg
    #     for event in pygame.event.get():

    #         if event.type == pygame.USEREVENT:    
    #             if len ( music_list ) > 0:
    #                 pygame.mixer.music.queue("playlist/" + music_list.pop(0))

    #            # print('aa')
    print("--- %s seconds ---" % (time.time() - start_time)) #show time