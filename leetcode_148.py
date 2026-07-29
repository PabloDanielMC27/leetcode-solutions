# 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # linear space
        if not head or not head.next:
            return head

        lst = []

        dummy = head
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next

        lst.sort()

        dummy = head
        i = 0
        while dummy:
            dummy.val = lst[i]
            dummy = dummy.next
            i += 1

        return head 

        # merge sort (log n space)
        # def sort(head):

        #     if not head or not head.next:
        #         return head
        
        #     slow = fast = head

        #     while fast.next and fast.next.next:
        #         slow = slow.next
        #         fast = fast.next.next
        
        #     second = slow.next
        #     slow.next = None
            
        #     first = sort(head)
        #     second = sort(second)
        #     return merge(first, second)

        # def merge(a, b):
            
        #     dummy = tail = ListNode()
        #     while a and b:
        #         if a.val <= b.val:
        #             tail.next, a = a, a.next
        #         else:
        #             tail.next, b = b, b.next
        #         tail = tail.next
        #     tail.next = a or b        
        #     return dummy.next

        # return sort(head)

            
            
