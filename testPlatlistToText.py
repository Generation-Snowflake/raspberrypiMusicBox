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



if __name__ == "__main__":

    url = 'http://128.199.247.96:3000/api/music/getmusicloop'
    r = requests.get(url,allow_redirects=True)

    with open("music.json", "w") as output:
        json.dump(r.json(), output)

    print("--- %s seconds ---" % (time.time() - start_time)) #show time