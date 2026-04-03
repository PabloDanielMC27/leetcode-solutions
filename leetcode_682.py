# 682. Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # stack = []

        # for op in operations:
        #     if op[-1].isnumeric():
        #         stack.append(int(op))
            
        #     elif op == "C":
        #         stack.pop()
            
        #     elif op == "D":
        #         stack.append(stack[-1] * 2)

        #     elif op == "+":
        #         top = stack.pop()
        #         summ = top + stack[-1]
        #         stack.append(top)
        #         stack.append(summ)

        # total = 0
        # for num in stack:
        #     total += num

        # return total

        # single pass

        stack = []
        total = 0

        for op in operations:
            if op[-1].isnumeric():
                num = int(op)
                stack.append(num)
                total += num
            
            elif op == "C":
                total -= stack[-1]
                stack.pop()
                 
            elif op == "D":
                mult = stack[-1] * 2
                total += mult
                stack.append(mult)

            elif op == "+":
                top = stack.pop()
                summ = top + stack[-1]
                total += summ
                stack.append(top)
                stack.append(summ)

        return total
        
