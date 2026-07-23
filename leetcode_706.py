# 706. Design HashMap

class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.boxes = 1000
        self.arr = [Node() for _ in range(self.boxes)]

    def put(self, key: int, value: int) -> None:
        box = key % self.boxes
        node = self.arr[box]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        box = key % self.boxes
        node = self.arr[box]
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        box = key % self.boxes
        node = self.arr[box]
        while node.next:
            if node.next.key == key:
                dummy = node.next
                node.next = node.next.next
                dummy.next = None
                return
            node = node.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
