# 3643. Flip Square Submatrix Vertically

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:


        m = len(grid)
        n = len(grid[0])
        
        nmat = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                nmat[row][col] = grid[row][col]
        # nmat = [row[:] for row in grid]

        up = x
        down = x + k - 1
        while up < down:
            for i in range(y, y + k):
                nmat[up][i], nmat[down][i] = nmat[down][i], nmat[up][i]

            up += 1
            down -= 1 

        return nmat

        
