import requests
from datetime import datetime
import speedtest
#for check space 
import psutil

# url = 'https://api.dv8automate.com/api/player/box/feedback' 
# r = requests.get(url,allow_redirects=True)

# print(r.content)
# # open('Sunkissed.mp3',('wb')).write(r.content)

now = datetime.now()
print(now)
#st = speedtest.Speedtest()
#netSpeed = st.download()
#print(netSpeed)

# url = 'https://api.dv8automate.com/api/player/box/feedback'
# myobj = {
#     'serialNumber':'10000000ce768306',
#     'freeSpace':'55',
#     'statusBox': 'offline',
#     'speedNet':netSpeed,
#     'startPlayTime':now,
#     'currentVolume':40
#     }

# x = requests.post(url, data = myobj)

# print(x.text)

# install package for speedtest 
# pip install speedtest-cli


path = '/'
bytes_avail = psutil.disk_usage(path).free
gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
print("freespace = " + str(gigabytes_avail))