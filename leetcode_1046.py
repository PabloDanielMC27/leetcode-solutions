# 1046. Last Stone Weight

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stone_cpy = [(-1)*val for val in stones]
        heapify(stone_cpy)

        while len(stone_cpy) > 1:
            stone1 = heapq.heappop(stone_cpy)
            stone2 = heapq.heappop(stone_cpy)

            if stone1 < stone2:
                heapq.heappush(stone_cpy, stone1 - stone2)
            
        return 0 if not stone_cpy else (-1) * stone_cpy[0]


        
