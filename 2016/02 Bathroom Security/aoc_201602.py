import aoc_201602_utilities as aoc_util
from typing import NamedTuple

NUMPAD_A = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

NUMPAD_B = [
    ["", "", "1", "", ""],
    ["", "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["", "A", "B", "C", ""],
    ["", "", "D", "", ""],
]

STEP = {"U": -1j, "D": +1j, "R": 1, "L": -1}


class Input(NamedTuple):
    data: list[str]


def parse_input(puzzle_input: str) -> Input:
    return Input(data=puzzle_input.splitlines())


def get_key_pos(key: str, numpad: list[list[str]]) -> complex:
    for row in range(len(numpad)):
        for col in range(len(numpad[row])):
            if numpad[row][col] == key:
                return complex(real=col, imag=row)
    return 0 + 0j


def get_next_key_pos(pos: complex, step: complex, numpad: list[list[str]]) -> complex:
    max_col = len(numpad[0]) - 1
    max_row = len(numpad) - 1
    new_pos = pos + step
    if (
        0 <= int(new_pos.real) <= max_col
        and 0 <= int(new_pos.imag) <= max_row
        and NUMPAD_B[int(new_pos.imag)][int(new_pos.real)] != ""
    ):
        return new_pos
    else:
        return pos


def solve(input: Input, numpad: list[list[str]], start_key: str) -> str:
    pos: complex = get_key_pos(start_key, numpad=numpad)
    result = ""
    for num_instruction in input.data:
        for step in num_instruction:
            pos = get_next_key_pos(pos, STEP[step], numpad)
        result += numpad[int(pos.imag)][int(pos.real)]

    return result


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return solve(input, numpad=NUMPAD_A, start_key="5")


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = parse_input(puzzle_input)
    return solve(input, numpad=NUMPAD_B, start_key="5")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
