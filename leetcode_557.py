# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.split(" ")
        ans = []
        for word in arr:
            word = word[::-1]
            ans.append("".join(word))

        return " ".join(ans)
