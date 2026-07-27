# 841. Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        visited.add(0)

        queue = deque(rooms[0])
  
        while queue:
            key = queue.popleft()
            if key not in visited:
                visited.add(key)
                for new_key in rooms[key]:
                    if new_key not in visited:
                        queue.append(new_key)

        return len(visited) == len(rooms)
        
