class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]:
            return 0 # entry or exit are blocked

        # set base case
        obstacleGrid[0][0] = 1
        
        # iterate through the grid and take sum from top and left
        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    continue # ignore base index
                    
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 'X' # mark it as blocked
                    continue

                cords = [(i-1,j), (i,j-1)] # [Top, Left]
                
                for x, y in cords:
                    if x >= 0 and y >= 0 and obstacleGrid[x][y] != 'X':
                        obstacleGrid[i][j] += obstacleGrid[x][y]

        return obstacleGrid[m-1][n-1] # return the end total
