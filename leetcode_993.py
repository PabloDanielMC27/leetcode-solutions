# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        self.cousins = [(0, None), (-1, None)]

        def dfs(root, parent, level):
            if not root:
                return
            
            if self.cousins[0][0] != 0 and self.cousins[1][0] != -1:
                return

            if root.val == x:
                self.cousins[0] = (level, parent)
            elif root.val == y:
                self.cousins[1] = (level, parent)
            
            dfs(root.left, root, level + 1)
            dfs(root.right, root, level + 1)

        dfs(root,None, 0)
        return self.cousins[0][0] == self.cousins[1][0] and self.cousins[0][1] != self.cousins[1][1]

        
