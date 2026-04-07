# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def func(root):

            if not root:
                return 0

            lh = func(root.left)
            rh = func(root.right)

            self.total += abs(lh - rh)

            return lh + rh + root.val
        
        self.total = 0
        func(root)
        return self.total
        
