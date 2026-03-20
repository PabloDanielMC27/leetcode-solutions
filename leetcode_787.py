#787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]

        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
    
        dist = [float('inf')] * n

        queue = deque()
        queue.append((0, src, 0))

        while queue:
            stops, node, cost = queue.popleft()

            if stops > k:
                continue

            for neighbor in adj[node]:
                if cost + neighbor[1] < dist[neighbor[0]] and stops <= k:
                    dist[neighbor[0]] = cost + neighbor[1]
                    queue.append((stops + 1, neighbor[0], cost + neighbor[1]))
        

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]

        

        
        
