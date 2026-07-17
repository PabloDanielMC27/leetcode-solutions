# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:

        # row = 0
        # summ = 0
        # for i in range(1, n + 1):
        #     summ += i
        #     if summ <= n:
        #         row += 1
        #     else:
        #         break        
    
        # return row

        l = 1
        r = n
        ans = 0
        while l <= r:
            mid = (r - l) // 2 + l
            partial_sum = mid * (mid + 1) // 2
            if partial_sum <= n:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
