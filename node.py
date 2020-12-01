class node:

    def __init__(self, num, matrix=None):

        self.matrix = matrix
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


    def getData(self, row):
        returnString = str(self.num) + " " + row + " "

        for i in range(0, 5):
            returnString += self.matrix[row-1][i]
            if i < 4:
                returnString += " "
        
        return returnString