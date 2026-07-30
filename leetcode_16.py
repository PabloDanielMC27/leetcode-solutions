# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        l = 0
        n = len(nums)
        closest = distance = float('inf')
        
        for l in range(n - 2):

            m = l + 1
            r = n - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]

                if total == target:
                    return target

                if abs(total - target) < distance:
                    distance = abs(total - target)
                    closest = total

                if total > target:
                    r -= 1
                else:
                    m += 1

        return closest
        
                

        
