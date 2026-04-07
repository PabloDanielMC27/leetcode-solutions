# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # # kahn's algorithm

        # # create indegree vector
        # indegree = [0] * numCourses

        # #build adj list
        # adj = [[] for _ in range(numCourses)]
        # for end, start in prerequisites:
        #     adj[start].append(end)
        #     indegree[end] += 1

        # # add courses with indegree = 0 to queue
        # queue = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)

        # ans = []
        # courseCounter = 0
        # while queue:
        #     course = queue.popleft()
        #     ans.append(course)
        #     courseCounter += 1

        #     for nextCourse in adj[course]:
        #         indegree[nextCourse] -= 1
        #         if indegree[nextCourse] == 0:
        #             queue.append(nextCourse)

        # if courseCounter == numCourses:
        #     return ans
        # return []
        

        # dfs

        # #build adj list
        adj = [[] for _ in range(numCourses)]
        for end, start in prerequisites:
            adj[start].append(end)

        # build visited array
        visited = [0] * numCourses

        def dfs(course, adj, ans):

            if visited[course] == 1:
                return False # cycle
            
            if visited[course] == 2:
                return True

            visited[course] = 1

            for neighbor in adj[course]:
                if not dfs(neighbor, adj, ans):
                    return False
            
            visited[course] = 2
            ans.append(course)
            return True

        ans = []
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course, adj, ans):
                    return []
        
        ans.reverse()
        return ans


    
        
    
        
