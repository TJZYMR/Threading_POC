# two task using two tread

from threading import Thread

class Hotel:
    def __init__(self,t):
        self.t = t
    def food(self):
        for i in range(1,6):
            print(self.t,i)


h1=Hotel('Take Order from Table')
h2=Hotel('Serve Order to Table')
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
# t1.join()
t2.start()

#serving cannot be done before taking any order
#so this is called race conditioon
#if we were to do join then all the orders would be takem 