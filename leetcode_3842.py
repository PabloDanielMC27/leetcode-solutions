# 3842. Toggle Light Bulbs

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        st = set()
        for bulb in bulbs:
            if bulb not in st:
                st.add(bulb)
            else:
                st.remove(bulb)

        return sorted(st)
        
