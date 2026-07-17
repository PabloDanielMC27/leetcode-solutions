# 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n
        first_bad = 0

        while l <= r:
            mid = (r - l) // 2 + l
            
            if isBadVersion(mid):    
                first_bad = mid
                r = mid - 1

            else:
                l = mid + 1

        return first_bad

            
            

            
        
