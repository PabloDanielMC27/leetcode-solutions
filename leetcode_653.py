# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()

        def dfs(root):
            if not root:
                return False
            
            if root.val not in visited:
                visited.add(k - root.val)
            else:
                return True


            lh = dfs(root.left)
            if lh:
                return True
            rh = dfs(root.right)
            if rh:
                return True

            return False

        return dfs(root)

        
