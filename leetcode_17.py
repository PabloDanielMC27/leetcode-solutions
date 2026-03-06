#17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"

        }
        

        def backtrack(idx, ds):
            
            if (len(ds) == self.n):
                self.ans.append("".join(ds))
                return

            for i in range(len(d[digits[idx]])):
                ds.append(d[digits[idx]][i])
                backtrack(idx + 1, ds)
                ds.pop()

        self.n = len(digits)
        self.ans = []
        backtrack(0, [])
        return self.ans


        




        
