# 648. Replace Words

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Node()
        for word in dictionary:
            self.addWord(word, root)

        sentenceAsList = sentence.split(" ")
        ans = []
        for word in sentenceAsList:
            newWord = self.runTrie(word, root)
            ans.append(newWord)
        return " ".join(ans)

    def addWord(self, word, root):
        node = root
        for letter in word:
            pos = ord(letter) - ord('a')
            if not node.children[pos]:
                node.children[pos] = Node()
            node = node.children[pos]
        node.end = True

    def runTrie(self, word, root):
        node = root
        ans = ""
        for letter in word:
            pos = ord(letter) - ord('a')
            if node.children[pos]:
                ans += letter
                node = node.children[pos]
            elif not node.end:
                return word
            if node.end:
                return ans
        return word
