# 1302. Deepest Leaves Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root, level):

            if not root.left and not root.right:
                if level > self.maxLevel:
                    print(level)
                    self.maxLevel = level
                    self.value = 0
                if level == self.maxLevel:
                    self.value += root.val
                return

            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        self.maxLevel = 0
        self.value = 0
        dfs(root, 0)

        return self.value
