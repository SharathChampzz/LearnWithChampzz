class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0 # entry itself blocked

        obstacleGrid[0][0] = 1

        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             obstacleGrid[i][j] = 'X'

        # if 

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    if i == 0 and j == 0:
                        continue
                    obstacleGrid[i][j] = 'X'

                sum = 0
                # [Top, Left]
                for x, y in [(i-1,j), (i,j-1)]:
                    if x >= 0 and y >= 0 and obstacleGrid[i][j] != 'X':
                        sum += obstacleGrid[x][y]

                obstacleGrid[i][j] = sum

        # print(obstacleGrid)

        return obstacleGrid[m-1][n-1]
