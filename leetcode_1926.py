# 1926. Nearest Exit from Entrance in Maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:

            row, col, time = queue.popleft()
            for delrow, delcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nrow = delrow + row
                ncol = delcol + col

                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and (nrow, ncol) not in visited and maze[nrow][ncol] == ".":
                    if (nrow == 0 or nrow == m - 1 or ncol == 0 or ncol == n - 1):
                        return time + 1
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol, time + 1)) 

        return -1
