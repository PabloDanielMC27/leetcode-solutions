# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min heap O(k logn)
        # nums =[-x for x in nums]
        # heapify(nums)
        # for i in range(k - 1):
        #     heapq.heappop(nums)

        # return -nums[0]

        # min heap (efficient) O(n log k)
        # queue = []
        # heapify(queue)
        # count = 0
        # for num in nums:
        #     if count < k:
        #         heapq.heappush(queue, num)
        #         count += 1
        #     elif num > queue[0]:
        #         heapq.heappushpop(queue, num)

        # return queue[0]

        # # quickselect
        # def quickselect(l, r, target):
        #     if r <= l:
        #         return

        #     pivot = random.randint(l, r) 
        #     nums[pivot], nums[r] = nums[r], nums[pivot]
            
        #     i = l - 1
        #     for j in range(l, r):
        #         if nums[j] <= nums[r]:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]

        #     nums[i + 1], nums[r] = nums[r], nums[i + 1]

        #     if target < i + 1:
        #         quickselect(l, i, target)
        #     elif target > i + 1:
        #         quickselect(i + 2, r, target)
        #     else:
        #         return

        # l = 0
        # r = len(nums) - 1
        # target = len(nums) - k
        # quickselect(l, r, target)

        # return nums[target]

        # dutch flag
        if not nums: 
            return
            
        pivot = random.choice(nums)
        left =  [x for x in nums if x < pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        R, M = len(right), len(mid)
        
        if k <= R:
            return self.findKthLargest(right, k)
        elif k > M + R:
            return self.findKthLargest(left, k - M - R)
        else:
            return mid[0]

        
        
