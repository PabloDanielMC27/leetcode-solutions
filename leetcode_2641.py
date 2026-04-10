# 2641. Cousins in Binary Tree II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # #bfs
        # queue = deque([(root, None)])
        # root.val = 0
        # level = 0

        # while queue:
        #     nodes_in_level = len(queue)
        #     total_sum = 0
        #     parent_sum_and_total = {}
        #     # get totals per parent and level total
        #     for _ in range(nodes_in_level):
        #         node, parent = queue.popleft()
      
        #         parent_sum_and_total[parent] = node.val + parent_sum_and_total.get(parent, 0)           

        #         total_sum += node.val

        #         queue.append((node, parent))

        #     # define if root.val is 0
        #     for _ in range(nodes_in_level):
        #         node, parent = queue.popleft()
       
        #         node.val = total_sum - parent_sum_and_total[parent]
               
        #         if node.left:
        #             queue.append((node.left, node))
        #         if node.right:
        #             queue.append((node.right, node))

        # return root


        # bfs

        queue = deque([root])
        root.val = 0

        while queue:
            size = len(queue)
            next_level_sum = 0
            level_nodes = []

            for _ in range(size):
                node = queue.popleft()
                level_nodes.append(node)

                if node.left:
                    next_level_sum += node.left.val
                if node.right:
                    next_level_sum += node.right.val

            for node in level_nodes:
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                
                if node.left:
                    node.left.val = next_level_sum - sibling_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = next_level_sum - sibling_sum
                    queue.append(node.right)

        return root
