class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_row = [False]*len(matrix)
        zeroes_col = [False]*len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes_row[i] = True
                    zeroes_col[j] = True
                    
                    
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zeroes_row[i] == True or zeroes_col[j] == True:
                    matrix[i][j] = 0
                    
        return matrix