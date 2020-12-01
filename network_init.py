import threading  # Used for multithreading
import socket
import node
import dvr_alg

in_file = open("network.txt", "r")

adj_matrix = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]


def network_init():
    lines = in_file.readlines()
    
    for i in range(0, 5):
        line = lines[i].split()
        adj_matrix.append(line)

    #print(adj_matrix[0][0])
    n1 = node.node(1)
    dvr_alg.dvr_alg(n1)

    return


# This is intended only to count how many nodes provided by any given text file
def count_nodes():
    string = in_file.readline()
    list = string.split()
    in_file.seek(0, 0)  # Resets read head on the file back to the beginning
    return len(list)


if __name__ == '__main__':
    network_init()