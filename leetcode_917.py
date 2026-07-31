# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        arr = list(s)
        while l < r:
            if arr[l].isalpha() and arr[r].isalpha():
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

            elif arr[l].isalpha():
                r -= 1
            else:
                l += 1

        return "".join(arr)
        
