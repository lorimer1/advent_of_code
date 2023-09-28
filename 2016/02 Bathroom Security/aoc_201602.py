import aoc_201602_utilities as aoc_util
from typing import NamedTuple
from dataclasses import dataclass

NUMPAD_A = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

NUMPAD_B = [
    ["", "", "1", "", ""],
    ["", "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["", "A", "B", "C", ""],
    ["", "", "D", "", ""],
]

STEP = {"U": -1j, "D": +1j, "R": 1, "L": -1}


@dataclass
class Input:
    puzzle_input: str
    data: list[str]

    def __post_init__(self):
        self.data = self.puzzle_input.splitlines()


def get_numpad_as_dict(numpad: list[list[str]]) -> dict[complex, str]:
    numpad_dict = dict()
    for r, row in enumerate(numpad):
        for c, key_value in enumerate(row):
            key_location = complex(real=c, imag=r)
            numpad_dict[key_location] = key_value
    return numpad_dict


def get_key_location(key: str, numpad: dict[complex, str]) -> complex:
    for key_location, key_value in numpad.items():
        if key_value == key:
            return key_location
    return 0 + 0j


def solve(input: Input, numpad: dict[complex, str], start_key: str) -> str:
    key_location: complex = get_key_location(start_key, numpad)
    result = ""
    for steps in input.data:
        for step in steps:
            new_location = key_location + STEP[step]
            if new_location in numpad and numpad[new_location] != "":
                key_location = new_location
        result += numpad[key_location]

    return result


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input, data=[])
    return solve(input, numpad=get_numpad_as_dict(NUMPAD_A), start_key="5")


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input, data=[])
    return solve(input, numpad=get_numpad_as_dict(NUMPAD_B), start_key="5")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
