# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            self.newNode.right = TreeNode(root.val)
            self.newNode = self.newNode.right
            dfs(root.right) 

        dummy = self.newNode = TreeNode(-1)
        dfs(root)
        return dummy.right


        
