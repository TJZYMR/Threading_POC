from threading import Thread,Event
from time import sleep
def light_switch():#for starting and stopping the green light
    sleep(3)
    e.set()#from here another function or thread will start executing unitl 5 secs and after that in the secon thread we show red light on.    print("Green Light On")
    sleep(5)
    print("Red Light On")
    e.clear()
def traffic():#for letting the traffic go saying that.
    e.wait()#here this thread will wait for the green light to be on.when set is eexecuting this thread will start executing.
    while e.is_set():
        print("You can go")
        sleep(0.5)
    print("Program done")
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()