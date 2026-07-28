# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = fast = head
        n = 1
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            n += 2
        if fast.next:
            n += 1
            fast.next.next = head
        else:
            fast.next = head

        k = k % n

        dummy = ListNode()
        dummy.next = head

        for i in range(n - k):
            dummy = dummy.next
            head = head.next

        dummy.next = None

        return head
        
