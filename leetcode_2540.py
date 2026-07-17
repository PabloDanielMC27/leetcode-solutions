# 2540. Minimum Common Value

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        #set solution

        # st = set(nums1)

        # for num in nums2:
        #     if num in st:
        #         return num
        # return -1

        # binary search
        # for number in nums2:
        #     l = 0
        #     r = len(nums1) - 1

        #     while l <= r:
        #         mid = (r - l) // 2 + l
                
        #         if nums1[mid] == number:
        #             return number
        #         if nums1[mid] < number:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        
        # return -1

        # two pointer

        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
        
