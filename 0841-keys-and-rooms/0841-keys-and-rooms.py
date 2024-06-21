class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # bfs approach
        start_node = 0 # starting room is empty
        visited_nodes = set()
        visited_nodes.add(start_node)

        queue = deque([start_node])

        while queue:
            node = queue.popleft()

            for neighbor_node in rooms[node]:
                if neighbor_node not in visited_nodes:
                    queue.append(neighbor_node)
                    visited_nodes.add(neighbor_node)

        return len(visited_nodes) == len(rooms) # check if all rooms are visited

        

