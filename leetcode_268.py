# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # O(n) space
        # st = set(nums)

        # for i in range(len(nums) + 1):
        #     if i not in st:
        #         return i


        # O(1) space
        n = len(nums)

        total = n * (n + 1) // 2

        for num in nums:
            total -= num
        return total
