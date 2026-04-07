# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def func(root):

            if not root:
                return

            for child in root.children:
                func(child)

            self.ans.append(root.val)


        self.ans = []
        func(root)
        return self.ans
        
