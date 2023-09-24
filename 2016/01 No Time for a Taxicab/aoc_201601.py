import aoc_201601_utilities as aoc_util
from typing import NamedTuple
from dataclasses import dataclass


@dataclass
class Location:
    dir: str
    N: int
    E: int


DIRECTIONS = {
    "N": {"N_Step": 1, "E_Step": 0, "R": "E", "L": "W"},
    "E": {"N_Step": 0, "E_Step": 1, "R": "S", "L": "N"},
    "S": {"N_Step": -1, "E_Step": 0, "R": "W", "L": "E"},
    "W": {"N_Step": 0, "E_Step": -1, "R": "N", "L": "S"},
}


class Input(NamedTuple):
    data: list[str]


def parse_input(puzzle_input: str) -> Input:
    return Input(data=puzzle_input.split(", "))


def solve(input: Input, is_b: bool = False) -> int:
    loc = Location(dir="N", N=0, E=0)
    visited: list[tuple[int, int]] = [(loc.N, loc.E)]
    passed_twice = False
    for dir_steps in input.data:
        lr, steps = dir_steps[0], int(dir_steps[1:])
        loc.dir = DIRECTIONS[loc.dir][lr]
        while steps:
            loc.N += DIRECTIONS[loc.dir]["N_Step"]
            loc.E += DIRECTIONS[loc.dir]["E_Step"]
            if is_b and (loc.N, loc.E) in visited:
                break
            visited.append((loc.N, loc.E))
            steps -= 1

    return abs(loc.N) + abs(loc.E)


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str(solve(input))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return str((solve(input, is_b=True)))


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
