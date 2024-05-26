import socket
import threading
from queue import Queue

# Defining variables
open_ports = []
thread_list = []
# The queue is needed to ensure that multiple threads only scan ports that haven't been scanned
# This makes it more efficient as scanned ports are 
queue = Queue()


def port_scan(port):
    # Checking if the port is open or closed
    try:
        # Creating a new socket and trying to connect to the ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def fill_queue(port_list):
    # Fill the queue with ports from the port list
    for port in port_list:
        queue.put(port)

def scanner():
    # Check if the queue is empty
    while not queue.empty():
        port = queue.get()
        # Do a port scan and print only the ports that are open
        if port_scan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

# Gathering input for IP address, starting and ending port range to scan
target = input('Enter IP address to scan: ')
start = int(input('Enter starting port range: '))
end = int(input('Enter ending port range: '))
# Initialize port list
port_list = range(start, end)
fill_queue(port_list)

# Threading the port scanner to run multiple processes and improve speed 
for t in range(100):
    thread = threading.Thread(target=scanner)
    thread_list.append(thread)

# Starting the threads in the thread list
for thread in thread_list:
    thread.start()

# Adding the threads in the thread list
for thread in thread_list:
    thread.join()

if len(open_ports) != 0:
    print("The open ports are:", open_ports)
else:
    print("There are no open ports")