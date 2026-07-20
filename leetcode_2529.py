# 2529. Maximum Count of Positive Integer and Negative Integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        # single pass
        # neg = 0
        # pos = 0
        # for num in nums:
        #     if num < 0:
        #         neg += 1
        #     elif num > 0:
        #         pos += 1
        
        # return max(neg, pos)

        # binary search
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] >= 0:
                r = mid - 1
            else:
                l = mid + 1
        neg = l

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
        pos = len(nums) - l

        return max(neg, pos)


        
