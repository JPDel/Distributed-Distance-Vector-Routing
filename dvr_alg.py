def dvr_alg(r_node, adj_mat):
    init_find_neighbors(r_node, adj_mat)
    mark_inf_values(r_node)
    #str = "2 1 999 999 999 999 3 999 999 5 999 999"
    #r_node.update(str)
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
            r_node.neighbors.append(i)

    return


# Sets all values that should be initially infinity as such.
# These are all set to an integer value of '999' as specified in the instructions
def mark_inf_values(r_node):
    row_num = r_node.num - 1

    for i in range(0, 5):

        r_node.dvr_matrix[row_num][i] = 999
        for j in range(0, 5):
            if (j != i) and (r_node.dvr_matrix[row_num][j] == 0):
                r_node.dvr_matrix[row_num][j] = 999

        r_node.dvr_matrix[i][row_num] = 999
        for j in range(0, 5):
            if r_node.dvr_matrix[i][j] == 0:
                r_node.dvr_matrix[i][j] = 999

    # Marks a node's distance to itself as 0
    # r_node.dvr_matrix[row_num][row_num] = 0

    return


# This function broadcasts any new shortest path estimates
#
# Return: - Upon broadcasting a new DVR estimate, this function will return True
#         - If no shortest path was found for broadcasting, then False is returned
def broadcast_string(r_node):
    # For testing: updated_rows = [None, [999, 2, 0, 0, 0], None, None, [999, 0, 0, 0, 1]]
    # no_broadcast_required = [None, None, None, None, None]
    updated_rows = select_bc_rows(r_node)

    # For testing: print("Broadcasting rows: " + str(updated_rows))
    # For testing:
    return form_bc_string(updated_rows, r_node.num)



# Checks the node's DVR matrix for rows with any new shortest paths found during the last update
# If any such rows are found they are placed in an array of rows and returned
def select_bc_rows(r_node):
    ret_rows = [None, None, None, None, None]
    cur_dvr = r_node.dvr_matrix
    prev_dvr = r_node.prev_dvr_matrix

    for i in range(0, 5):
        if cur_dvr[i] != prev_dvr[i]:  # If a change occurred in this row during the last update

            for j in range(0, 5):  # Find that change
                if cur_dvr[i][j] != prev_dvr[i][j]:

                    shorter_path_found = True
                    for k in range(0, 5):  # And compare that new value to the rest of the values in that row

                        if (j != k) and (cur_dvr[i][k] != 0) and (cur_dvr[i][k] != 999) and \
                                (cur_dvr[i][j] >= cur_dvr[i][k]):
                            # If the new value does not provide a new shortest path
                            shorter_path_found = False  # Do not broadcast that row

                    if shorter_path_found:  # Adds that row to the array about to be broadcast
                                            # if a shorter path is found

                        ret_rows[i] = cur_dvr[i]
    return ret_rows


# Assembles the string of data that will be broadcast through TCP connection
# This is meant to be called within broadcast()
# Parameters: rows - An array of rows from the dvr matrix that the node will broadcast
#             node_num - The number of the node
#
# Return: Returns a string of format:
#          "[node#] [DVR row#] [data1], [data2], ... ,[data5], [\n],[DVR row#], [data1], ... ,[data5]"
def form_bc_string(rows, node_num):
    ret_string = str(node_num) + " " + "\n"
    for i in range(0, 5):  # Checks the array for which rows need to be broadcast
        if rows[i] is not None:
            row_string = str(i) + " " + "\n"
            for j in range(0, 5):  # Inserts the selected rows' values in to the return string
                row_string = row_string + str(rows[i][j]) + " "

            ret_string = ret_string + row_string + "\n"

    return ret_string


# Calls the update function belonging to the node object
def update(r_node):
    r_node.update()
    # TODO: Still needs to be implemented
    return
