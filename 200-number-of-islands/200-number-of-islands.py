class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for c in range(len(grid[0]))] for r in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] == "1":
                    self.move(grid, i, j, visited)
                    count += 1
        return count
    
    def move(self, grid, i, j, visited):
        if(i<0 or j<0 or i >=len(grid) or j >=len(grid[0]) or visited[i][j] == True or grid[i][j] == "0"):
            return
        visited[i][j] = True
        self.move(grid, i+1, j, visited)
        self.move(grid, i, j+1, visited)
        self.move(grid, i-1, j, visited)
        self.move(grid, i, j-1, visited)