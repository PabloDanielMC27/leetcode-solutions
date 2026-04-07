# 559. Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def f(root):
        
            if not root:
                return 0

            maxV = 0
            for child in root.children:
                maxV = max(maxV, f(child))
            return  1 + maxV

        return f(root)

   
