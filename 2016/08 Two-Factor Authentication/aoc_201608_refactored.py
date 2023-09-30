import aoc_201608_utilities as aoc_util
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Input:
    """
    Provides a useful data structure for the puzzle input.
        puzzle_input: text from input file
        data: structured puzzle input
    """

    puzzle_input: str
    operations: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.operations = [line for line in self.puzzle_input.splitlines()]


def do_operation(screen: np.ndarray, operation: str) -> np.ndarray:
    if operation.startswith("rect"):
        width, height = map(int, operation.split()[1].split("x"))
        screen[:height, :width] = 1
    elif operation.startswith("rotate"):
        _, axis, index, _, shift = operation.split()
        index = int(index.split("=")[1])
        shift = int(shift)
        if axis == "row":
            screen[index] = np.roll(screen[index], shift)
        else:
            screen[:, index] = np.roll(screen[:, index], shift)
    return screen


def solve(puzzle_input: str) -> np.ndarray:
    input = Input(puzzle_input)
    screen = np.zeros((6, 50))
    for operation in input.operations:
        screen = do_operation(screen, operation)
    return screen


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    screen = solve(puzzle_input)
    return str(int(sum([pixel for row in screen for pixel in row])))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    screen = solve(puzzle_input)
    return "\n" + "\n".join(
        " ".join("#" if on else " " for on in line) for line in screen
    )


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")  # read the terminal for answer
    aoc_util.send_answer(part="b", answer="ZJHRKCPLYJ")
