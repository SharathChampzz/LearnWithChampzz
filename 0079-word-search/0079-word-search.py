class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        result_len = len(word)

        def search(i, j, index, visited):
            if index >= result_len:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or board[i][j] != word[index]:
                return False

            index += 1
            visited.append((i, j))

            path = [
            search(i + 1, j + 0, index, visited),
            search(i + 0, j + 1, index, visited),
            search(i - 1, j + 0, index, visited),
            search(i + 0, j - 1, index, visited)
            ]

            index -= 1
            visited.remove((i, j))

            return any(path)

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                found = search(i, j, 0, [])
                # print(f'Anaylsed for ({i}, {j}).. Result is {found}')
                if found:
                    return True

        return False