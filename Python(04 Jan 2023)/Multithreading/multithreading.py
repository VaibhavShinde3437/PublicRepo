# import threading

# print(threading.current_thread())
# print(threading.current_thread().ident)
# print(threading.current_thread().is_alive())

# ========================================================================================================================================================

from threading import Thread, active_count
from time import sleep

# def display():
#     for i in range(4):
#         print("* " * i)

# t1 = Thread(target=display)
# t1.start()

# def display(n, msg="1 "):
#     for i in range(n):      # t1 thread
#         print(msg * i)

# t1 = Thread(target=display, kwargs={'n':10,'msg':"a "})
# t1.start()

# for _ in range(10):
#     print("Hello ")    # Main thread

# =======================================================================================================================================================

# class Sample:
#     def display(self, n, msg):
#         for i in range(n):
#             print(msg * i)

# s = Sample()

# t1 = Thread(target=s.display(10, "* "))
# t1.start()

# ======================================================================================================================================================

# class Sample:
#     @classmethod
#     def display(self, n, msg):
#         for i in range(n):
#             print(msg * i)

# t1 = Thread(target=Sample.display(10, "1 "))
# t1.start()

# =====================================================================================================================================================

# class Sample:
#     @staticmethod
#     def display(n, msg):
#         for i in range(n):
#             print(msg * i)

# t1 = Thread(target=Sample.display(10, "1 "))
# t1.start()
#  ====================================================================================================================================================

# l = ["Vaibhav", "Ujwal", "Rasik", "Arun", "Tarun"]
# class MyThread(Thread):
#     def __init__(self,val):
#         self.val = val
#         Thread.__init__(self)
#     def run(self):
#         if self.val:
#             print("Hello")
#         for name in l:
#             print(name)

# t1 = MyThread(False)
# t1.start()
# print(t1.ident)

# =====================================================================================================================================================

# def display(n):
#     for i in range(n):
#         print(i * "1 ")

# def show(n):
#     for i in range(n):
#         print(i * "2 ")

# t1 = Thread(target=display, args=(5,))
# t2 = Thread(target=show, args=(5,))

# t1.start()
# print("Active Thread :", active_count())
# t2.start()

# t1.name = "Hehe" 
# t2.name = "Haha"
# print(t1.name)
# print(t2.name)

# print(t1.ident)
# print(t1.native_id)

# ========================================================================================================================================================

# def upload():
#     print("Uploading a video")
#     sleep(2)
#     print("Video uploaded")
# def notification():
#     print("A notification will send to the user")

# t1 = Thread(target=upload)
# t2 = Thread(target=notification)

# t1.start()
# t1.join()
# t2.start()
# t2.join()

# for _ in range(5):
#     print("Hello")

# =====================================================================================================================================================

class Sample():
    def __init__(self):
        self.n = 100

    def add_sub(self, num):
        self.n = self.n + num
        self.n = self.n - num
        print("Add_Sub :", self.n)
        
        


t1 = Thread(target=Sample().add_sub, args=(10,))
t2 = Thread(target=Sample().add_sub, args=(20,))

t1.start()
t2.start()
