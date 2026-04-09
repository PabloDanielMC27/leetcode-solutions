# 2085. Count Common Words With One Occurrence

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        dict1 = Counter(words1)
        dict2 = Counter(words2)

        count = 0
        for word in words2:
            if dict1[word] == 1 and dict2[word] == 1:
                count += 1
        return count
    
        
