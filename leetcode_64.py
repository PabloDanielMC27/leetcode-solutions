# 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # def backtrack(m, n):

        #     if m == 0 and n == 0:
        #         return grid[0][0]

        #     if m < 0 or n < 0:
        #         return float("inf")

        #     return grid[m][n] + min(backtrack(m - 1, n), backtrack(m, n - 1)) 

        # m = len(grid)
        # n = len(grid[0])
        # return backtrack(m - 1, n - 1)

        # def backtrack2(m, n, dp):

        #     if m == 0 and n == 0:
        #         return grid[0][0]

        #     if m < 0 or n < 0:
        #         return float("inf")
            
        #     if dp[m][n] != -1:
        #         return dp[m][n]

        #     dp[m][n] = grid[m][n] + min(backtrack2(m - 1, n, dp), backtrack2(m, n - 1, dp)) 
        #     return dp[m][n]

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # return backtrack2(m - 1, n - 1, dp)

        class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # def backtrack(m, n):

        #     if m == 0 and n == 0:
        #         return grid[0][0]

        #     if m < 0 or n < 0:
        #         return float("inf")

        #     return grid[m][n] + min(backtrack(m - 1, n), backtrack(m, n - 1)) 

        # m = len(grid)
        # n = len(grid[0])
        # return backtrack(m - 1, n - 1)

        # def backtrack2(m, n, dp):

        #     if m == 0 and n == 0:
        #         return grid[0][0]

        #     if m < 0 or n < 0:
        #         return float("inf")
            
        #     if dp[m][n] != -1:
        #         return dp[m][n]

        #     dp[m][n] = grid[m][n] + min(backtrack2(m - 1, n, dp), backtrack2(m, n - 1, dp)) 
        #     return dp[m][n]

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # return backtrack2(m - 1, n - 1, dp)

        def tabulation(m, n):

            dp = [[-1] * n for _ in range(m)]      

            for row in range(0, m):
                for col in range(0, n):
                    if row == 0 and col == 0:
                        dp[0][0] = grid[0][0]

                    else:
                        up = float('inf')
                        left = float('inf')
                        if row > 0:
                            up = dp[row - 1][col]
                        if col > 0:
                            left = dp[row][col - 1]
                        dp[row][col] = grid[row][col] + min(up, left)
 
            return dp[m - 1][n - 1]

        m = len(grid)
        n = len(grid[0])
        return tabulation(m, n)             
