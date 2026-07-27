# 208. Implement Trie (Prefix Tree)

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if not child:
                child = node.children[ord(letter) - ord('a')] = Node()
            node = child
        node.end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if not child:
                return False
            node = child
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            child = node.children[ord(letter) - ord('a')]
            if not child:
                return False
            node = child
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
