import socket
import threading

from queue import Queue

target = 'yourIp'

queue = Queue()
open_port = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_port.append(port)


# you can choose what range of your Ip you want to scan
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

# you can change how many thread you want ,the larger the number is ,the faster the scanning is
for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are :", open_port)
