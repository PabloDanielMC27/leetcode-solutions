# 2073. Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        #O (n * len(tickets[k])) solution
        
        # n = tickets[k]
        # time = 0

        # queue = deque(tickets)

        # while n != 0:

        #     time += 1

        #     if k == 0:
        #         n -= 1
        #         k = len(queue) - 1

        #         if n == 0: 
        #             break
        #     else:
        #         k -= 1

        #     new_number = queue.popleft()
        #     if new_number - 1 > 0:
        #         queue.append(new_number - 1)

        # return time


        # O(n) solution
        n = len(tickets)

        time = 0

        for i in range(n):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time
