class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def backtrack(row, column, index):
            if index == len(word):
                return True
            if row < 0 or column < 0 or row >= rows or column >= columns:
                return False
            if board[row][column] != word[index]:
                return False

            original_letter = board[row][column]
            board[row][column] = '#'
            
            found = (
                backtrack(row + 1, column, index + 1) or
                backtrack(row - 1, column, index + 1) or
                backtrack(row, column + 1, index + 1) or
                backtrack(row, column - 1, index + 1)
            )

            board[row][column] = original_letter
            return found

        for row in range(rows):
            for col in range(columns):
                if backtrack(row, col, 0):
                    return True

        return False