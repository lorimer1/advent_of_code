import aoc_2016dd_utilities as aoc_util
from typing import NamedTuple


class Input(NamedTuple):
    data: list[str]


def parse_input(puzzle_input: str) -> Input:
    return Input(data=puzzle_input.splitlines())


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str("")


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str("")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    # aoc_util.send_answer(part="a", answer=answer_a)

    # answer_b = solve_b(aoc_util.PUZZLE.input_data)
    # print(f"Part b: {answer_b}")
    # aoc_util.send_answer(part="b", answer=answer_b)
