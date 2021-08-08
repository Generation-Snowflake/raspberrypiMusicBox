import requests
from datetime import datetime
import speedtest
#for check space 
import psutil
import threading

test_feedback = 0
spdT = 0
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


class NineThread(threading.Thread):
	def __init__(self,event):
		threading.Thread.__init__(self)
		self.stopped = event
	
	def run(self):
		global test_feedback
		while not self.stopped.wait(20.0):
                        path = '/'
			bytes_avail = psutil.disk_usage(path).free
			gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
			print("freespace = " + str(gigabytes_avail))

			url = 'https://api.dv8automate.com/api/player/box/feedback'
			myobj = {
				'serialNumber':'10000000ce768306',
				'freeSpace': str(gigabytes_avail),
				'statusBox':'online',
				'speedNet':spdT,
				'startPlayTime':test_feedback,
				'currentVolume':'0'
				}

			x = requests.post(url,data = myobj)
			print(x.text)


class speedTest(threading.Thread):
	def __init__(self,event):
		threading.Thread.__init__(self)
		self.stopped = event
	def run(self):
		global test_feedback
		while not self.stopped.wait(30.0):
                        path = '/'
			bytes_avail = psutil.disk_usage(path).free
			gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
			print("freespace = " + str(gigabytes_avail))

			st = speedtest.Speedtest()
			spdT = st.download()

			url = 'https://api.dv8automate.com/api/player/box/feedback'
			myobj = {
				'serialNumber':'10000000ce768306',
				'freeSpace': str(gigabytes_avail),
				'statusBox':'online',
				'speedNet':spdT,
				'startPlayTime':test_feedback,
				'currentVolume':'0'
				}

			x = requests.post(url,data = myobj)
			print(x.text)
			test_feedback+=1
		



if __name__ == "__main__":

	stopFlag = threading.Event()
	thread = NineThread(stopFlag)
	thread.start()


	stopFlag2 = threading.Event()
	thread2 = speedtest(stopFlag2)
	thread2.start()
#now = datetime.now()

#now = datetime.now()
#print(now)
#st = speedtest.Speedtest()
#spdTest = st.download()

#path = '/'
#bytes_avail = psutil.disk_usage(path).free
#gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
#print("freespace = " + str(gigabytes_avail))


#print(now)
#st = speedtest.Speedtest()
#netSpeed = st.download()
#print(netSpeed)

#print(getserial())

#url = 'https://api.dv8automate.com/api/player/box/feedback'
#myobj = {
#     'serialNumber':("10000000ce768306"),
#     'freeSpace':str(gigabytes_avail),
#     'statusBox': 'offline',
#     'speedNet':spdTest,
#     'startPlayTime':now,
#     'currentVolume':40
#     }

#x = requests.post(url, data = myobj)

#print(x.text)



