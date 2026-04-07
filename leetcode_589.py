# 589. N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def func(root):
            if not root:
                return

            self.ans.append(root.val)

            for child in root.children:
                func(child)

        self.ans = []
        func(root)
        return self.ans
