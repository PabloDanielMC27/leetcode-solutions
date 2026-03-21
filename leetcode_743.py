# 743. Network Delay Time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # #build adj list
        # adj = [[] for _ in range(n + 1)]
        # for time in times:
        #     adj[time[0]].append((time[1], time[2]))
        
        # # add dist vector
        # dist = [float('inf')] * (n + 1) 
        # dist[k] = 0

        # # generate queue
        # queue = deque()
        # queue.append((k, 0))

        # while queue:

        #     node, cost = queue.popleft()

        #     for neighbor in adj[node]:
        #         newNode = neighbor[0] 
        #         newCost = neighbor[1]

        #         if  cost + newCost < dist[newNode]:
        #             dist[newNode] = cost + newCost
        #             queue.append((newNode, dist[newNode]))

        # # check max value
        # maxV = 0
        # for i in range(1, n + 1):
        #     if dist[i] == float('inf'):
        #         return -1
            
        #     maxV = max(maxV, dist[i])
        
        # return maxV


        #build adj list
        adj = [[] for _ in range(n + 1)]
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        
        # add dist vector
        dist = [float('inf')] * (n + 1) 
        dist[k] = 0

        # generate queue
        queue = []
        heapq.heappush(queue, (0, k))

        while queue:

            cost, node = heapq.heappop(queue)

            if cost > dist[node]:
                continue

            for neighbor in adj[node]:
                newNode = neighbor[0] 
                newCost = neighbor[1]

                if  cost + newCost < dist[newNode]:
                    dist[newNode] = cost + newCost
                    heapq.heappush(queue, (dist[newNode], newNode))

        # check max value
        maxV = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            
            maxV = max(maxV, dist[i])
        
        return maxV



        
