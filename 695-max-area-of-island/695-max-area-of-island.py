class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    area = self.graph(grid, visited, i, j)
                    max_area = max(max_area, area)
                    
        return max_area
                    
                    
    def graph(self, grid, visited, i, j):
        
        if i<0 or j<0 or i>=len(grid) or j >=len(grid[0]) or visited[i][j] == True or grid[i][j] == 0:
            return 0
        
        visited[i][j] = True

        up = self.graph(grid, visited, i-1, j)
        down = self.graph(grid, visited, i+1, j)
        left = self.graph(grid, visited, i, j-1)
        right = self.graph(grid, visited, i, j+1)
        
        return up+down+left+right+1
        