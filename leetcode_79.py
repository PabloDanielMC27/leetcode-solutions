# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(idx, row, col):

            if idx == len(word):
                return True
            
            for delrow, delcol in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                nrow = row + delrow
                ncol = col + delcol

                if nrow >= 0 and nrow < self.n and \
                  ncol >= 0 and ncol < self.m and \
                    board[nrow][ncol] == word[idx]:

                    aux = board[nrow][ncol]
                    board[nrow][ncol] = "#"
                   
                    if dfs(idx + 1, nrow, ncol):
                        return True

                    board[nrow][ncol] = aux
                    
            return False


        
        self.n = len(board)
        self.m = len(board[0])


        for row in range(self.n):
            for col in range(self.m):
                if board[row][col] == word[0]:
                    aux = board[row][col]
                    board[row][col] = "#"
                    if dfs(1, row, col):
                        return True
                        
                    board[row][col] = aux

        return False
