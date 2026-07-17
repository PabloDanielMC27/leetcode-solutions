# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        total = 0

        for row in grid:
            l = 0
            r = len(grid[0]) - 1
        
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            
            total += len(grid[0]) - max(l, r)
        
        return total
