# 3242. Design Neighbor Sum Service

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        
        m = len(grid)
        n = len(grid[0])
        self.d = {}

        self.values = [[0] * n for _ in range(m)]
        self.diagValues = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):

                self.d[grid[row][col]] = (row, col)

                # adjNeighbor sum
                for delrow, delcol in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                    nrow = delrow + row
                    ncol = delcol + col

                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
                        self.values[row][col] += grid[nrow][ncol]
                       
                # diagNeighbor sum
                for delrow, delcol in [(-1,-1), (1, -1), (1, 1), (-1, 1)]:
                    nrow = delrow + row
                    ncol = delcol + col

                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
                        self.diagValues[row][col] += grid[nrow][ncol]


    def adjacentSum(self, value: int) -> int:
        row, col = self.d[value]
        return self.values[row][col]
        

    def diagonalSum(self, value: int) -> int:
        row, col = self.d[value]
        return self.diagValues[row][col]
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
