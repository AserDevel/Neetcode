class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_flag = True
        column_flag = True
        box_flag = True

        #check if all rows are valid
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for k in range(j+1,9):
                        if board[i][j] == board[i][k]:
                            row_flag = False
        
        #check if all columns are valid
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    for k in range(j+1,9):
                        if board[j][i] == board[k][i]:
                            column_flag = False

        #check if all boxes are valid
        for i in range(9):
            if i < 3:
                x = i*3
                y = 0
            elif i < 6:
                x = (i-3)*3
                y = 3
            else:
                x =(i-6)*3
                y = 6
            for j1 in range(3):
                for k1 in range(3):
                    if board[j1+x][k1+y] != '.':
                        for j2 in range(j1+1, 3):
                            for k2 in range(k1+1, 3):
                                if board[j1+x][k1+y] == board[j2+x][k2+y]: 
                                    box_flag = False
        
        if box_flag & row_flag & column_flag: return True
        else: return False