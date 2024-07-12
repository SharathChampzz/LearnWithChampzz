class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m # initialize 2D board with size m*n 

        # now build the possible combination board
        # idea is, you can reach to the point only from top or from left. 
        # so, if we are already know in how many ways we can reach to the top location and left location
        # we can simply take sum of it to get the current location possiblity
        # total_possible_ways (x,y) = arr[x-1][y] (top) + arr[x][y-1] (bottom)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue # This is already set

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

    def uniquePathsUsingRecursion(self, m: int, n: int) -> int:
        result = 0

        def make_move(current_x, current_y):
            nonlocal result

            # check if current_x and current_y are valid
            if current_x > m or current_y > n:
                return # overflow

            # check if we reached the destination
            if current_x == m and current_y == n:
                result += 1
                return

            # move down
            make_move(current_x + 1, current_y)
            
            # move right
            make_move(current_x, current_y + 1)

        make_move(1, 1)

        return result
