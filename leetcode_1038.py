# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.total = 0
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)

            self.total += root.val

        def dfs2(root):
            if not root:
                return
            
            dfs2(root.left)
            
            aux = root.val
            root.val = self.total
            self.total -= aux

            dfs2(root.right)

        dfs(root)
        dfs2(root)
        return root

        

            

            
        
