# 2101. Detonate the Maximum Bombs

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # self.max = 0

        # def dfs(bomb):

        #     counter = 0
        #     exploded = 0

        #     self.visited[bomb] = 1

        #     x_pos = bombs[bomb][0]
        #     y_pos = bombs[bomb][1]

        #     for i in range(self.n):
        #         if i != bomb and self.visited[i] == 0:
        #             x_pos2 = bombs[i][0]
        #             y_pos2 = bombs[i][1]
        #             distance = ((x_pos - x_pos2)**2 + (y_pos - y_pos2)**2)
        #             radius = bombs[bomb][2]
        #             if distance <= (radius * radius):
        #                 counter += 1
        #                 val = dfs(i)
        #                 exploded = max(exploded, val)
                    
        #     return exploded + counter

        # self.n = len(bombs)
        # for i in range(self.n):
        #     self.visited = [0] * self.n
        #     dfs(i)
        #     self.max = max(self.max, sum(self.visited))
  
        # return self.max
        
        # more efficient version 
        def dfs(bomb):

            counter = 0
            exploded = 0

            self.visited[bomb] = 1
            for neighbor in self.adj[bomb]:
                if self.visited[neighbor] == 0: 
                    dfs(neighbor)
                    
        # calculate distances once
        self.n = len(bombs)
        self.adj = [[] for _ in range(self.n)]
        for i in range(self.n):
            x_pos = bombs[i][0]
            y_pos = bombs[i][1]
            radius = bombs[i][2]
            for j in range(self.n):
                if i != j:
                    x_pos2 = bombs[j][0]
                    y_pos2 = bombs[j][1]
                    distance = ((x_pos - x_pos2)**2 + (y_pos - y_pos2)**2)
                    if distance <= radius * radius:
                        self.adj[i].append(j)

        self.max = 0
        for i in range(self.n):
            self.visited = [0] * self.n
            dfs(i)
            self.max = max(self.max, sum(self.visited))
   
        return self.max
        
