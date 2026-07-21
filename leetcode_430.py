# 430. Flatten a Multilevel Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            curr = node
            tail = node

            while curr:
                nextNode = curr.next

                if curr.child:
                    childTail = dfs(curr.child)
                    curr.next = curr.child
                    curr.child.prev = curr

                    curr.child = None

                    childTail.next = nextNode
                    if nextNode:
                        nextNode.prev = childTail
                    tail = childTail
                else:
                    tail = curr


                curr = nextNode

            return tail
        
        dfs(head)
        return head


