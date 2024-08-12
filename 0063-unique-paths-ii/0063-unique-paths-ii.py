class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0 # entry itself blocked

        # iterate and mark blockages as 'X'
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 'X'

        # base case
        obstacleGrid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue # skip this is already set

                sum = 0
                # [Top, Left]
                for x, y in [(i-1,j), (i,j-1)]:
                    if x >= 0 and y >= 0 and obstacleGrid[i][j] != 'X':
                        sum += obstacleGrid[x][y]

                obstacleGrid[i][j] = sum

        return obstacleGrid[m-1][n-1]
