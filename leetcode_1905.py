# 1905. Count Sub Islands

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def bfs(row, col, m, n):

            queue = deque([(row, col)])
           
            self.visited[row][col] = 1
            marker = True

            while queue:
                row, col = queue.popleft()
                marker = marker and grid1[row][col]
                for delrow, delcol in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                    nrow = delrow + row
                    ncol = delcol + col

                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid2[nrow][ncol] == 1 and self.visited[nrow][ncol] == 0:
                        self.visited[nrow][ncol] = 1
                        queue.append((nrow, ncol))
                    
            return marker

        m = len(grid1)
        n = len(grid1[0])
        self.visited = [[0] * n for _ in range(m)]

        count = 0
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and self.visited[row][col] == 0:
                    if bfs(row, col, m, n):
                        count += 1

        return count

        
        
