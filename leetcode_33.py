# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # brute force
        # for i, number in enumerate(nums):
        #     if number == target:
        #         return i
        # return -1

        # binary search
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
