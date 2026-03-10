# 213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:

        # def backtrack(dp, n):
        #     if n == 0:
        #         return dp[0]

        #     if n < 0:
        #         return 0

        #     take = dp[n] + backtrack(dp, n - 2)
        #     not_take = backtrack(dp, n - 1)
        #     return max(take, not_take)

        # def memo(dp, n, ds):
        #     if n == 0:
        #         return dp[0]

        #     if n < 0:
        #         return 0

        #     if ds[n] != -1:
        #         return ds[n]

        #     take = dp[n] + memo(dp, n - 2, ds)
        #     not_take = memo(dp, n - 1, ds)
        #     ds = max(take, not_take)
        #     return ds

        # dp1 = nums[:-1]
        # dp2 = nums[1:]
        # n = len(nums) - 1
        # ds = [-1] * n

        # if n == 0:
        #     return nums[0]

        # return max(memo(dp1, n - 1, ds), memo(dp2, n - 1, ds))

        # def tabu(dp):
        #     n = len(dp)
        #     ds = [-1] * n

        #     for i in range(n):

        #         if i == 0:
        #             ds[0] = dp[0]

        #         else:
        #             if i == 1:
        #                 ds[1] = max(dp[0], dp[1])
                   
        #             else:
        #                 take = dp[i] + ds[i - 2]
        #                 not_take = ds[i - 1]
        #                 ds[i] = max(take, not_take)
                
        #     return ds[n - 1]

        # dp1 = nums[:-1]
        # dp2 = nums[1:]
        # n = len(nums) - 1
        # ds = [-1] * n

        # if n == 0:
        #     return nums[0]

        # return max(tabu(dp1), tabu(dp2))

        def tabu(dp):
            n = len(dp)

            prev1 = 0
            prev2 = 0

            for i in range(n):
                
                take = dp[i] + prev2
                not_take = prev1
                curr = max(take, not_take)
                
                prev2 = prev1
                prev1 = curr
                
            return prev1

        dp1 = nums[:-1]
        dp2 = nums[1:]
        n = len(nums) - 1

        if n == 0:
            return nums[0]

        return max(tabu(dp1), tabu(dp2))

