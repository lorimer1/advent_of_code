import aoc_201512_utilities as aoc_util
import re
import json


numbers = re.compile("-?\d+")


def parse1(puzzle_input: str) -> list[int]:
    data = list(map(int, re.findall(numbers, puzzle_input)))
    return data


def solve1(puzzle_input: str) -> int:
    data = parse1(puzzle_input)
    return sum(data)


def parse2(puzzle_input: str) -> list[str]:
    data = json.loads(puzzle_input)
    return data


def solve2(puzzle_input: str) -> list:
    data = parse2(puzzle_input)
    return find_sum(data)


def find_sum(jason: list) -> int:
    if type(jason) is int:
        return jason

    if type(jason) is dict:
        if "red" in jason.values():
            return 0
        else:
            return sum(map(find_sum, jason.values()))

    if type(jason) is list:
        return sum(map(find_sum, jason))
    else:
        return 0


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve1(input_data)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve2(input_data)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
