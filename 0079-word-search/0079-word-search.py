class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        result_len = len(word)

        def search(i, j, index):
            if index >= result_len:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = search(i + 1, j + 0, index + 1) or \
                    search(i + 0, j + 1, index + 1) or \
                    search(i - 1, j + 0, index + 1) or \
                    search(i + 0, j - 1, index + 1)

            board[i][j] = temp
            
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(i, j, 0):
                    return True

        return False