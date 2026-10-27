class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                for j in range(9):
                    if j != c and board[r][j] == num:
                        return False

                # Check current column
                for i in range(9):
                    if i != r and board[i][c] == num:
                        return False

           
                start_row = (r // 3) * 3
                start_col = (c // 3) * 3

                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if (i != r or j != c) and board[i][j] == num:
                            return False

        return True