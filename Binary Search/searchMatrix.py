class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            midRow = (bot + top) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1            
            else:
                break
        else:
            return False    

        midRow = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            midCol = (r + l) // 2
            if target == matrix[midRow][midCol]:
                return True
            elif target < matrix[midRow][midCol]:
                r = midCol - 1
            else:
                l = midCol + 1
        
        return False