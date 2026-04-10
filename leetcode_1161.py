# 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # bfs
        queue =deque([(root)])
        maxV = root.val
        ans = 1
        level = 1
        while queue:
            nodes_in_level = len(queue)
            total = 0
            for _ in range(nodes_in_level):
                
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))

            if total > maxV:
                maxV = total
                ans = level

            level += 1

        return ans

        # # dfs
        # def dfs(root, level):
        #     if not root:
        #         return

        #     if len(levels) == level:
        #         levels.append(root.val) 
        #     else:
        #         levels[level] += root.val

        #     dfs(root.left, level + 1)
        #     dfs(root.right, level + 1)


        # levels = []
        # dfs(root, 0)
        # maxV = max(levels)
        # for i in range(len(levels)):
        #     if levels[i] == maxV:
        #         return i + 1

            

        
