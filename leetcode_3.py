# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # l,r,maxV = 0, 0, 0

        # d = {}

        # while (r < len(s)):
            
        #     d[s[r]] = 1 + d.get(s[r],0)

        #     while d[s[r]] > 1:
        #         d[s[l]] -= 1
        #         l += 1

        #     maxV = max(maxV, r - l + 1)
        #     r += 1
        
        # return maxV


        l,r,maxV = 0, 0, 0

        seen = {}

        while (r < len(s)):
            
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            seen[s[r]] = r

            maxV = max(maxV, r - l + 1)
            r += 1
        
        return maxV


