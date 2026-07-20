# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:

        minV = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:

            if nums[l] < nums[r]:
                minV = min(minV, nums[l])
                break
                
            mid = (r - l) // 2 + l
            minV = min(minV, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return minV
