# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:

        # def backtrack(n):
        #     if n == 0:
        #         return nums[0]
            
        #     if n < 0:
        #         return - 1

        #     return max(nums[n] + backtrack(n - 2), backtrack(n - 1))


        # n = len(nums)
        # return backtrack(n - 1)

        # def memo(n, dp):
                       
        #     if n < 0:
        #         return 0

        #     if dp[n] != -1:
        #         return dp[n]
            
        #     dp[n] = max(nums[n] + memo(n - 2, dp), memo(n - 1, dp))

        #     return dp[n]


        # n = len(nums)
        # dp = [-1] * n
        # dp[0] = nums[0]
        # return memo(n - 1, dp)
        

        # def tabulation():
                       
        #     n = len(nums)
        #     if n == 1:
        #         return nums[0]

        #     dp = [0] * n

        #     dp[0] = nums[0]

        #     for i in range(1, n):
        #         if i == 1: 
        #             dp[1] = max(nums[0], nums[1])
        #         else:
        #             take = nums[i] + dp[i - 2]
        #             not_take = dp[i - 1] # + 0
        #             dp[i] = max(take, not_take)
        #     return dp[n - 1]

        # return tabulation()

        def tabulation():
                       
            n = len(nums)
            if n == 1:
                return nums[0]

            prev1 = nums[0]
            prev2 = 0

            for i in range(1, n):
                curr = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return prev1
        return tabulation()
