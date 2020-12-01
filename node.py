class node:

    def __init__(self, num, matrix=None):

        self.matrix = matrix
        self.neighbors = []
        self.num = num  # a number from 1-5
        self.dvr_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # prev_dir_matrix is used to compare to dvr_matrix to check for new shortest paths
        self.prev_dvr_matrix = [[999, 999, 999, 999, 999], [999, 999, 999, 999, 999], [999, 999, 999, 999, 999],
                                [999, 999, 999, 999, 999], [999, 999, 999, 999, 999]]
        if matrix is None:
            self.matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def update(self, dataString):
        # data will come in the form of a string "nodeNum row dataPoint1 dataPoint2 dataPoint3 dataPoint4 dataPoint5"

        data = dataString.split(" ")

        nodeNum = int(data[0])
        row = int(data[1])
        datapoints = [int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])]

        # Update current node's matrix here
        
        # Update current node's matrix here
        lowest = None

        for i in range(0,5):
            if row == self.num or i == self.num: # Don't add any information about the current node to or from itself
                continue
            if datapoints[i] != 0: # If there's some meaningful information
                if lowest == None or lowest > datapoints[i]: # Find the lowest non-zero value
                    lowest = datapoints[i]

                    if self.matrix[row][nodeNum] == 0 and self.matrix[nodeNum][nodeNum] != 0: # If the previous value was 0, make it non-zero
                        self.matrix[row][nodeNum] = datapoints[i] + self.matrix[nodeNum][nodeNum]
                    elif self.matrix[row][nodeNum] != 0 and self.matrix[nodeNum][nodeNum] != 0:
                        if self.matrix[row][nodeNum] > datapoints[i] + self.matrix[nodeNum][nodeNum]: # If the previous value was higher than the current value, set it to the lower value
                            self.matrix[row][nodeNum] = datapoints[i] + self.matrix[nodeNum][nodeNum]
        
        # The above should work if the broadcasting node sends out it's row info to all other nodes, not just their neighbors


    def getData(self, row):
        returnString = str(self.num) + " " + row + " "

        for i in range(0, 5):
            returnString += self.matrix[row-1][i]
            if i < 4:
                returnString += " "
        
        return returnString