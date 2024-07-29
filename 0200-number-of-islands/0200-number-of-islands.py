class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Counts the number of islands in a given grid.

        Args:
            grid: A matrix of characters representing the grid, where '1'
                represents land and '0' represents water.

        Returns:
            The number of islands in the grid.
        """

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        visited = set()

        def get_valid_neighbors(row, col):
            """Gets valid neighbors for a given cell.

            Args:
                row: The row index of the cell.
                col: The column index of the cell.

            Returns:
                A list of tuples representing valid neighbor coordinates.
            """

            neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, top, left, bottom
            valid_neighbors = []

            for dr, dc in neighbors:
                new_row, new_col = row + dr, col + dc

                # Check boundaries
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                # Check if already visited or water
                if (new_row, new_col) in visited or grid[new_row][new_col] == "0":
                    continue

                valid_neighbors.append((new_row, new_col))

            return valid_neighbors

        def bfs(row, col):
            """Performs breadth-first search to mark an island as visited.

            Args:
                row: The starting row of the island.
                col: The starting column of the island.
            """

            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()
                for nr, nc in get_valid_neighbors(r, c):
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    island_count += 1

        return island_count 
