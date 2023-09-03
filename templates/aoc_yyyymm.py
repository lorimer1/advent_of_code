import aoc_yyyymm_utilities as aoc_util


def parse(puzzle_input: str) -> list[str]:
    data = puzzle_input.splitlines()
    return data


def solve(puzzle_input: str, is_b: bool = False):
    data = parse(puzzle_input)
    pass


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data)
    print(f"Part 1: {part1}")
    # if not aoc_util.PUZZLE.answered_a:
    #     aoc_util.PUZZLE.answer_a = part1

    # part2 = solve(input_data, is_b=True)
    # print(f"Part 2: {part2}")
    # if not aoc_util.PUZZLE.answered_b:
    #     aoc_util.PUZZLE.answer_b = part2
