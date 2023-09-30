import aoc_201608_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Input:
    """
    Provides a useful data structure for the puzzle input.
        puzzle_input: text from input file
        data: structured puzzle input
    """

    puzzle_input: str
    data: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.data = [line for line in self.puzzle_input.splitlines()]


ON = "#"
OFF = "."
SCREEN = [[OFF] * 50 for _ in range(6)]


def transpose(array: list[list[str]]) -> list[list[str]]:
    return [list(x) for x in zip(*array)]


def do_rect(screen: list[list[str]], area: str) -> list[list[str]]:
    wide, tall = [int(val) for val in area.split("x")]
    for row in range(tall):
        for col in range(wide):
            screen[row][col] = ON
    return screen


def do_rotate_row(screen: list[list[str]], row: int, steps: int) -> list[list[str]]:
    new_row = [OFF] * 50
    for col_idx, pixel in enumerate(screen[row]):
        new_row[(col_idx + steps) % 50] = pixel
    screen[row] = new_row
    return screen


def do_rotate_col(screen: list[list[str]], col: int, steps: int) -> list[list[str]]:
    trasposed_screen = transpose(screen)
    new_transposed_col = [OFF] * 6
    for row_idx, pixel in enumerate(trasposed_screen[col]):
        new_transposed_col[(row_idx + steps) % 6] = pixel
    trasposed_screen[col] = new_transposed_col
    return transpose(trasposed_screen)


def do_rotate(screen: list[list[str]], tokens: list[str]) -> list[list[str]]:
    axis = tokens[0]
    index = int(tokens[1].split("=")[-1])
    shift = int(tokens[-1])
    if axis == "row":
        return do_rotate_row(screen, index, shift)
    else:
        return do_rotate_col(screen, index, shift)


def do_operation(screen: list[list[str]], operation: str) -> list[list[str]]:
    tokens = [token for token in operation.split()]
    if tokens[0] == "rect":
        return do_rect(screen, tokens[1])
    else:
        return do_rotate(screen, tokens[1:])


def solve(puzzle_input: str) -> list[list[str]]:
    input = Input(puzzle_input)
    screen = SCREEN
    for operation in input.data:
        screen = do_operation(screen, operation)
    return screen


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    screen = solve(puzzle_input)
    return str(len([pixel for row in screen for pixel in row if pixel == ON]))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    screen = solve(puzzle_input)
    result = ""
    for row in screen:
        result += "\n" + "".join(row)
    return str(result)


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")  # read the terminal for answer
    aoc_util.send_answer(part="b", answer="ZJHRKCPLYJ")
