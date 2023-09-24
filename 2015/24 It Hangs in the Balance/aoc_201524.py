import aoc_201524_utilities as aoc_util
from typing import NamedTuple
from itertools import combinations
from functools import reduce
from operator import mul


class Input(NamedTuple):
    data: list[int]


def parse_input(puzzle_input: str) -> Input:
    return Input(data=sorted(map(int, puzzle_input.splitlines()), reverse=True))


# note that we don't need to check if the remainder evenly split in to the correct group weight
def solve(all_weights: list[int], no_of_groups: int) -> int:
    goal_weight = sum(all_weights) // no_of_groups
    for i in range(len(all_weights)):
        qes = [
            reduce(mul, c)
            for c in combinations(all_weights, i)
            if sum(c) == goal_weight
        ]
        if qes:
            return min(qes)
    return -1


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str(solve(input.data, 3))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str(solve(input.data, 4))


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
