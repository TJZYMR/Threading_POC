from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Run Method")
#
t=MyThread()
# print(t.name)
t.start()
t.join()
for i in range(5):
    print("Main Thread")

#mthods used=>Thread class,name,start,join