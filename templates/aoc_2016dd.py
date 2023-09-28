import aoc_2016dd_utilities as aoc_util
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


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str("")


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str("")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    # aoc_util.send_answer(part="a", answer=answer_a)

    # answer_b = solve_b(aoc_util.PUZZLE.input_data)
    # print(f"Part b: {answer_b}")
    # aoc_util.send_answer(part="b", answer=answer_b)
