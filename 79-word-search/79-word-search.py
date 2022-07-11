class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def move(board, i, j, visited, word, k):
            if k == len(word):
                return True
            
            if i<0 or j<0 or i>=len(board) or j>= len(board[0]) or visited[i][j] == True or board[i][j] != word[k]:
                return False
            
            
            visited[i][j] = True
            
            a = move(board, i-1, j, visited, word,k+1) 
            b = move(board, i+1, j, visited, word,k+1) 
            c = move(board, i, j-1, visited, word,k+1) 
            d = move(board, i, j+1, visited, word,k+1)
            visited[i][j] = False
            
            return a or b or c or d
            
        
        
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and visited[i][j] != True:
                    res = move(board, i, j, visited, word, 0)
                    if res == True:
                        return True
                    
        return False
            
        