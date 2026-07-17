# 3619. Count Islands With Total Value Divisible by K

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        # dfs

        # def dfs(row, col, visited, n, m, total):
        #     total += grid[row][col]
        #     visited[row][col] = 1
        #     for delrow, delcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        #         nrow = delrow + row
        #         ncol = delcol + col

        #         if (nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] != 0 and visited[nrow][ncol] != 1):
        #             total = dfs(nrow, ncol, visited, n, m, total)
            
        #     return total

        # m = len(grid)
        # n = len(grid[0])

        # visited = [[0] * n for _ in range(m)]

        # counter = 0

        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] != 0 and visited[row][col] != 1:
        #             total = dfs(row, col, visited, n, m, 0)
        #             if (total % k == 0):
        #                 counter += 1

        # return counter


        # bfs

        def bfs(row, col, visited, n, m, total):
            total += grid[row][col]
            visited[row][col] = 1
            queue = deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()            
            
                for delrow, delcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nrow = delrow + row
                    ncol = delcol + col

                    if (nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] != 0 and visited[nrow][ncol] != 1):
                        visited[nrow][ncol] = 1
                        queue.append((nrow, ncol))

                        total += grid[nrow][ncol]
            
            return total

        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]

        counter = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0 and visited[row][col] != 1:
                    total = bfs(row, col, visited, n, m, 0)
                    if (total % k == 0):
                        counter += 1

        return counter
