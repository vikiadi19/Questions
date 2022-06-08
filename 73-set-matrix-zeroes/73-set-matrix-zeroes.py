class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero, colZero = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowZero.add(i)
                    colZero.add(j)
                    
        for i in rowZero:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
                
        for j in colZero:
            for i in range(len(matrix)):
                matrix[i][j] = 0
                
        return matrix
                