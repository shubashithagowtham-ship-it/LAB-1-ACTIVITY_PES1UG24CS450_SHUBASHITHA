import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = self.choose_size()
        self.puzzle = Puzzle(self.size)

        # Session statistics are initialised once.
        self.moves = 0
        self.started = time.monotonic()

    def choose_size(self):
        while True:
            print("\nChoose Puzzle Size:")
            print("3 - 3x3")
            print("4 - 4x4")
            print("5 - 5x5")

            choice = input("Enter 3, 4, or 5: ").strip()

            if choice in ("3", "4", "5"):
                return int(choice)

            print("Invalid choice. Please enter 3, 4, or 5.")

    def display(self):
        print()

        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        elapsed = int(time.monotonic() - self.started)
        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print(
            f"\nSliding Puzzle ({self.size}x{self.size})"
            "\nW/A/S/D moves tiles. Q quits."
        )

        while True:
            self.display()

            if self.puzzle.solved():
                elapsed = int(time.monotonic() - self.started)
                print("Solved!")
                print(
                    f"Final score: {self.moves} moves "
                    f"in {elapsed} seconds."
                )
                return

            key = input("> ").strip().lower()

            if key == "q":
                print("Game ended.")
                return

            if key not in ("w", "a", "s", "d"):
                print("Invalid command. Use W/A/S/D or Q.")
                continue

            if self.puzzle.move(key):
                self.moves += 1
            else:
                print("That move is not possible.")