import threading


def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")


t1 = threading.Thread(target=sum, args=('thread_1', 5))
t2 = threading.Thread(target=sum, args=('thread_2', 5))

t1.start()
t2.start()

print("Main")

# Asynchronized program 
#synchronized -> youtube 0:00 -> 1:15  0:00 0:45 0:03  1:00 0:13
# list, buffer [image 1 image 15 imsage 100 image 3 ]