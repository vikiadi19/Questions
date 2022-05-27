class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l, m, count = len(grid), len(grid[0]), 0
        visited = [[False for j in range(m)] for i in range(l)]
        
        for i in range(l):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    self.graph(grid, i, j, visited)
                    
        return count
        
    def graph(self, grid, i, j, visited):
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or visited[i][j] == True or grid[i][j] == "0":
            return
        
        visited[i][j] = True
        self.graph(grid, i-1, j, visited)
        self.graph(grid, i+1, j, visited)
        self.graph(grid, i, j-1, visited)
        self.graph(grid, i, j+1, visited)