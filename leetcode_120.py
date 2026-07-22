# 120. Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # def backtrack(level, idx):

        #     if level == len(triangle) - 1:
        #         return triangle[level][idx]

        #     minV = min(backtrack(level + 1, idx), backtrack(level + 1, idx + 1))

        #     return triangle[level][idx] + minV

        # return backtrack(0, 0)

        # def backtrack2(level, idx, ds):

        #     if level == len(triangle) - 1:
        #         return ds[level][idx]

        #     if ds[level][idx] != float('inf'):
        #         return ds[level][idx]

        #     minV = min(backtrack2(level + 1, idx, ds), backtrack2(level + 1, idx + 1, ds))

        #     ds[level][idx] = triangle[level][idx] + minV
        #     return ds[level][idx]

        # ds = [[float('inf')] * len(triangle) for _ in range(len(triangle))]
        # for i in range(len(triangle)):
        #     ds[-1][i] = triangle[-1][i]

        # return backtrack2(0, 0, ds)


        ds = [[float('inf')] * len(triangle) for _ in range(len(triangle))]
        ds[0][0] = triangle[0][0]
        
        for level in range(1, len(triangle)):
            for idx in range(level + 1):
                if idx == 0:
                    ds[level][idx] = triangle[level][idx] + ds[level - 1][idx]
                elif idx == level:
                    ds[level][idx] = triangle[level][idx] + ds[level - 1][idx - 1]
                else:
                    ds[level][idx] = triangle[level][idx] + min(ds[level - 1][idx], ds[level -1][idx - 1]) 

        return min(ds[-1])
