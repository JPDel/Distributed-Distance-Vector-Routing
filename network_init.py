import threading  # Used for multithreading
import socket


in_file = open("network.txt", "r")


# Note: I'll probably try to implement with a single thread before attempting with multithreading
def network_init():
    return


# This is intended only to count how many nodes provided by any given text file
def count_nodes():
    string = in_file.readline()
    list = string.split()
    in_file.seek(0, 0)  # Resets read head on the file back to the beginning
    return len(list)


if __name__ == '__main__':
    network_init()