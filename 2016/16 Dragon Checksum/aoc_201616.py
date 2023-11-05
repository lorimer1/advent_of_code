import aoc_201616_utilities as aoc_util
from dataclasses import dataclass, field


def create_data(input: str, length: int) -> str:
    a = input

    while len(a) < length:
        b = ["1" if bit == "0" else "0" for bit in reversed(a)]
        a += "0" + "".join(b)

    return a[:length]


def calc_checksum(data: str) -> str:
    while True:
        checksum = ""

        for digit_1, digit_2 in zip(data[::2], data[1::2]):
            checksum += "1" if digit_1 == digit_2 else "0"

        if len(checksum) % 2:
            return checksum

        data = checksum


@aoc_util.timeit
def solve(puzzle_input: str, disk_length: int, is_b=False) -> str:
    data = create_data(puzzle_input, disk_length)
    return calc_checksum(data)


if __name__ == "__main__":
    answer_a = solve(puzzle_input="00101000101111010", disk_length=272)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(puzzle_input="00101000101111010", disk_length=35651584)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
