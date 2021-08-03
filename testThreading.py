from threading import Thread
import time
x=0

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            time.sleep(5.0)
            x+1
            return

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            time.sleep(1.0)
            print (x)


myClassA()
myClassB()
while True:
    pass
