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

        def backtrack(dp):
                       
           for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i > 0 and j > 0:
                    dp[i][j] += dp[i][j - 1] + dp [i -1][j] 
                else:
                    dp[i][j] = 1

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        backtrack(dp)
        return dp[m - 1][n - 1]
        

        

        
