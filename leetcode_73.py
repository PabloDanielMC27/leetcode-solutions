# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        # O(nm) space
        # def markcell(row, col, visited, n, m):
        #     minus_x = col
        #     while minus_x >= 0:
        #         matrix[row][minus_x] = 0
        #         visited[row][minus_x] = 1
        #         minus_x -= 1

        #     plus_x = col
        #     while plus_x < n:
        #         matrix[row][plus_x] = 0
        #         visited[row][plus_x] = 1
        #         plus_x += 1

        #     minus_y = row
        #     while minus_y >= 0:
        #         matrix[minus_y][col] = 0
        #         visited[minus_y][col] = 1
        #         minus_y -= 1

        #     plus_y = row
        #     while plus_y < m:
        #         matrix[plus_y][col] = 0
        #         visited[plus_y][col] = 1
        #         plus_y += 1

        
        # m = len(matrix)
        # n = len(matrix[0])

        # visited = [[0] * n for _ in range(m)]

        # queue = deque([])

        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col] == 0:
        #             visited[row][col] = 1
        #             queue.append((row,col))

        # while queue:
        #     row, col = queue.popleft()

        #     markcell(row, col, visited, n, m)

        # O(n + m) space               
        # m = len(matrix)
        # n = len(matrix[0])

        # rows = []
        # cols = [] 

        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col] == 0:
        #             rows.append(row)
        #             cols.append(col)

        # for row in range(m):
        #     for col in range(n):
        #         if row in rows or col in cols:
        #             matrix[row][col] = 0

        # O(1) space
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # first row has zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # first column has zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # fill with zeros based on first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


