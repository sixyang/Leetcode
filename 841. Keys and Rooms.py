class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque()
        queue.append(rooms[0])
        visited = {0,}
        while queue:
            for _ in range(len(queue)):
                room = queue.popleft()
                for j in room:
                    if j not in visited:
                        visited.add(j)
                        queue.append(rooms[j])
        return True if visited == set(range(len(rooms))) else False
