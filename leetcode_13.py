# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        equiv = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s) - 1, -1, -1):
            current_pos = equiv[s[i]]
            if current_pos < total and s[i] != s[i + 1]:
                total -= current_pos
            else:
                total += current_pos
        return total
           


        
