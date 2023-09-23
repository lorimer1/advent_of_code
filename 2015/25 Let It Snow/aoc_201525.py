import aoc_201525_utilities as aoc_util
from typing import NamedTuple
from itertools import count


class Input(NamedTuple):
    row: int
    col: int


def parse_input(puzzle_input: str) -> Input:
    words = puzzle_input.split(" ")
    row = int(words[-3].split(",")[0])
    col = int(words[-1][:-1])
    return Input(row, col)


def solve(input: Input, start: int = 20151125) -> int:
    result = start
    for diagonal in count(start=2):
        col = 1
        for row in range(diagonal, 0, -1):
            result = (result * 252533) % 33554393
            if row == input.row and col == input.col:
                return result
            col += 1

    return -1


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str(solve(input))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str("")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    # answer_b = solve_b(aoc_util.PUZZLE.input_data)
    # print(f"Part b: {answer_b}")
    # aoc_util.send_answer(part="b", answer=answer_b)
