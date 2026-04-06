# 207. Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # # kahn's algorithm

        # #create adj list
        # adj = [[] for _ in range(numCourses)]
        # for end, start in prerequisites:
        #     adj[start].append(end)

        # # build indegree vector
        # indegree = [0] * numCourses
        
        # # populate indegree vector
        # for course in adj:
        #     for end in course:
        #         indegree[end] += 1

        # # fill queue
        # queue = deque()
        # counter = 0
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        #         counter += 1

        # while queue:
        #     course = queue.popleft()

        #     for neighbor in adj[course]:
        #         indegree[neighbor] -= 1

        #         if indegree[neighbor] == 0:
        #             queue.append(neighbor)
        #             counter += 1
        
        # return counter == numCourses

        # topo sort using dfs

        # build inverted adj list
        adj = [[] for _ in range(numCourses)]
        for end, start in prerequisites:
            adj[start].append(end)

        # build visited/in process vector 
        visited = [0] * numCourses

        def dfs(course, adj, visited):

            # in process
            if visited[course] == 1:
                # cycle
                return False

            # visited
            if visited[course] == 2:
                return True

            visited[course] = 1

            for neighbor in adj[course]:
                if not dfs(neighbor, adj, visited):
                    return False

            visited[course] = 2
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                #not visited
                if not dfs(course, adj, visited):
                    return False

        return True
            

    






        
