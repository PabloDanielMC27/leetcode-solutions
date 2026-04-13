# 1282. Group the People Given the Group Size They Belong To

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        # single pass
        ans = []
        groups = defaultdict(list)
        for i, value in enumerate(groupSizes):

            if len(groups[value]) < value:
                groups[value].append(i)   
            
            if len(groups[value]) == value:
                ans.append(groups[value])
                groups[value] = []

        return ans
