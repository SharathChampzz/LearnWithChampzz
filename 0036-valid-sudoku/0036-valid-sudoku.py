class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we will maintain mapping for rows, columns and subbox, as we iterate through
        # so that we can directly check if the element is already present in row/column/subbox
        # instead of doing repeatitive iteration
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        subbox = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                
                if num in rows[i] or num in columns[j] or num in subbox[(i//3, j//3)]:
                    return False
                    
                rows[i].add(num)
                columns[j].add(num)
                subbox[(i//3, j//3)].add(num)
                # subboxes also like an 2-D array, we can represent (0,0)...(2,2)
                # as subboxes are split by 3-3-3 elements, divide by 3 and get quotient
                # getting quotient will get us the index of the subbox in 2D array

        return True

    def TempisValidSudoku(self, board: List[List[str]]) -> bool:
        
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