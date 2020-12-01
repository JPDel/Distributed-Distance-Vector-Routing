import network_init
import node


def dvr_alg(r_node, adj_mat):
    init_find_neighbors(r_node, adj_mat)
    mark_untouchable_rows(r_node)
    print(r_node.dvr_matrix)
    return


# Used to find a nodes immediate neighbors during initialization
def init_find_neighbors(r_node, adj_mat):
    row_num = r_node.num - 1
    row = adj_mat[row_num]

    for i in range(0, 5):
        if row[i] != '0':
            # Casts the values from adj_matrix as integers because they're strings initially
            r_node.dvr_matrix[i][i] = int(row[i])

    return


def mark_untouchable_rows(r_node):
    row_num = r_node.num - 1

    for i in range(0, 5):
        r_node.dvr_matrix[row_num][i] = 999
        r_node.dvr_matrix[i][row_num] = 999

    return


def broadcast():
    return


# Calls the node classes' update function
def update(r_node):
    r_node.update()
    return


# Checks is a new shortest path was found during an update of the matrix
# Returns true if a nsp was found, false otherwise.
def check_for_nsp():
    return
