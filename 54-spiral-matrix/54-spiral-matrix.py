class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         i, j = 0, 0
#         visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
#         res = []
#         def trackPath(matrix, i, j, res):
#             if i >= 0 and j >= 0 and visited[i][j] == False and j < len(matrix[0]):
#                 visited[i][j] = True
#                 res.append(matrix[i][j])
#                 trackPath(matrix, i, j+1, res)
#             elif j == len(matrix[0]) and :
#                 visited[i][j] = True
#                 res.append(matrix[i][j])
#                 trackPath(matrix, i+1, j, res)
#             elif <condition>:
#                 visited[i][j] = True
#                 res.append(matrix[i][j])
#                 trackPath(matrix, i-1, j, res)
#             else:
#                 visited[i][j] = True
#                 res.append(matrix[i][j])
#                 trackPath(matrix, i, j-1, res)
            
#         return res

            top, bottom = 0, len(matrix)
            left, right = 0, len(matrix[0])
            res = []
            
            while left < right and top < bottom:
                #printing the top layer from left to right
                for i in range(left, right):
                    res.append(matrix[top][i])
                top += 1
                   
                #printing the vertical layer from top to bottom
                for i in range(top, bottom):
                    res.append(matrix[i][right-1])
                right -= 1
                
                if not (left<right and top<bottom):
                    break
                
                #printing the bottom layer from right to left
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom-1][i])
                bottom -= 1
                    
                for i in range(bottom-1, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                
                
            return res