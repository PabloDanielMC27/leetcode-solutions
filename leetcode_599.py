# 599. Minimum Index Sum of Two Lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d = defaultdict()

        for i, word in enumerate(list1):
            d[word] = i

        maxV = float('-inf')
        for i, word in enumerate(list2):
            if word in d:
                d[word] += i
                d[word] *= -1
                maxV = max(maxV, d[word])
        
        ans = []
        for key, value in d.items():
            if value == maxV:
                ans.append(key)

        return ans
              
   
