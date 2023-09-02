import aoc_201511_utilities as aoc_util


def parse(puzzle_input: str) -> list[str]:
    data = list(puzzle_input)
    return data


def increment_password(password):
    while True:
        idx = -1
        while password[idx] == "z":
            password[idx] = "a"
            idx -= 1
        password[idx] = chr(ord(password[idx]) + 1)
        yield password


def solve(puzzle_input: str):
    password = parse(puzzle_input)

    has_increasing_straight = lambda pw_nums: (
        any(a == b - 1 == c - 2 for a, b, c in zip(pw_nums, pw_nums[1:], pw_nums[2:]))
    )
    has_invalid_letters = lambda pw: any(l in pw for l in "iol")
    has_two_pairs = lambda pw: len({a for a, b in zip(pw, pw[1:]) if a == b}) >= 2

    while True:
        password = next(increment_password(password))
        if (
            has_increasing_straight(list(map(ord, password)))
            and not has_invalid_letters(password)
            and has_two_pairs(password)
        ):
            return "".join(password)


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(part1)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
