# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:

        # n = len(height)

        # left = []
        # maxL = 0
        # for i in range(n):
        #     maxL = max(maxL, height[i])
        #     left.append(maxL)
            

        # right = []
        # maxR = 0
        # for i in range(n - 1, -1, -1):
        #     maxR = max(maxR, height[i])
        #     right.append(maxR)
        
        # print(left, right)

        # total = 0
        # for i in range(n):
        #     total += min(left[i], right[n - 1 - i]) - height[i]
        
        # return total

        l, r = 0, len(height) - 1

        maxL = 0
        maxR = 0
        total = 0
        while l <= r:

            if maxL <= maxR:
                temp = min(maxL, maxR) - height[l]
                maxL = max(maxL, height[l])
                l += 1 
            else:
                temp = min(maxL, maxR) - height[r]
                maxR = max(maxR, height[r])
                r -= 1

            if temp > 0:
                total += temp

        return total
