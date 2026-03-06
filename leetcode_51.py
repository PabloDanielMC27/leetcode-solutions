#51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        def check_valid(i, ds):

            n = len(ds)

            for col in range(n):
                if ds[col] == i:
                    return False

            for diagd in range(n):
                if ds[diagd] + diagd == i + n:
                    return False
            
            for diagu in range(n):
                if (n + i) - 2* (n - diagu) == ds[diagu] + diagu :
                    return False
            return True  

        def backtrack(idx, ds, n):
            if idx == n:
                arr =[]
                for row in self.ds2:
                    arr.append("".join(row))
                
                self.ans.append(list(arr))

            for i in range(n):
                if check_valid(i, ds):
                    ds.append(i)
                    self.ds2[i][len(ds) - 1] = "Q"
                    backtrack(idx + 1, ds, n)
                    self.ds2[i][len(ds) - 1] = "."
                    ds.pop()


        self.ans = []
        self.ds2 = [["."] * n for _ in range(n)]
        backtrack(0, [], n)

        return self.ans

        
