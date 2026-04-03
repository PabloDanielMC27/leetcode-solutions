# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # brute force
        # n = len(heights)

        # maxx = 0
        # for i in range(n):
        #     min_heights = heights[i]
        #     for j in range(i, n):
        #         min_heights = min(min_heights, heights[j])
        #         base = j - i + 1
        #         maxx = max(maxx, base * min_heights)

        # return maxx


        # one pass
        stack = [] # index stack
        new_heights = [0] + heights + [0]
        n = len(new_heights)

        maxx = 0
        for i in range(n):
            while stack and new_heights[i] < new_heights[stack[-1]]:
                top = stack.pop()
                height = new_heights[top]
                base = i - stack[-1] - 1
                maxx = max(maxx, base * height)
            stack.append(i) 

        return maxx
        


        
