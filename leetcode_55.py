# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # backtrack
        # def backtrack(idx):

        #     if idx >= len(nums) - 1:
        #         return True

        #     for i in range(1, nums[idx] + 1):
        #         if backtrack(idx + i):
        #             return True
            
        #     return False


        # return backtrack(0)

        # memoization
        # def memoization(idx, ds):

        #     if idx >= len(nums) - 1:
        #         return True

        #     if ds[idx] is not None:
        #         return ds[idx]

        #     for i in range(1, nums[idx] + 1):
        #         if memoization(idx + i, ds):
        #            ds[idx] = True
        #            return True
            
        #     ds[idx] = False
        #     return False

        # ds = [None] * len(nums)
        # return memoization(0, ds)

        # tabulation
        # ds = [False] * len(nums)
        # ds[-1] = True
        
        # for i in range(len(nums) - 2, -1, -1):
        #     closer = min(i + nums[i], len(nums) - 1)
        #     for j in range(i + 1, closer + 1):
        #         if ds[j]:
        #             ds[i] = True
        #             break
        # return ds[0]

        # greedy
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        
