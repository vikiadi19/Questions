class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         rows, cols = len(matrix), len(matrix[0])
#         rowZero = False
#         for r in range(rows):
#             for c in range(cols):
#                 if matrix[r][c] == 0:
#                     if r>0:
#                         matrix[r][0] = 0
#                     else:
#                         rowZero = True
#                     matrix[0][c] = 0
                    
#         for r in range(1, rows):
#             for c in range(1, cols):
#                 if matrix[r][0] == 0 or matrix[0][c]==0:
#                     matrix[r][c] = 0
                    
#         if rowZero == True:
#             for c in range(cols):
#                 matrix[0][c] = 0
                
#         if matrix[0][0] == 0:
#             for r in range(rows):
#                 matrix[r][0] = 0
                
#         return matrix

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0