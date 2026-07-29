# 654. Maximum Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def addNode(l, r):

            if l == r:
                return None
            
            max_val = -1
            max_idx = -1
            for i in range(l, r):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_idx = i

            node = TreeNode(max_val)
            node.left = addNode(l, max_idx)
            node.right = addNode(max_idx + 1, r)

            return node

        r = len(nums)
        l = 0    
        return addNode(l, r)
            


        
