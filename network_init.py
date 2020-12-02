import threading  # Used for multithreading
import time
import node
import dvr_alg
from socket import *

in_file = open("network.txt", "r")

adj_matrix = []
sockets = [12001, 12002, 12003, 12004, 12005]
significantInfo = True
currentSocket = None

currentLock = threading.Lock()  # A helper synchronization primitive for currentThread
currentThread = threading.Semaphore(value=1)  # A semaphore that determines which thread is actively sending information
readyToReceive = threading.Semaphore(
    value=4)  # A semaphore that determines which threads still need to share their rows on the current iteration of the protocol


def network_init():
    lines = in_file.readlines()
    if len(lines) == 0:  # I don't know why but an exception gets raised if this isn't here
        return
    threads = []
    currentThread.acquire()
    for i in range(0, 5):
        line = lines[i].split()
        adj_matrix.append(line)
        thread = threading.Thread(target=create_node, args=(i, adj_matrix[i]))
        threads.append(thread)
        thread.start()
        # currentThread.release()
        # n1 = node.node(1)
        # n2 = node.node(2)
        # n3 = node.node(3)
        # n4 = node.node(4)
        # n5 = node.node(5)

        # dvr_alg.dvr_alg(n1, adj_matrix)
        # dvr_alg.dvr_alg(n2, adj_matrix)
        # dvr_alg.dvr_alg(n3, adj_matrix)
        # dvr_alg.dvr_alg(n4, adj_matrix)
        # dvr_alg.dvr_alg(n5, adj_matrix)

        # Node creation should be handled in create_node()
    currentThread.release()  # Should be released when the server goes online
    while (significantInfo):

    return


# Each master thread will run this seperately
def create_node(nodeNum, matrixLine):
    threadNode = node.node(nodeNum, matrixLine)
    mySocket = sockets[nodeNum]
    needsToSend = True  # Determines if this node still needs to send this round

    while (significantInfo):
        if (needsToSend and currentThread.acquire(blocking=False)):
            needsToSend = False
            # You are the currently broadcasting thread
            while (not readyToReceive.acquire(blocking=False)):
                readyToReceive.release()

            # All other threads are ready to recieve your info, send it
            currentSocket = sockets[nodeNum]
            serverName = 'localhost'
            serverPort = 12000
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))
            clientSocket.send(dvr_alg.broacast_string(threadNode).encode())
            currentThread.release()
        else:
            readyToReceive.acquire()
            dataString = clientSocket.recv(1024)
            threadNode.update(dataString)
            readyToReceive.release()

    clientSocket.close()
    print("thread " + str(nodeNum))


# This is intended only to count how many nodes provided by any given text file
def count_nodes():
    string = in_file.readline()
    list = string.split()
    in_file.seek(0, 0)  # Resets read head on the file back to the beginning
    return len(list)


if __name__ == '__main__':
    network_init()

network_init()