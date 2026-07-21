# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # linear time solution
        d = {}

        for i, num in enumerate(nums):
            if num not in d.keys():
                d[target - num] = i
            else:
                return [i, d[num]]

