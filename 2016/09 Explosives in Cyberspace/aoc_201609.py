import aoc_201609_utilities as aoc_util
from dataclasses import dataclass, field
from typing import NamedTuple
import re


@dataclass
class Input:
    """
    Provides a useful data structure for the puzzle input.
        puzzle_input: text from input file
        data: structured puzzle input
    """

    puzzle_input: str
    without_whitespace: str = field(default_factory=str)

    def __post_init__(self):
        """parse the puzzle input"""
        self.without_whitespace = self.puzzle_input.replace("\n", "")


BRACKET_PATTERN = re.compile(r"\((\d+)x(\d+)\)")


def decompress(compressed, is_b=False):
    brackets = BRACKET_PATTERN.search(compressed)
    if not brackets:
        return len(compressed)
    length = int(brackets.group(1))
    repeats = int(brackets.group(2))
    start_idx = brackets.start() + len(brackets.group())
    count = (
        decompress(compressed[start_idx : start_idx + length], is_b) if is_b else length
    )

    return (
        len(compressed[: brackets.start()])
        + repeats * count
        + decompress(compressed[start_idx + length :], is_b)
    )


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(decompress(compressed=input.without_whitespace))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(decompress(compressed=input.without_whitespace, is_b=True))


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
