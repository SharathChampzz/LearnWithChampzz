class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_row(x,y):
            current_value = board[x][y]
            for i in range(9):
                if board[x][i] == current_value and i != y:
                    return False
            return True

        def check_column(x,y):
            current_value = board[x][y]
            for i in range(9):
                if board[i][y] == current_value and i != x:
                    return False
            return True

        def check_sub_box(x,y):
            current_value = board[x][y]
            start_box_x = (x//3)*3
            start_box_y = (y//3)*3

            for i in range(start_box_x, start_box_x+3):
                for j in range(start_box_y, start_box_y+3):
                    if board[i][j] == current_value and i!=x and j!=y:
                        return False
            return True

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if not check_row(x,y):
                    print(f'Check row failed for x:{x} and y:{y} == Duplicate => {board[x][y]}')
                    return False
                if not check_column(x,y):
                    print(f'Check column failed for x:{x} and y:{y} == Duplicate => {board[x][y]}')
                    return False
                if not check_sub_box(x,y):
                    print(f'Check subbox failed for x:{x} and y:{y} == Duplicate => {board[x][y]}')
                    return False

        return True