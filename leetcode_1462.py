# 1462. Course Schedule IV

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # kahn algorithm
        d = defaultdict(set)

        adj = [[] for _ in range(numCourses)]
        for start, end in prerequisites:
            adj[end].append(start)

        inDegree = [0] * numCourses
        for node in adj:
            for end in node:
                inDegree[end] += 1

        queue = deque()
        for node, value in enumerate(inDegree):
            if value == 0:
                queue.append(node)

        while queue:
            leaf = queue.popleft()

            for node in adj[leaf]:
                d[node].add(leaf)
                d[node] |= d[leaf]

                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)

        ans = []
        for first, last in queries:
            if last in d[first]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
                

            





        
