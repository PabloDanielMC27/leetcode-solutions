# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # divide and conquer
        # def mergesort(list1, list2):

        #     dummy = curr = ListNode()
        #     while list1 and list2:
        #         if list1.val <= list2.val:
        #             curr.next = list1
        #             list1 = list1.next
        #         else:
        #             curr.next = list2
        #             list2 = list2.next
        #         curr = curr.next
        #     curr.next = list1 or list2

        #     return dummy.next

        # cpy = list(lists)
        # while len(cpy) > 1:
        #     merged = []
        #     for i in range(0, len(cpy), 2):
        #         if i + 1 < len(cpy):
        #             merged.append(mergesort(cpy[i], cpy[i + 1]))
        #         else:
        #             merged.append(cpy[i])

        #     cpy = merged
        # return cpy[0] if cpy else None

        # min heap
        queue = []
        heapify(queue)
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(queue, (head.val, i, head))

        dummy = curr = ListNode()
        while queue:
            value, i, node = heapq.heappop(queue)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(queue, (node.next.val, i, node.next))

        return dummy.next
