from threading import *

class Mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("child Thread Constructor",a)
    def run(self):
        print("child Thread Run")
t=Mythread(10)
t.start()
print("Main Thread")