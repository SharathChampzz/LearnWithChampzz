class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # logic used: lets try to revisit non-visited/disconnected nodes again and again
        # the number of time, we revisit or try on disconnected nodes. We will get the province counts.
        
        n = len(isConnected)
        all_nodes = {i for i in range(n)}
        visited_node = set()
        
        province_count = 0

        # bfs using adjacent matrix
        def bfs(new_node):
            queue = deque([new_node])
            visited_node.add(new_node)

            while queue:
                node = queue.popleft()

                for index in range(n):
                    if index in visited_node or isConnected[node][index] == 0:
                        continue

                    queue.append(index)
                    visited_node.add(index)
                    all_nodes.remove(index)

        while all_nodes:
            start_node = all_nodes.pop()
            bfs(start_node)
            province_count += 1

        return province_count
