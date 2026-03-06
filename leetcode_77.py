#77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        def backtrack(start, ds):
            if len(ds) == k:
                self.ans.append(list(ds))
                return 

           
            for i in range(start, n + 1):
                ds.append(i)
                backtrack(i + 1, ds)
                ds.pop()



        self.ans = []
        backtrack(1,[])
        return self.ans
