import threading
import time

def thread_1():# move character
    while True:
        print("thread 1\n")
        time.sleep(2.0)

t1 = threading.Thread(target=thread_1)
t1.start()

temp = input("user input:")
print(temp)