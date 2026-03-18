# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # ans = []
        # for num in nums1:
        #     stack = []
        #     visit = False
        #     number = -1
        #     for num2 in nums2:
        #         stack.append(num2)
        #         if num == num2:
        #             visit = True
                
        #         if visit and num2 > num:
        #             number = num2
        #             break
            
        #     ans.append(number)

        # return ans
                
        
        stack = []
        pairs = {}
  
        for num in reversed(nums2):

            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                pairs[num] = stack[-1] 
            else:
                pairs[num] = -1

            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(pairs[num])
        
        return ans
