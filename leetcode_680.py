# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:

        # recursion - linear space
        # def areEqual(l, r, checked):
        #     if l >= r:
        #         return True
        #     if s[l] == s[r]:
        #         return areEqual(l + 1, r - 1, checked)

        #     else:
        #         if checked:
        #             return False
        #         else:
        #             return areEqual(l + 1, r, True) or areEqual(l, r - 1, True)

        # l = 0
        # r = len(s) - 1
        # return areEqual(l, r, False)

        # two pointer - constant space
        def areEqual(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return areEqual(l + 1, r) or areEqual(l, r - 1)
            l += 1
            r -= 1

        return True
