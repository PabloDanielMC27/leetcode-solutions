# 1472. Design Browser History

class Node:
    def __init__(self, page = ""):
        self.prev = None
        self.next = None
        self.page = page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.head = Node()
        self.tail = Node()
        node = Node(homepage)
        node.prev = self.head
        node.next = self.tail

        self.head.next = node
        self.tail.prev = node
        self.curr = node
        
    def visit(self, url: str) -> None:
    
    
        node = Node(url)
        node.next = self.tail
        node.prev = self.curr
        self.tail.prev = node
        self.curr.next = node

        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr.prev != self.head and steps!= 0:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.page

        

    def forward(self, steps: int) -> str:
        while self.curr.next != self.tail and steps != 0:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
