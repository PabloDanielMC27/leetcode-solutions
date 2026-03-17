# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        
        # summ = 0

        # while True:
        #     num_str = str(num)
            
        #     for c in num_str:
        #         summ += int(c)
            
        #     print(summ)
        #     if summ < 10:
        #         return summ
        #     else:
        #         num = summ
        #         summ = 0
        
        
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9

        return num % 9
