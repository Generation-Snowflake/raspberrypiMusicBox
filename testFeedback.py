import requests
from datetime import datetime
import speedtest
#for check space 
import psutil

class speedTest:
    def speedTest():
        now = datetime.now()
        print(now)
        st = speedtest.Speedtest()
        netSpeed = st.download()

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


now = datetime.now()


# print(now)
# st = speedtest.Speedtest()
# netSpeed = st.download()
# print(netSpeed)

# url = 'https://api.dv8automate.com/api/player/box/feedback'
# myobj = {
#     'serialNumber':'10000000ce768306',
#     'freeSpace':'55',
#     'statusBox': 'offline',
#     'speedNet':spdTest,
#     'startPlayTime':now,
#     'currentVolume':40
#     }

# x = requests.post(url, data = myobj)

#print(x.text)



# path = '/'
# bytes_avail = psutil.disk_usage(path).free
# gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
# print("freespace = " + str(gigabytes_avail))