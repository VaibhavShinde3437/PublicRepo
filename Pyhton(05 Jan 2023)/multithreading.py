from threading import *
import threading
from time import sleep

# myLock = Lock()
# counter = 0
# def count(n):
#     myLock.acquire()
#     global counter
#     for i in range(10000000):
#         counter += 1
#     print(f"Thread {n}'s count is {counter}")
#     myLock.release()
    
       
        
# t1 = Thread(target=count, args=(1,))
# t2 = Thread(target=count, args=(2,))

# t1.start() 
# # t1.join()
# t2.start()
# t2.join()
# print(counter)

# =======================================================================================================================================================

# l = Lock()
# def hello(n):
#     print(f"Thread {n} before acquiring")
#     l.acquire()
#     print(f"Thread {n} locked")
#     l.release()
#     # print(f"Thread {n} after release")


# t1 = Thread(target=hello, args=(1,))
# t2 = Thread(target=hello, args=(2,))

# t1.start()
# # t1.join()
# t2.start()

# =======================================================================================================================================================
# l = Semaphore(3)

# def display(name):
#     l.acquire()
#     for _ in range(5):
#         print("Hello")
#         print(name)
#         sleep(2)
#     l.release()
 

# t1 = Thread(target=display, args=("Thread 1",))
# t2 = Thread(target=display, args=("Thread 2",))
# t3 = Thread(target=display, args=("Thread 3",))
# t4 = Thread(target=display, args=("Thread 4",))
# t5 = Thread(target=display, args=("Thread 5",))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# ====================================================================================================================================================================

# def custom_hook(args):
#     print("Everything about exception :")
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])

# def hello():
#     for _ in range(5):
#         sleep(3)
#         print("Hello" + 10)

# def display():
#     for _ in range(5):
#         print("Display")
#         sleep(1)
# threading.excepthook = custom_hook
# t1 = Thread(target=hello)
# t2 = Thread(target=display)

# t1.start()
# t2.start() 

# ============================================================================================================================================================

# e = Event()

# def task():
#     print("Game has started..")
#     sleep(3)
#     e.set()
#     sleep(3)

# def end():
#     e.wait()
#     if e.is_set():
#         print("Game session will be destroyed...")

# t1 = Thread(target=task)
# t2 = Thread(target=end)

# t1.start()
# t2.start()

# ============================================================================================================================================================

# e = Event()
# def lightSwitch():
#     while True:
#         print("Green")
#         e.set()
#         sleep(5)
#         print("Red")
#         e.clear()
#         sleep(5)
#         e.set()
        

# def msg():
#     e.wait()
#     while e.is_set():
#         print("You can go")
#         sleep(0.5)
#         e.wait()
        

# t1 = Thread(target=lightSwitch)
# t2 = Thread(target=msg)

# t1.start() 
# t2.start()

# ===========================================================================================================================================================


# def write():
#     con.acquire()
#     tem = [38,28,46,12,85,69,55]
#     with open("temp.txt", "a") as file:
#         for t in tem:
#             file.write(str(t)+"\n")
#     con.notify_all()
#     con.release()

# def max_temp():
#     con.acquire()
#     con.wait(timeout=0)
#     lines = []
#     with open("temp.txt", "r") as file:
#         for line in file:
#             lines.append(int(line))

#     ans = 0
#     for num in lines:
#         if ans <= num:
#             ans = num

#     print(ans)
#     # print(lines)
#     con.release()

# def avg_temp():
#     con.acquire()
#     con.wait(timeout=0)
#     lines = []
#     with open("temp.txt", "r") as file:
#         for line in file:
#             lines.append(int(line))
#     ans = 0;
#     for num in lines:
#         ans += num
#     print(ans/len(lines))
#     con.release()

# con = Condition()


# t1 = Thread(target=write)
# t2 = Thread(target=max_temp)
# t3 = Thread(target=avg_temp)


# t1.start()
# t2.start()
# t3.start()

# =========================================================================================================================================================

