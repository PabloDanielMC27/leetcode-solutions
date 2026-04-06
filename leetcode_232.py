# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack2:
            return len(self.stack) == 0
        return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
