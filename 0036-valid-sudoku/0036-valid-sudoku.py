class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COLS = collections.defaultdict(set)
        ROWS = collections.defaultdict(set)
        SUB_BOXES = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):

                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in ROWS[r]
                    or board[r][c] in COLS[c]
                    or board[r][c] in SUB_BOXES[r // 3, c // 3]
                ):
                    return False

                COLS[c].add(board[r][c])
                ROWS[r].add(board[r][c])
                SUB_BOXES[r // 3, c // 3].add(board[r][c])

        return True
