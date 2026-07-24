# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        # dfs
        # def dfs(root):
        #     if not root:
        #         return True
            
        #     lh = dfs(root.left)
        #     if not lh:
        #         return False
        #     rh = dfs(root.right)
        #     if not rh:
        #         return False

        #     if root.val != self.reference:
        #         return False
            
        #     return True
        
        # self.reference = root.val
        # return dfs(root)

        # bfs
        queue = deque()
        queue.append(root)
        reference = root.val
        
        while queue:
            node = queue.popleft()

            if node.val != reference:
                return False
            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return  True
                
        
