#705. Design HashSet

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.boxes = 1000
        self.values = [None] * self.boxes

    def add(self, key: int) -> None:
        
        box = key % self.boxes
        
        curr = self.values[box]
        if not curr:
            self.values[box] = Node(key)
            return
        
        while True:
            if curr.val == key:
                return
            
            if not curr.next:
                break
            
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        
        box = key % self.boxes
        curr = self.values[box]
        prev = None
        while curr:
            if curr.val == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.values[box] = curr.next
                return
            
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        
        box = key % self.boxes
        curr = self.values[box]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
