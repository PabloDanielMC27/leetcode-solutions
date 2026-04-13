# 322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # backtrack
        # def backtrack(target):

        #     if target == 0:
        #         return 0

        #     minCoins = float('inf')
        #     for coin in coins:
        #         if target - coin >= 0:
        #             minCoins = min(minCoins, 1 + backtrack(target - coin))
        #     return minCoins

        # ans =  backtrack(amount)
        # if ans == float('inf'):
        #     return - 1
        # return ans

        # memo
        # def memo(target, ds):

        #     if target == 0:
        #         return ds[0]
                
        #     if ds[target] < float('inf'):
        #         # already calculated
        #         return ds[target]
    
        #     minCoins = ds[target]
        #     for coin in coins:
        #         if target - coin >= 0:
        #             minCoins = min(minCoins,1 + memo(target - coin, ds))
        #     ds[target] = minCoins
        #     return ds[target]

        # memoization ds
        # ds = [float('inf')] * (amount + 1)
        # ds[0] = 0

        # memo(amount, ds)
        # if ds[-1] == float('inf'):
        #     return -1
        # return ds[-1]

        # tabulation
        ds = [float('inf')] * (amount + 1)
        ds[0] = 0
            
        for i in range(1, len(ds)):
            for coin in coins:
                if i - coin >= 0:
                    ds[i] = min(ds[i], 1 + ds[i - coin])                  

        if ds[-1] == float('inf'):
            return -1
        return ds[-1]
      


                
        
