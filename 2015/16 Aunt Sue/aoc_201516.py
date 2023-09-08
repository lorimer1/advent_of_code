import aoc_201516_utilities as aoc_util

MFCSAM_RESULT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

# Sue 1: children: 1, cars: 8, vizslas: 7


def parse_line(line: str) -> dict:
    name_part_len = len(line.split(": ")[0])
    sue_part, rest = line[:name_part_len], line[name_part_len + 2 :]
    sue_num = int(sue_part.split(" ")[1])
    sue = dict()
    for attribute in rest.split(", "):
        key, val = attribute.split(": ")
        sue[key] = int(val)
    return sue, sue_num


def parse(puzzle_input: str) -> list[str]:
    data = puzzle_input.splitlines()
    return data


def is_my_aunt(test_sue: dict, is_b: bool = False) -> bool:
    for key in test_sue:
        if is_b and key in ["cats", "trees"]:
            if test_sue[key] <= MFCSAM_RESULT[key]:
                return False
        elif is_b and key in ["pomeranians", "goldfish"]:
            if test_sue[key] >= MFCSAM_RESULT[key]:
                return False
        elif test_sue[key] != MFCSAM_RESULT[key]:
            return False

    return True


def solve(puzzle_input: str, is_b: bool = False):
    data = parse(puzzle_input)
    for line in data:
        sue, sue_num = parse_line(line)
        if is_my_aunt(sue, is_b):
            return sue_num
    return None


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(input_data, is_b=True)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
