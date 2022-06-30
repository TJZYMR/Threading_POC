from threading import current_thread, Thread


# mt = current_thread()
# print(mt.name)
# print(mt.daemon)  # will return False which means its non-daemon thread
# if parent is daemon then child will be daemon thread as well
def disp():
    print("Disp Dunction")
    t2 = Thread(target=show)
    print("T2:", t2.daemon)


def show():
    print("Show Function")


mt = current_thread()
print(mt.name)
print("MT:", mt.daemon)
t1 = Thread(target=disp)
print("T1:", t1.daemon)
t1.daemon = True
print("T1:", t1.daemon)
t1.start()
t1.join()
print("Main Thread")
