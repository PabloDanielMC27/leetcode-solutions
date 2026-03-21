# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # #floyd-warshall

        # mat = [[(float('inf'))] * n for _ in range(n)]

        # for i in range(n):
        #     mat[i][i] = 0

        # for edge in edges:
        #     start = edge[0]
        #     end = edge[1]
        #     dist = edge[2]

        #     mat[start][end] = dist
        #     mat[end][start] = dist

        # for k in range(n):
        #     for row in range(n):
        #         for col in range(n):
        #             if mat[row][k] + mat[k][col] < mat[row][col]:
        #                 mat[row][col] = mat[row][k] + mat[k][col]

        
        # dist = [0] * n
        # minv = float('inf')
        # for row in range(n):
        #     for col in range(n):
        #         if mat[row][col] > 0 and mat[row][col] <= distanceThreshold:
        #             dist[row] += 1

        #     minv = min(minv, dist[row])

        # for i in range(n - 1, -1, -1):
        #     if dist[i] == minv:
        #         return i 

        # return -1



        #dijkstra

        #build adj list
        adj = [[] for _ in range(n)]
        for edge in edges:
            node = edge[0]
            neighbor = edge[1]
            cost = edge[2]

            adj[node].append((neighbor, cost))
            adj[neighbor].append((node, cost))
        
        def solve(node, adj):

            #build dist vector
            dist = [float('inf')] * n
            dist[node] = 0

            #build queue
            queue = []
            heapq.heappush(queue, (0, node))

            while queue:
                cost, node = heapq.heappop(queue)
                if cost > dist[node]:
                        continue

                for neighbor in adj[node]:
                    newNode = neighbor[0]
                    newCost = neighbor[1]
                    
                    if cost + newCost < dist[newNode]:
                        dist[newNode] = newCost + cost

                        heapq.heappush(queue, (dist[newNode], newNode))


            count = 0

            for city in range(n):
                if dist[city] != 0 and dist[city] <= distanceThreshold:
                    count += 1

            return count
        
        minV = float('inf')
        res = -1
        for i in range(n):
            value = solve(i, adj)
            minV = min(value, minV)
            if value == minV:
                res = i
                
        return res
