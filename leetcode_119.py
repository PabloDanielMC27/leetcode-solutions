# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        store = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            level_arr = [1]
            for j in range(1, i):
                level_arr.append(store[i - 1][j - 1] + store[i - 1][j])
            level_arr.append(1)
            store.append(level_arr)
        
        return store[-1]

        
