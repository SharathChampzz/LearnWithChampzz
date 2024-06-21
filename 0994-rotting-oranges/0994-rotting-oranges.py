class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        # [(x,y, steps), ()]
        steps = 0 # minutes
        rotten_locations = [(i, j, steps) for i in range(row) for j in range(column) if grid[i][j] == 2] # handling multiple rotten oranges
        # add all the rotten oranges and as we are maintaining step counts. Each rotten will have its own step count.
        # It kinda acts as multiple threads evaluating nodes at the same time.
        # but in reality, node1..noden will be evaluating in their turns and gets equal chances
        queue = deque(rotten_locations)

        visited_nodes = set()
        visited_nodes.update(rotten_locations)

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            rotten_x, rotten_y, steps = queue.popleft()

            for x, y in directions:
                neighbour_x, neighbour_y = rotten_x + x, rotten_y + y
                # print(f'Cheecking if valid: {neighbour_x},{neighbour_y}: {(neighbour_x, neighbour_y) in visited_nodes}, {neighbour_x > row-1 or neighbour_y > column-1}')

                if (neighbour_x, neighbour_y) in visited_nodes:
                    continue # already visited

                if neighbour_x > row-1 or neighbour_y > column-1 or neighbour_x < 0 or neighbour_y < 0:
                    continue # list overflow indexes

                if grid[neighbour_x][neighbour_y] != 1:
                    continue  # it is not fresh or it might be empty, so ignore

                # when we add it to the queue make sure to make it as routen
                print(f'New rotten cords: ({neighbour_x},{neighbour_y}) and steps will be {steps+1}')
                grid[neighbour_x][neighbour_y] = 2

                queue.append((neighbour_x, neighbour_y, steps + 1))
                visited_nodes.add((neighbour_x, neighbour_y))

        # check if any fresh oranges still present
        fresh_status = any([grid[i][j] == 1 for i in range(row) for j in range(column)])

        if fresh_status:
            return -1

        return steps
        
