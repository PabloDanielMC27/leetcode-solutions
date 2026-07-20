# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # search row
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        row = mid
        
        # search column
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (r - l) // 2 + l

            if matrix[row][mid] == target:
                return True
            
            if matrix[row][l] <= target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
