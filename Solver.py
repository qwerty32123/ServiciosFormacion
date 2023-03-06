class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        if self._solve(0, 0):
            return self.board
        else:
            return None

    def _solve(self, row, col):
        if col == 9:
            col = 0
            row += 1
            if row == 9:
                return True

        if self.board[row][col] != 0:
            return self._solve(row, col + 1)

        for num in range(1, 10):
            if self._is_valid(row, col, num):
                self.board[row][col] = num
                if self._solve(row, col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def _is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False

        for i in range(9):
            if self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False

        return True