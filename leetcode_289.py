# 289. Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):

                count = 0

                neigh_row = [-1, 0, 1]
                neigh_col = [-1, 0, 1]
                for delrow in neigh_row:
                    for delcol in neigh_col:

                        if delrow == 0 and delcol == 0:
                            continue

                        nrow = delrow + row
                        ncol = delcol + col
                        if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and (board[nrow][ncol] == 1 or board[nrow][ncol] == 4):
                            count += 1

                if (count < 2 or count > 3) and board[row][col] == 1:
                    board[row][col] = 4  # from 1 to 0
                
                elif count == 3 and board[row][col] == 0:
                    board[row][col] = 5  # from 0 to 1

        for row in range(m):
            for col in range(n):
                if board[row][col] == 4:
                    board[row][col] = 0
                elif board[row][col] == 5:
                    board[row][col] = 1
        
