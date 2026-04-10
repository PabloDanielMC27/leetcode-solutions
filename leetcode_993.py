# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # dfs
        # self.cousins = [(0, None), (-1, None)]

        # def dfs(root, parent, level):
        #     if not root:
        #         return
            
        #     if self.cousins[0][0] != 0 and self.cousins[1][0] != -1:
        #         return

        #     if root.val == x:
        #         self.cousins[0] = (level, parent)
        #     elif root.val == y:
        #         self.cousins[1] = (level, parent)
            
        #     dfs(root.left, root, level + 1)
        #     dfs(root.right, root, level + 1)

        # dfs(root,None, 0)
        # return self.cousins[0][0] == self.cousins[1][0] and self.cousins[0][1] != self.cousins[1][1]

        # bfs


        queue = deque([(root, None)])
        
        while queue:
            nodes_in_level = len(queue)
            x_parent = None
            y_parent = None

            for _ in range(nodes_in_level):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False
