# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def bfs():

            queue = deque()
            queue.append((sr,sc))
            self.ans[sr][sc] = color

            while queue:

                row, col = queue.popleft()

                for drow, dcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nrow = row + drow
                    ncol = col + dcol

                    if nrow >= 0 and nrow < self.n and ncol >= 0 and ncol < self.m \
                      and image[nrow][ncol] == image[row][col] and self.ans[nrow][ncol] != color:
                        self.ans[nrow][ncol] = color
                        queue.append((nrow, ncol))  


        self.n = len(image)
        self.m = len(image[0])

        self.ans = [[-1] * self.m for _ in range(self.n)]

        for row in range(self.n):
            for col in range(self.m):
                self.ans[row][col] = image[row][col]

        bfs()
        return self.ans

        
