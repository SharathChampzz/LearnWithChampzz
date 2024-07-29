class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return
            
            board[i][j] = 'S'

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        # perform calculation for corners rows and columns
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O': # or simply we can update everything else to 'X' that works 
                    board[i][j] = 'X'
