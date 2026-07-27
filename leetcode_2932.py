# 2932. Maximum Strong Pair XOR I

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        maxV = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    maxV = max(maxV, nums[i] ^ nums[j])

        return maxV

        
