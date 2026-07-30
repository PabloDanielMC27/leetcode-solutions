# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # linear space
        # vers1 = version1.split(".")
        # vers2 = version2.split(".")

        # vers1 = [int(num) for num in vers1]
        # vers2 = [int(num) for num in vers2]

        # n1 = len(vers1)
        # n2 = len(vers2)
        
        # for i in range(max(n1, n2)):

        #     v1 = vers1[i] if i < n1 else 0
        #     v2 = vers2[i] if i < n2 else 0

        #     if v1 < v2:
        #         return -1
        #     elif v1 > v2:
        #         return 1

        # return 0  

        # constant space
        i = 0
        j = 0
        n1 = len(version1)
        n2 = len(version2)

  
        while i < n1 or j < n2:
            num1 = "0"
            while i < n1 and version1[i] != '.':
                num1 += version1[i] 
                i += 1
    
            num2 = "0"
            while j < n2 and version2[j] != '.':
                num2 += version2[j] 
                j += 1

            if int(num1) < int(num2):
                return -1
            elif int(num1) > int(num2):
                return 1

            i += 1
            j += 1

        return 0


            


        
