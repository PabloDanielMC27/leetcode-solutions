# 310. Minimum Height Trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # kahn algorithm
        adj = [[] for _ in range(n)]
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        inDegree = [0] * n
        for num in range(n):
            for end in adj[num]:
                inDegree[end] += 1

        st = set([i for i in range(n)])

        leaves = deque()
        for node, count in enumerate(inDegree):
            if count == 1:
                leaves.append(node)

        while len(st) > 2:
            size = len(leaves) 

            for _ in range(size):
                leaf = leaves.popleft()
                inDegree[leaf] -= 1
                st.remove(leaf)

                for neighbor in adj[leaf]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 1:
                        leaves.append(neighbor)
            
        return list(st)



            


                
