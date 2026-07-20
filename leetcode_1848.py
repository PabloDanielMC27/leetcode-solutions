# 1848. Minimum Distance to the Target Element

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        # single pass
        ans = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))
        return ans

        
