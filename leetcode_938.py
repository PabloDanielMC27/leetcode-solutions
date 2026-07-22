# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # def dfs(root):

        #     if not root:
        #         return

        #     dfs(root.left)
        #     if low <= root.val <= high:
        #         self.maxVal += root.val
        #     dfs(root.right)
        
        # self.maxVal = 0
        # dfs(root)
        # return self.maxVal

        
        def dfs(root):

            if not root:
                return

            if root.val >= low:
                dfs(root.left)

            if low <= root.val <= high:
                self.maxVal += root.val
            
            if root.val <= high:
                dfs(root.right)
        
        self.maxVal = 0
        dfs(root)
        return self.maxVal
        
