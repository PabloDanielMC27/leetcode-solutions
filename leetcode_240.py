# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # n log m solution
        # for row in range(len(matrix)):
            
        #     # search in row
        #     l = 0
        #     r = len(matrix[0]) - 1
        #     while l <= r:
        #         mid = (r - l) // 2 + l
        #         if matrix[row][mid] == target:
        #             return True
        #         elif matrix[row][mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1

        # return False

        # n + m solution
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False 
            

