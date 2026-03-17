#146. LRU Cache

class Node:
    def __init__(self, val = 0, key = 0):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val
            
                

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
            self.capacity += 1

        newNode = Node(value, key)
        self.insert(newNode)
        self.capacity -= 1
        self.cache[key] = newNode

        if self.capacity < 0:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
            self.capacity += 1

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
