# 1670. Design Front Middle Back Queue

class Node:
    def __init__(self, value = 0):
        self.prev = None
        self.next = None
        self.val = value

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        

    def pushFront(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

        self.count += 1
        
    def pushMiddle(self, val: int) -> None:
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        node = Node(val)
        if fast.next:
            node.next = slow.next
            node.prev = slow
            node.prev.next = node
            node.next.prev = node
        else:
            node.next = slow
            node.prev = slow.prev
            node.next.prev = node
            node.prev.next = node 

        self.count += 1       

    def pushBack(self, val: int) -> None:
        node = Node(val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev.next = node
        
        self.count += 1
        
    def popFront(self) -> int:

        if self.count >= 1:
            node = self.head.next
            self.head.next = node.next
            node.next.prev = self.head

            node.next = None
            node.prev = None

            self.count -= 1
            return node.val
        return -1

    def popMiddle(self) -> int:
        if self.count >= 1:
            slow = fast = self.head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            slow.prev.next = slow.next
            slow.next.prev = slow.prev

            slow.next = None
            slow.prev = None           
         
            self.count -= 1
            return slow.val
        return -1
        
    def popBack(self) -> int:
        if self.count >= 1:
            node = self.tail.prev
            self.tail.prev = node.prev
            node.prev.next = self.tail

            node.prev = None
            node.next = None

            self.count -= 1
            return node.val
        return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
