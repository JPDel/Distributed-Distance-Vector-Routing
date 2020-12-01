import network_init
import node

def dvr_alg(node):
    init_find_neighbors(node)
    mark_untouchable_rows(node)
    print(node.dvr_matrix)
    return


# Used to find a nodes immediate neighbors during initialization
def init_find_neighbors(node):
    row_num = node.num - 1
    row = network_init.adj_matrix[row_num]

    for i in range(0, 4):
        if row[i] != 0:
            node.dvr_matrix[i][i] = row[i]


def mark_untouchable_rows(node):
    row_num = node.num - 1

    for i in range(0, 4):
        node.dvr_matrix[row_num][i] = 999
        node.dvr_matrix[i][row_num] = 999

    return


def broadcast():
    return


# Calls the node classes' update function
def update(node):
    node.update()
    return


# Checks is a new short path was found during an update of the matrix
# Returns true if a nsp was found, false otherwise.
def check_for_nsp():
    return
