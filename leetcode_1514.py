# 1514. Path with Maximum Probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        # build adj list
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))

        # build dist array
        dist =[0] *n
        dist[start_node] = -1 

        # generate priority queue
        pqueue = [] 
        heapq.heappush(pqueue, (dist[start_node], start_node))

        while pqueue:
            prob, node = heapq.heappop(pqueue)
            prob = -prob
            
            if prob < dist[node]:
                continue

            for newNode, newProb in adj[node]:
                if prob * newProb > dist[newNode]:
                    dist[newNode] = prob * newProb
                    heapq.heappush(pqueue, (-dist[newNode], newNode))
            
            print(pqueue)

        return dist[end_node]
        
