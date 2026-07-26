# 221. Maximal Square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # self.max = 0

        # def backtrack(row, col):

        #     if row < 0 or col < 0:
        #         return 0

        #     left = backtrack(row, col - 1)
        #     up = backtrack(row - 1, col)
        #     diag = backtrack(row - 1, col - 1)
        #     val = min(left, up, diag)
        #     if matrix[row][col] == '1':
        #         self.max = max(self.max, 1 + val)
        #         return 1 + val
        #     else:
        #         return 0

        # m = len(matrix) - 1 
        # n = len(matrix[0]) - 1
        # backtrack(m, n)
        # return self.max * self.max

        # self.max = 0

        # def memoization(row, col, dp):

        #     if row < 0 or col < 0:
        #         return 0

        #     if dp[row][col] != 0:
        #         return dp[row][col]
        #     else:
        #         left = memoization(row, col - 1, dp)
        #         up = memoization(row - 1, col, dp)
        #         diag = memoization(row - 1, col - 1, dp)
        #         val = min(left, up, diag)
        #         if matrix[row][col] == '1':
        #             self.max = max(self.max, 1 + val)
        #             dp[row][col] = 1 + val

        #         return dp[row][col]

        # m = len(matrix) 
        # n = len(matrix[0])

        # dp = [[0] * n for _ in range(m)]
        # memoization(m - 1, n - 1, dp)
        # return self.max * self.max

        self.max = 0
        m = len(matrix) 
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for row in range(1, m  + 1):
            for col in range(1, n + 1):

                left = dp[row][col - 1]
                up = dp[row - 1][col]
                diag = dp[row - 1][col - 1]
                val = min(left, up, diag)
                if matrix[row - 1][col - 1] == '1':
                    self.max = max(self.max, 1 + val)
                    dp[row][col] = 1 + val
        
        return self.max * self.max
            
        
