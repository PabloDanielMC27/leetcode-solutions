# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        if numRows >= 2:
            ans.append([1, 1])

        for i in range(3, numRows + 1):
            level_arr = [1]
            for j in range(1, i - 1):
                level_arr.append(ans[i - 2][j - 1] + ans[i - 2][j])
            level_arr.append(1)
            ans.append(level_arr)                

        return ans
        

        
