from aocd.models import Puzzle


def print_example_test_data(puzzle: Puzzle):
    if not puzzle.answered_a:
        print(
            [
                (example.input_data, int(example.answer_a))
                for example in puzzle.examples
                if not example.answer_a is None
            ]
        )
        return

    print(
        [
            (example.input_data, int(example.answer_b))
            for example in puzzle.examples
            if not example.answer_b is None
        ]
    )


def solve(puzzle: Puzzle, submit_a=False, submit_b=False):
    solution1 = part1(puzzle.input_data)
    solution2 = part2(puzzle.input_data)

    print(solution1)
    print(solution2)

    if submit_a and not puzzle.answered_a:
        puzzle.answer_a = solution1
    if submit_b and not puzzle.answered_b:
        puzzle.answer_b = solution2


import re


def parse(puzzle_input):
    return puzzle_input.splitlines()


def is_nice_string(s):
    # Rule 1: Contains at least three vowels
    if not sum(c in "aeiou" for c in s) >= 3:
        return False

    # Rule 2: Contains at least one letter that appears twice in a row
    if not any(a == b for a, b in zip(s, s[1:])):
        return False

    # Rule 3: Does not contain the forbidden substrings
    if not all(f not in s for f in ("ab", "cd", "pq", "xy")):
        return False

    return True


def is_nice_string_2(s):
    # Rule 1: Check for a pair of any two letters that appears at least twice without overlapping
    if not re.search(r"(..).*\1", s):
        return False

    # Rule 2: Check for a letter that repeats with exactly one letter between them
    if not re.search(r"(.).\1", s):
        return False

    return True


def part1(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    return len(list(filter(is_nice_string, data)))


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    return len(list(filter(is_nice_string_2, data)))


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=5)  #
    # print_example_test_data(puzzle)
    solve(puzzle, submit_a=True, submit_b=True)
