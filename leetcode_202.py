# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:

        # brute force

        # visited = set()
        
        # while True:
        #     summ = 0

        #     while n != 0:
            
        #         d = n % 10
        #         n //= 10

        #         summ += d**2

        #     n = summ
        #     if n == 1:
        #         return True

        #     if n in visited:
        #         return False
        #     visited.add(n)
            
        # cycle detection

        def nextt(num):
            summ = 0
            while num != 0:
                d = num % 10
                num //= 10
                summ += d**2

            return summ


        slow = n
        fast = nextt(n)

        while fast != 1 and slow != fast:
            slow = nextt(slow)
            fast = nextt(nextt(fast))
        return fast == 1

        
