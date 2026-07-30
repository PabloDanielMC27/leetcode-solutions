# 1372. Longest ZigZag Path in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        
        def dfs(root, count, left):
        
            if not root:
                return

            self.max = max(self.max, count)

            if left:
                dfs(root.left, 1, True)
            else:
                dfs(root.left, 1 + count, True)

            if not left:
                dfs(root.right, 1, False)
            else:
                dfs(root.right, 1 + count, False)

        self.max = 0
        dfs(root, 0, False)
        return self.max
