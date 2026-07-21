# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = -1
        while l <= r:
            k = (r - l) // 2 + l

            eat = 0
            for pile in piles:
                eat += math.ceil(pile / k)

            if eat <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1

        return ans
        
