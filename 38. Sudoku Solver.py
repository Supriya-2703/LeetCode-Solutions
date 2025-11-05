class Solution:
    def solveSudoku(self, board):
        """
        Modify board in-place to solve the Sudoku.
        board: List[List[str]] with '.' for empty cells.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True  
            r, c = empties[idx]
            b = (r // 3) * 3 + (c // 3)
            for d in map(str, range(1, 10)):
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
            return False

        backtrack()
