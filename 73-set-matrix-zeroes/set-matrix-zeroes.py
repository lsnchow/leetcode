class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # create an array to store all the values
        r = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for x in range(n):
                if matrix[i][x] == 0:
                    # appending: row, column
                    r.append([i,x])
        
        for pairs in r:
            # a is row
            a = pairs[0]
            # b is column
            b = pairs[1]
            # vertical - a, i:
            for i in range(0,n):
                matrix[a][i] = 0
            for i in range(0,m):
                matrix[i][b] = 0


        