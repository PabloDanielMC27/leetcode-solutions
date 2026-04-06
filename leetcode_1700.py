# 1700. Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        n = len(students)
        stu_queue = deque(students)
        queue = deque(sandwiches)
        
        count = 0
        while True:
            if queue[0] == stu_queue[0]:
                #valid
                queue.popleft()
                stu_queue.popleft()
                n -= 1
                count = 0

            else:
                student = stu_queue.popleft()
                stu_queue.append(student)
                count += 1

            if count == n:
                return n
            

        
