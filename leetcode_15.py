# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # brute force + set
        # nums.sort()

        # l = 0
        # n = len(nums)

        # st = set()
        # while l < n - 2:
        #     m = l + 1
        #     r = n - 1

        #     while m < r:
        #         total = nums[l] + nums[m] + nums[r]
        #         if  total == 0:
        #             st.add((nums[l], nums[m], nums[r]))
        #             m += 1

        #         elif total > 0:
        #             r -= 1
        #         else:
        #             m += 1
            
        #     l += 1

        # return list(st)

        # constant space
        nums.sort()

        l = 0
        n = len(nums)

        ans = []
        while l < n - 2:
            m = l + 1
            r = n - 1

            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if  total == 0:
                    ans.append([nums[l], nums[m], nums[r]])

                    while m < r and nums[m] == nums[m + 1]:
                        m += 1
                    while m < r and nums[r] == nums[r - 1]:
                        r -= 1
                    m += 1

                elif total > 0:
                    r -= 1
                else:
                    m += 1
            while l < n - 1 and nums[l] == nums[l + 1]:
                l += 1
            l += 1

        return ans
