
def dvr_alg(r_node, adj_mat):
    init_find_neighbors(r_node, adj_mat)
    mark_untouchable_rows(r_node)
    broadcast(r_node)

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


# "Untouchable" rows are the rows in the DVR matrix that should not contain path values in them.
# These are all set to an integer value of '999' as specified in the instructions
def mark_untouchable_rows(r_node):
    row_num = r_node.num - 1

    for i in range(0, 5):
        r_node.dvr_matrix[row_num][i] = 999
        r_node.dvr_matrix[i][row_num] = 999

    return


def broadcast(r_node):
    #updated_rows = None

    # For testing:
    updated_rows = [None, [999, 2, 0, 0, 0], None, None, [999, 0, 0, 0, 1]]

    # TODO: Write func to select which rows to broadcast
    # updated_rows = select_bc_rows(r_node)
    # TODO: and insert them in to 'updated_rows' in their corresponding index

    form_bc_string(updated_rows, r_node.num)
    # For testing: print(form_bc_string(updated_rows, r_node.num))

    return


def select_bc_rows(r_node):
    ret_rows = [None, None, None, None, None]
    cur_dvr = r_node.dvr_matrix
    prev_dvr = r_node.prev_dvr_matrix

    for i in range(0, 5):
        if cur_dvr[i] != prev_dvr[i]:  # If a change occurred in this row during the last update

            for j in range(0, 5):  # Find that difference and compare to see if
                                   # the diff resulted in a new shortest path
                if cur_dvr[i][j] != prev_dvr[i][j]:
                    return

    return ret_rows


# Assembles the string of data that will be broadcast through TCP connection
# This is meant to be called within broadcast()
# Parameters: rows - An array of rows from the dvr that the node will broadcast
#             node_num - The number of the node
#
# Return: Returns a string of format:
#          "[node#] [DVR row#] [data1], [data2], ... ,[data5], [DVR row#], [data1], ... ,[data5]"
def form_bc_string(rows, node_num):
    ret_string = str(node_num) + " "
    for i in range(0, 5):  # Checks the array for which rows need to be broadcast
        if rows[i] is not None:
            row_string = str(i) + " "
            for j in range(0, 5): # Inserts the selected rows' values in to the return string
                row_string = row_string + str(rows[i][j]) + " "

            ret_string = ret_string + row_string

    return ret_string


# Calls the update function belonging to the node object
def update(r_node):

    r_node.update()
    return


# Checks is a new shortest path was found during an update of the matrix
# Returns true if a nsp was found, false otherwise.
def check_for_nsp():
    return
