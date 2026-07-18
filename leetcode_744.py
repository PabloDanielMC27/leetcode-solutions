# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # brute force
        # target = ord(target)

        # for letter in letters:
        #     if ord(letter) > target:
        #         return letter
        # return letters[0]
        

        # binary search
        target = ord(target)

        l = 0
        r = len(letters) - 1
        ans = 'a'
        while l <= r:
            mid = (r - l) // 2 + l
            if ord(letters[mid]) > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans if l != len(letters) else letters[0]
