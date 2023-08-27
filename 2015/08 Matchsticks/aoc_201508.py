import aoc_201508_utilities as aoc_util


def parse(puzzle_input: str) -> list[str]:
    data = puzzle_input.splitlines()
    return data


def solve1(puzzle_input: str):
    data = parse(puzzle_input)
    return sum(len(line) - len(eval(line)) for line in data)


def solve2(puzzle_input: str):
    data = parse(puzzle_input)
    return sum(line.count(r'"') + line.count("\\") + 2 for line in data)


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
