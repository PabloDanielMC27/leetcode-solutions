# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # def backtrack(m, n):
        #     if m == 0 and n == 0:
        #         return 1

        #     if obstacleGrid[m][n] == 1:
        #         return 0
            
        #     up = 0
        #     left = 0

        #     if m > 0:
        #         up = backtrack(m - 1, n)
        #     if n > 0:
        #         left = backtrack(m, n - 1)
            
        #     return up + left

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # return backtrack(m - 1, n - 1)

        # def memo(m, n, dp):
        #     if m == 0 and n == 0 and obstacleGrid[m][n] != 1:
        #         return 1

        #     if obstacleGrid[m][n] == 1:
        #         return 0

        #     if dp[m][n] != -1:
        #         return dp[m][n]

        #     up = 0
        #     left = 0
        #     if m > 0:
        #         up = memo(m - 1, n, dp)
        #     if n > 0:
        #         left = memo(m, n - 1, dp)
            
        #     dp[m][n] = up + left
            
        #     return dp[m][n]

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [[-1] * n for _ in range(m)]
        # return memo(m - 1, n - 1, dp)


        def tabulation():

            m = len(obstacleGrid)
            n = len(obstacleGrid[0])

            dp = [[0] * n for _ in range(m)]
                    
            for row in range(m):
                for col in range(n):
                    if row == 0 and col == 0 and obstacleGrid[row][col] != 1:
                        dp[0][0] = 1
                    else:
                        if obstacleGrid[row][col] == 1:
                            dp[row][col] = 0
                        else:
                            up = 0
                            left = 0
                            if row > 0:
                                up = dp[row - 1][col]
                            if col > 0:
                                left = dp[row][col - 1]
                        
                            dp[row][col] = up + left

            return dp[m - 1][n - 1]

        return tabulation()
        
