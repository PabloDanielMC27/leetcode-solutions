# 2824. Count Pairs Whose Sum is Less than Target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # brute force
        # nums.sort()

        # total = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             total += 1
        # return total

        # two pointers
        nums.sort()
        n = len(nums)
        total = 0

        l = 0
        r = n - 1
        while l < r:
            
            if nums[l] + nums[r] < target:
                total += r - l
                l += 1
            else:
                r -= 1
            
        return total
