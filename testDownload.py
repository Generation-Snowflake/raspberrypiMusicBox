import requests
import json
import time
from datetime import datetime
import speedtest
#for check space 
import psutil
from tqdm import tqdm
import os

# url = 'http://128.199.247.96:3000/api/music/getmusicloop'  #playlist URL http://128.199.247.96:3000/api/music
# r = requests.get(url,allow_redirects=True)

#r = str(r.content).split(",")  # split each song to list
# python_obj = json.loads(r.json())

# dicTest = r.json()["loop1"]

# for i in len(dicTest["break1"]):
#     print(dicTest["break1"][i])

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



while True:
    time.sleep(1)
    try:
        url = 'http://128.199.247.96:3000/api/music/getmusicloop'  #playlist URL http://128.199.247.96:3000/api/music
        r = requests.get(url,allow_redirects=True)
    except ValueError:
        print(ValueError)


    # if str(r.json()['download']) == "True":
    #     if os.path.isdir('playlist') == False:
    #         os.mkdir('playlist')

    #     url = 'http://128.199.247.96:3000/api/music'
    #     playlist = requests.get(url,allow_redirects=True)
    #     playlist = str(playlist.content).split(',')

    #     playlist_lst = str(playlist).split('"')
    #     playlist_lst.pop(playlist_lst.index("['b\\'["))
    #     playlist_lst.pop(playlist_lst.index("]\\'']"))

    #     for i,enum in enumerate(playlist_lst):
    #         if enum == "', '":
    #             playlist_lst.pop(i)

    #     for j in tqdm(range (0,len(playlist_lst))):
    #         music = playlist_lst[j].split('/')
    #         music_download = requests.get(playlist_lst[j],allow_redirects=True)
    #         open('playlist/'+music[-1],('wb')).write(music_download.content)

    #get free space 
    path = '/'
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    
    #get raspberry pi serial 
    serial = getserial() 

    #print(len(r.json()['loop1']['break1']/2))
    #print()
    # for i in len(int(r.json()['loop1']['break1']))/2:
    #     print(r.json()['loop1']['break1'][i])
    print(r.json()['loop1']['break1'][1])
    # print(r.json()['download'])
    # print(r.json()['command'])
    #print(len(r.json()['loop1']['break1']))
    print(str(r.json()))
    now = datetime.now()

    url = 'https://api.dv8automate.com/api/player/box/feedback'
    myobj = {
            'serialNumber':"10000000ce768306",
            'freeSpace':str(gigabytes_avail),
            'statusBox': 'offline',
            'speedNet':'spdTest',
            'startPlayTime':now,
            'currentVolume':40
            }

    x = requests.post(url, data = myobj)
    print(x.text)

# {"download":true,
# "loop1":{"break1":[{"sound":"01.Lotus_sVisa10(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"02.Lotus_sAutoInsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"2.SmartHeartชดฝนเกง15Sec.mp3","duration":"00:00.14"},
# {"sound":"3.MEOอยากกินMe-O15Sec.mp3","duration":"00:00.14"},
# {"sound":"4.Ducthmill_Yoghurt_1_15JUN(Radio).mp3","duration":"00:00.32"},
# {"sound":"5.Ducthmill_Delight_16_31MAY(Radio).mp3","duration":"00:00.30"},
# {"sound":"6.Trueyourevised.mp3","duration":"00:00.30"},
# {"sound":"7.RosdeeMhakKim.mp3","duration":"00:00.28"},
# {"sound":"8.FoodPandaShop.mp3","duration":"00:00.14"},
# {"sound":"9.Dnee_Concentrated30s(Remix).mp3","duration":"00:00.30"},
# {"sound":"03.Lotus_shealthinsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"04.Lotus_Clubcard(01-15Aug21).mp3","duration":"00:00.16"},
# {"sound":"05.Retail_Service_Hyper(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"06.ThematicMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.32"},
# {"sound":"07.SalmonMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.23"},
# {"sound":"08.RiceMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"09.EGGMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.19"},
# {"sound":"10.CageFreeEggMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"11.PorkMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"12.ซอสปรุงรสMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.20"},
# {"sound":"13.Lotusสินค้าราคามหาชนใหม่_ภาคกลาง(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"14.สินค้าราคามหาชนใหม่_ภาคใต้(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"15.สินค้าราคามหาชนใหม่_ภาคเหนือ(01-15Aug21).mp3","duration":"00:00.30"}],
# "command":"play",
# "break2":[{"sound":"16.สินค้าราคามหาชนใหม่_ภาคอีสาน(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"17.Lotus_Covid19(01-15Aug21).mp3","duration":"00:01.10"},
# {"sound":"18.dunnhumbymedia_2021(01-15Aug21).mp3","duration":"00:00.09"},
# {"sound":"Promotion_weekly_29JUL_4AUG_21(Radio).mp3","duration":"00:00.30"},
# {"sound":"(2.30)ขอโทษดาว-เอิ๊ตภัทรวี.mp3","duration":"00:02.30"},
# {"sound":"(2.30)คนที่ไม่ใช่-โอปวีร์คชภักดี.mp3","duration":"00:02.30"}],
# "break3":[{"sound":"05.Retail_Service_Hyper(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"06.ThematicMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.32"},
# {"sound":"07.SalmonMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.23"},
# {"sound":"08.RiceMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"09.EGGMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.19"},
# {"sound":"10.CageFreeEggMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"11.PorkMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"12.ซอสปรุงรสMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.20"},
# {"sound":"13.Lotusสินค้าราคามหาชนใหม่_ภาคกลาง(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"14.สินค้าราคามหาชนใหม่_ภาคใต้(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"15.สินค้าราคามหาชนใหม่_ภาคเหนือ(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"01.Lotus_sVisa10(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"02.Lotus_sAutoInsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"2.SmartHeartชดฝนเกง15Sec.mp3","duration":"00:00.14"},
# {"sound":"3.MEOอยากกินMe-O15Sec.mp3","duration":"00:00.14"},
# {"sound":"4.Ducthmill_Yoghurt_1_15JUN(Radio).mp3","duration":"00:00.32"},
# {"sound":"5.Ducthmill_Delight_16_31MAY(Radio).mp3","duration":"00:00.30"},
# {"sound":"6.Trueyourevised.mp3","duration":"00:00.30"},
# {"sound":"7.RosdeeMhakKim.mp3","duration":"00:00.28"},
# {"sound":"8.FoodPandaShop.mp3","duration":"00:00.14"},
# {"sound":"9.Dnee_Concentrated30s(Remix).mp3","duration":"00:00.30"},
# {"sound":"03.Lotus_shealthinsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"04.Lotus_Clubcard(01-15Aug21).mp3","duration":"00:00.16"}],
# "break4":[{"sound":"(2.30)คนที่แสนดี-Gee.mp3","duration":"00:02.30"},
# {"sound":"16.สินค้าราคามหาชนใหม่_ภาคอีสาน(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"17.Lotus_Covid19(01-15Aug21).mp3","duration":"00:01.10"},
# {"sound":"18.dunnhumbymedia_2021(01-15Aug21).mp3","duration":"00:00.09"},
# {"sound":"Promotion_weekly_29JUL_4AUG_21(Radio).mp3","duration":"00:00.30"},
# {"sound":"(2.30)คล้าย-NICE CNX.mp3","duration":"00:02.30"}],
# "break5":[{"sound":"15.สินค้าราคามหาชนใหม่_ภาคเหนือ(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"01.Lotus_sVisa10(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"02.Lotus_sAutoInsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"2.SmartHeartชดฝนเกง15Sec.mp3","duration":"00:00.14"},
# {"sound":"3.MEOอยากกินMe-O15Sec.mp3","duration":"00:00.14"},
# {"sound":"4.Ducthmill_Yoghurt_1_15JUN(Radio).mp3","duration":"00:00.32"},
# {"sound":"5.Ducthmill_Delight_16_31MAY(Radio).mp3","duration":"00:00.30"},
# {"sound":"6.Trueyourevised.mp3","duration":"00:00.30"},
# {"sound":"7.RosdeeMhakKim.mp3","duration":"00:00.28"},
# {"sound":"8. FoodPandaShop.mp3","duration":"00:00.14"},
# {"sound":"9.Dnee_Concentrated30s(Remix).mp3","duration":"00:00.30"},
# {"sound":"05.Retail_Service_Hyper(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"06.ThematicMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.32"},
# {"sound":"07.SalmonMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.23"},
# {"sound":"08.RiceMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"09.EGGMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.19"},
# {"sound":"10.CageFreeEggMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.27"},
# {"sound":"11.PorkMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.29"},
# {"sound":"12.ซอสปรุงรสMIXEDIT_master(01-15Aug21).mp3","duration":"00:00.20"},
# {"sound":"13.Lotusสินค้าราคามหาชนใหม่_ภาคกลาง(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"14.สินค้าราคามหาชนใหม่_ภาคใต้(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"03.Lotus_shealthinsurance(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"04.Lotus_Clubcard(01-15Aug21).mp3","duration":"00:00.16"}],
# "break6":[{"sound":"(2.30)ขอโทษ-บุรินทร์บุญวิสุทธิ์.mp3","duration":"00:02.30"},
# {"sound":"16.สินค้าราคามหาชนใหม่_ภาคอีสาน(01-15Aug21).mp3","duration":"00:00.30"},
# {"sound":"17.Lotus_Covid19(01-15Aug21).mp3","duration":"00:01.10"},{"sound":"18.dunnhumbymedia_2021(01-15Aug21).mp3","duration":"00:00.09"},{"sound":"Promotion_weekly_29JUL_4AUG_21(Radio).mp3","duration":"00:00.30"},{"sound":"(2.30)ความรักกำลังก่อตัว-นนท์ธนนท์.mp3","duration":"00:02.30"}]}}
