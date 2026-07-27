# 1011. Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights) 
        r = n = sum(weights)

        ans = n

        while l <= r:
            mid = (r - l) // 2 + l
            cap = mid
            tot = 1
            for weight in weights:
                if weight <= cap:
                    cap -= weight
                else:
                    tot += 1
                    cap = mid
                    cap -= weight
            
            if tot <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
