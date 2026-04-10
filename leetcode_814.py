# 814. Binary Tree Pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return False
            
            lh = dfs(root.left)
            if not lh: # lh does not have 1 in subtree
                root.left = None 
            rh = dfs(root.right)
            if not rh: # rh does not have 1 in subtree
                root.right = None
            
            if root.val == 1 or lh or rh:
                return True
            return False 

        if dfs(root):
            return root
        return None
