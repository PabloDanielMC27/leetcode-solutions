# 211. Design Add and Search Words Data Structure

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if not child:
                child = node.children[ord(letter) - ord('a')] = Node()
            node = child
        node.end = True   

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)
  
    def dfs(self, idx, word, node):
        if idx == len(word):
            return node.end

        if word[idx] != '.':
            pos = ord(word[idx]) - ord('a')
            if node.children[pos]:
                return self.dfs(idx + 1, word, node.children[pos])
            return False
        else:
            for child in node.children:
                if child:
                    if self.dfs(idx + 1, word, child):
                        return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
