# 2089. Find Target Indices After Sorting Array

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        # single pass
        # nums.sort()
        # ans = []
        # for i, num in enumerate(nums):
        #     if num == target:
        #         ans.append(i)
        # return ans

        # binary search
        nums.sort()
        ans = []
        first = last = -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        first = l

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        last = r

        for num in range(first, last + 1):
            ans.append(num)

        return ans 
