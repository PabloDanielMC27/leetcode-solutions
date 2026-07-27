# 3898. Find the Degree of Each Vertex

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        ans = []
        for node in matrix:
            ans.append(sum(node))
        return ans

        
        
