class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def move(grid, visited, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or visited[i][j] == True or grid[i][j] == "0":
                return
            
            visited[i][j] = True
            
            move(grid, visited, i-1, j)
            move(grid, visited, i+1, j)
            move(grid, visited, i, j-1)
            move(grid, visited, i, j+1)
        
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    move(grid, visited, i, j)
                    
                    
        return count
        
        
        