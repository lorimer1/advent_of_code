import aoc_201601_utilities as aoc_util
from typing import NamedTuple
from dataclasses import dataclass


class Input(NamedTuple):
    data: list[str]


def parse_input(puzzle_input: str) -> Input:
    return Input(data=puzzle_input.split(", "))


ROTATION = {"L": 1j, "R": -1j}


@dataclass
class Person:
    dir: complex
    location: complex


def manhattan_dist(location: complex):
    return int(abs(location.real) + abs(location.imag))


def solve(input: Input, is_b: bool = False) -> int:
    me = Person(location=0 + 0j, dir=1j)
    visited: list[complex] = [me.location]
    for instruction in input.data:
        lr, steps = instruction[0], int(instruction[1:])
        me.dir *= ROTATION[lr]
        for _ in range(steps):
            me.location += me.dir
            if is_b and me.location in visited:
                return manhattan_dist(me.location)  # solve_b
            visited.append(me.location)

    return manhattan_dist(me.location)  # solve_a


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
