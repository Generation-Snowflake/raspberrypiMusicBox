#!/usr/bin/python3
import alsaaudio
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

scan = alsaaudio.cards()
#print("cards:", scan)
#for card in scan:
#    scanMixers = alsaaudio.mixers(scan.index(card))
#    print("mixers:", scanMixers)

for mixername in alsaaudio.mixers():
    print('mixername='+mixername)

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

        while not self.stopped.wait(60.0):
            #try:
                #url = 'http://128.199.247.96:3000/api/music/getmusicloop/'+getserial()
                url = 'http://128.199.247.96:3000/api/music/getmusicloop/10000000588a85c2'
                r = requests.get(url,allow_redirects=True)
                # print('playlistresq:'+r.text)
                with open("musicTest.json", "w") as output:
                    json.dump(r.json(), output)

                with open('musicTest.json') as f:
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
            #except:
                print("Request fail...")

# m = alsaaudio.Mixer('Master')
# current_volume = m.getvolume()
# print(current_volume)
# m.setvolume(100)
# print(current_volume)

if __name__ == "__main__":

    stopFlag = threading.Event()
    request_thread = RequestThread(stopFlag)
    request_thread.start()
