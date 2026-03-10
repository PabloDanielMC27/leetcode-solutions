# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # def backtrack(m , n, dp):
                       
        #     if m < 0 or n < 0:
        #         return 0

        #     if dp[m][n] != -1:
        #         return dp[m][n]

        #     up = backtrack(m - 1, n, dp)
        #     left = backtrack(m, n - 1, dp)
        #     dp[m][n] = up + left
        #     return dp[m][n]
        
        # dp = [[-1] * n for _ in range(m)]
        # dp[0][0] = 1
        # return backtrack(m - 1, n - 1, dp)

        def tabulation(dp):
                       
           for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0: up = dp[i - 1][j]
                    if j > 0: left = dp[i][j - 1]
                    dp[i][j] = up + left

        dp = [[0] * n for _ in range(m)]
        tabulation(dp)
        return dp[m - 1][n - 1]
        

        

        
