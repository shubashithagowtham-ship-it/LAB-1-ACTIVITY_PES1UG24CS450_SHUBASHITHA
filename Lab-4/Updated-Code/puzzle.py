import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Begin with the solved arrangement.
        tiles = list(range(1, self.size * self.size)) + [0]
        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        # The blank starts at the bottom-right corner.
        blank_r = self.size - 1
        blank_c = self.size - 1

        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }
        opposite = {
            "w": "s",
            "s": "w",
            "a": "d",
            "d": "a",
        }

        previous_direction = None

        # Scramble using legal moves only.
        # Every resulting board is therefore solvable.
        steps = max(100, self.size * self.size * 20)

        for _ in range(steps):
            possible_moves = []

            for direction, (dr, dc) in directions.items():
                # Avoid immediately undoing the previous move.
                if (
                    previous_direction is not None
                    and direction == opposite[previous_direction]
                ):
                    continue

                nr = blank_r + dr
                nc = blank_c + dc

                if (
                    0 <= nr < self.size
                    and 0 <= nc < self.size
                ):
                    possible_moves.append((direction, nr, nc))

            direction, nr, nc = random.choice(possible_moves)

            # Slide an adjacent tile into the blank.
            board[blank_r][blank_c], board[nr][nc] = (
                board[nr][nc],
                board[blank_r][blank_c],
            )

            blank_r, blank_c = nr, nc
            previous_direction = direction

        # Ensure the initial board is not already solved.
        solved_board = (
            list(range(1, self.size * self.size)) + [0]
        )
        if sum(board, []) == solved_board and self.size > 1:
            board[-1][-1], board[-1][-2] = (
                board[-1][-2],
                board[-1][-1],
            )

        return board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }

        if direction not in directions:
            return False

        r, c = self.blank_pos()
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc],
            self.board[r][c],
        )
        return True

    def solved(self):
        return sum(self.board, []) == (
            list(range(1, self.size * self.size)) + [0]
        )