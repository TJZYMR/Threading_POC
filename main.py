from threading import Thread,current_thread

# def disp(a,b):
#     print("Thread Running",a,b)
#
# for i in range(5):
#     t=Thread(target=disp,args=(10,20))
#     t.start()
def disp():
    print("Default Child Thread name:",current_thread().name)
    current_thread().name="Doc Thread"
    print("New Child Thread name:",current_thread().name)

t=Thread(target=disp,name="New name")
# t1=Thread(target=disp)
# t.name="Tatva Thread"
t.start()
# t1.start()

print("default Main Thread name:", current_thread().name)
# current_thread().name="tatva tuts"
# print("New Main Thread name:", current_thread().name)