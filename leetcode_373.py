# 373. Find K Pairs with Smallest Sums

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # #backtrack
        # PAIR = 2
        # pre_ans = []
        # def backtrack(ds, pre_ans, nums2):
            
        #     if len(ds) == PAIR:
        #         pre_ans.append(list(ds))
        #         return

        #     for num in nums2:
        #         # take
        #         ds.append(num)
        #         backtrack(ds, pre_ans, nums2)
        #         #not take
        #         ds.pop()

        # ds = []
        # for num in nums1:
        #     # take
        #     ds.append(num)
        #     backtrack(ds, pre_ans, nums2)
        #     # not take
        #     ds.pop()

        # pre_ans.sort()
        
        # ans = []
        # for pair in pre_ans:
        #     if k != 0:
        #         ans.append(pair)
        #         k -= 1
        
        # return ans

        # min heap

        ans = []
        queue = []

        # initialize heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(queue, (nums1[i] + nums2[0], i, 0))

        while k > 0 and queue:
            total, i, j = heapq.heappop(queue)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1   

        return ans


            
        
