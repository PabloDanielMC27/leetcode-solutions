# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        new_mat = [[-1] * c for _ in range(r)]

        for row in range(m):
            for col in range(n):
                idx = row * n + col
                new_mat[idx // c][idx % c] = mat[row][col]

        return new_mat
