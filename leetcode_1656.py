# 1656. Design an Ordered Stream

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * n
        self.pos = 0
        self.n = n   

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.arr[idKey - 1] = value

        while self.pos < self.n and self.arr[self.pos] != "":
            ans.append(self.arr[self.pos])
            self.pos += 1
        return ans
