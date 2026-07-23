# 671. Second Minimum Node In a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        self.ans = float('inf')

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)

            if root.val > dummy.val:
                self.ans = min(self.ans, root.val)

        dummy = root
        dfs(root)
        return self.ans if self.ans < float('inf') else -1


            
        
