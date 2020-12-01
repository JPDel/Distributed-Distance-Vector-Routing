import threading #Used for multithreading
import time
import node
import dvr_alg
from socket import *

in_file = open("network.txt", "r")

adj_matrix = []
sockets = []

locker = threading.Lock()
semaphore = threading.Semaphore(value=1)
currentThread = threading.Condition() # A cv that determines which thread is currently running
needToShare = threading.Semaphore(value=5) # A semaphore that determines which threads still need to share their rows on the current iteration of the protocol

def network_init():
    lines = in_file.readlines()
    print(len(lines))
    threads = []
    for i in range(0,5):
        line = lines[i].split()
        adj_matrix.append(line)
        thread = threading.Thread(target=create_node, args=(i, adj_matrix[i]))
        threads.append(thread)
        thread.start()

        #n1 = node.node(1)
        #n2 = node.node(2)
        #n3 = node.node(3)
        #n4 = node.node(4)
        #n5 = node.node(5)

        #dvr_alg.dvr_alg(n1, adj_matrix)
        #dvr_alg.dvr_alg(n2, adj_matrix)
        #dvr_alg.dvr_alg(n3, adj_matrix)
        #dvr_alg.dvr_alg(n4, adj_matrix)
        #dvr_alg.dvr_alg(n5, adj_matrix)

        # Node creation should be handled in create_node()
    
    return

# Each master thread will run this seperately
def create_node(nodeNum, matrixLine):
    
    semaphore.acquire()

    print("Thread "+str(nodeNum)+" started\n")
    threadNode = node.node(nodeNum, matrixLine)

    semaphore.release()
    

# This is intended only to count how many nodes provided by any given text file
def count_nodes():
    string = in_file.readline()
    list = string.split()
    in_file.seek(0, 0)  # Resets read head on the file back to the beginning
    return len(list)

if __name__ == '__main__':
    network_init()

network_init()