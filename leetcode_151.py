# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:

        arr = s.split()
        arr.reverse()
        return " ".join(arr)
        
