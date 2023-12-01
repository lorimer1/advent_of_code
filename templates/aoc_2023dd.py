import aoc_2023dd_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Input:
    puzzle_input: str
    data: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.data = self.puzzle_input.splitlines()


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    input = Input(puzzle_input)
    raise ValueError("Answer not found")


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    # aoc_util.send_answer(part="a", answer=answer_a)

    # answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    # print(f"Part b: {answer_b}")
    # aoc_util.send_answer(part="b", answer=answer_b)
