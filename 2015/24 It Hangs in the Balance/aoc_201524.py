import aoc_201524_utilities as aoc_util
from typing import NamedTuple
from itertools import permutations
from functools import reduce

"""
g1, g2, g3 weigh the same
smallest g1 possible
return product of g1 (smallest g1 if multiple smallest g1)
"""


class Input(NamedTuple):
    data: list[int]


class Solution(NamedTuple):
    used: int
    qe: int


def parse_input(puzzle_input: str) -> Input:
    return Input(data=sorted(map(int, puzzle_input.splitlines()), reverse=True))


def get_max_count(all_weights: list[int], goal_weight: int) -> int:
    weight = 0
    for idx, weight in enumerate(reversed(all_weights)):
        weight += weight
        if weight >= goal_weight:
            return idx
    return len(all_weights)


def solve(all_weights: list[int], no_of_groups: int) -> int:
    def aux(weights, used_weight, used_count, qe):
        if used_weight == goal_weight:
            possible_solutions.add(Solution(used_count, qe))
        elif used_weight < goal_weight and weights and used_count < max_allowed_count:
            aux(weights[1:], used_weight, used_count, qe)
            aux(weights[1:], used_weight + weights[0], used_count + 1, qe * weights[0])

    possible_solutions: set[Solution] = set()
    goal_weight = sum(all_weights) // no_of_groups
    max_allowed_count = get_max_count(all_weights, goal_weight)
    aux(all_weights, used_weight=0, used_count=0, qe=1)
    best_solution = min(possible_solutions)
    return best_solution.qe


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
