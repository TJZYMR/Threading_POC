from threading import *
import time
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l=RLock()
        # print(self.l)
    def reserve(self, need_seat):
        # self.l.acquire(blocking=True,timeout=2)
        self.l.acquire()
        self.l.acquire()

        # print(self.l)
        print('Available Seats:', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allowed for {name}')
            self.available_seat -= need_seat
            # time.sleep(3)
        else:
            print('Sorry! All seats has alloted')
        self.l.release()
        self.l.release()

f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Soname')
t3 = Thread(target=f.reserve, args=(2,), name='raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")