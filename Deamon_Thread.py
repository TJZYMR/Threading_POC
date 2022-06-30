from threading import Thread

def disp():
    print("Daemon Thread")

t1=Thread(target=disp)
t1.daemon=True
t1.start()
print(t1.daemon)