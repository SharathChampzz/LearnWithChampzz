class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # logic used: lets try to revisit non-visited/disconnected nodes again and again
        # the number of time, we revisit or try on disconnected nodes. We will get the province counts.
        
        visited_node = set()

        # bfs using adjacent matrix
        def bfs(new_node):
            queue = deque([new_node])
            visited_node.add(new_node)

            while queue:
                node = queue.popleft()

                for index, neighbour in enumerate(isConnected[node]):
                    if index in visited_node or neighbour == 0:
                        continue

                    queue.append(index)
                    visited_node.add(index)
                    all_nodes.remove(index)

        n = len(isConnected)
        all_nodes = {i for i in range(n)}

        province_count = 0
        while all_nodes:
            start_node = all_nodes.pop()
            bfs(start_node)
            province_count += 1

        return province_count
