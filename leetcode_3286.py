# 3286. Find a Safe Walk Through a Grid

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        

        # #bfs
        # m = len(grid)
        # n = len(grid[0])

        # visited = [[-1]* n for _ in range(m)]
        # visited[0][0] = health - grid[0][0]

        # if visited[0][0] < 1:
        #     return False

        # queue =deque([(0, 0, visited[0][0])])

        # while queue:
        #     row, col, currHealth = queue.popleft()

        #     for delrow, delcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        #         nrow = delrow + row
        #         ncol = delcol + col

        #         if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
        #             newHealth = currHealth - grid[nrow][ncol]
        #             if newHealth > visited[nrow][ncol]:
        #                 if nrow == m - 1 and ncol == n - 1 and newHealth >= 1:
        #                     return True

        #                 queue.append((nrow, ncol, currHealth - grid[nrow][ncol]))
        #                 visited[nrow][ncol] = max(visited[nrow][ncol], newHealth)

        # return False


        #dijkstra
        m = len(grid)
        n = len(grid[0])

        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = health - grid[0][0]

        if visited[0][0] < 1:
            return False

        pqueue = []
        heapq.heappush(pqueue, (-visited[0][0], 0, 0))        

        while pqueue:
            currHealth, row, col = heapq.heappop(pqueue)
            currHealth = -currHealth

            if currHealth < visited[row][col]:
                    continue

            for delrow, delcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nrow = row + delrow
                ncol = col + delcol

                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
                    newHealth = currHealth - grid[nrow][ncol]
                    if nrow == m - 1 and ncol == n - 1 and newHealth >= 1:
                        return True
                    
                    if newHealth > visited[nrow][ncol]:
                        visited[nrow][ncol] = newHealth
                        heapq.heappush(pqueue, (-newHealth , nrow, ncol))
                        

        return False


        
