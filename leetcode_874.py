# 874. Walking Robot Simulation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        obs_set = set()
        for (x, y) in obstacles:
            obs_set.add((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # n, e, s, w 
        idx = 0

        x, y = 0, 0
        maxV = 0

        for command in commands:
            if command == -1:
                # turn right
                idx = (idx + 1) % 4
            if command == -2:
                # turn left
                idx = (idx - 1) % 4
    
            else:
                # move
                for _ in range(command):
                    nx = x + directions[idx][0]
                    ny = y + directions[idx][1]

                    if (nx, ny) in obs_set:
                        break
                    x = nx
                    y = ny
                    maxV = max(maxV, x * x + y * y)
                
        return maxV

