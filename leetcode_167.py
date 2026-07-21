# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # brute force
        # for i, num in enumerate(numbers):
        #     for j, num2 in enumerate(numbers):
        #         if i == j:
        #             continue
        #         if num + num2 == target:
        #             return [i + 1, j + 1]

        # two pointers
        i = 0
        j = len(numbers) - 1

        while i < j:  
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            
            elif total > target:
                j -= 1
            elif total < target:
                i += 1
