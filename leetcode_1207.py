# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d = defaultdict()
        for num in arr:
            d[num] = d.get(num, 0) + 1

        st = set()
        for num in list(d.values()):
            if num not in st:
                st.add(num)
            else:
                return False
        return True
        
