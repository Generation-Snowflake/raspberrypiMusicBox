import multiprocessing
import time

def countdown(name, delay, count):
    while True:
      time.sleep(delay)
      print (f'{name, time.ctime(time.time()), count}')
      count -= 1
      
class newProcess(multiprocessing.Process):
    def __init__(self, name, count):
        multiprocessing.Process.__init__(self)
        self.name = name
        self.count = count
    def run(self):
        print("Starting: " + self.name + "\n")
        countdown(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")
        
class nextProcess(multiprocessing.Process):
    def __init__(self, name, count):
        multiprocessing.Process.__init__(self)
        self.name = name
        self.count = count
    def run(self):
        print("Starting: " + self.name + "\n")
        countdown(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")
      
t = newProcess("newProcess 1", 50)
t2 = nextProcess("nextProcess 2", 50)
t.start()
t2.start()
c = 0
while c < 50:
    c = c+1
    print("nine")
#t.join()
print("Done")  
