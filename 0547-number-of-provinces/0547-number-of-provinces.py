class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(start_node: int):
            queue = deque([start_node])
            visited[start_node] = True

            while queue:
                node = queue.popleft()
                for neighbor in range(n):
                    if not visited[neighbor] and isConnected[node][neighbor] == 1:
                        queue.append(neighbor)
                        visited[neighbor] = True

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for i in range(n):
            if not visited[i]:
                bfs(i)
                province_count += 1

        return province_count