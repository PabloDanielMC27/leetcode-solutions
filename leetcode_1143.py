# 1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # # backtrack
        # def backtrack(i, j):

        #     if i < 0 or j < 0:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return 1 + backtrack(i - 1, j - 1)

        #     return max(backtrack(i - 1, j), backtrack(i, j - 1))

        # m = len(text1)
        # n = len(text2)
        # return backtrack(m - 1, n - 1)

        # memoization
        # def memoization(i, j, ds):

        #     if i < 0 or j < 0:
        #         return 0

        #     if ds[i][j] != -1:
        #         return ds[i][j]

        #     if text1[i] == text2[j]:
        #         ds[i][j] = 1 + memoization(i - 1, j - 1, ds)
        #         return ds[i][j]

        #     ds[i][j] = max(memoization(i - 1, j, ds), memoization(i, j - 1, ds)) 
        #     return ds[i][j]

        # m = len(text1)
        # n = len(text2)
        # ds = [[-1] * n for _ in range(m)]
        # return memoization(m - 1, n - 1, ds)

        #tabulation
        m = len(text1)
        n = len(text2)

        ds = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(len(ds)):
            ds[i][0] = 0
        for i in range(len(ds[0])):
            ds[0][i] = 0
        
        for i in range(1, len(ds)):
            for j in range(1, len(ds[0])):
                if text1[i - 1] == text2[j - 1]:
                    ds[i][j] = 1 + ds[i - 1][j - 1]
                else:
                    ds[i][j] = max(ds[i - 1][j], ds[i][j - 1])
        
        return ds[-1][-1]

        
        
