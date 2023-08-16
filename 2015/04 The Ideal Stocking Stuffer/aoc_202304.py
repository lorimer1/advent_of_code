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


from hashlib import md5
from itertools import count


def parse(puzzle_input: str) -> str:
    return puzzle_input


def do_solve(input: str, target: str, start: int = 1) -> int:
    for i in count(start):
        m = md5(f"{input}{i}".encode()).hexdigest()
        if m.startswith(target):
            return i


def part1(puzzle_input: str) -> int:
    data = parse(puzzle_input)  # pre-process input
    return do_solve(puzzle_input, 5 * "0")


def part2(puzzle_input: str) -> int:
    data = parse(puzzle_input)  # pre-process input
    return do_solve(puzzle_input, 6 * "0")


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=4)  #
    # print_example_test_data(puzzle)
    solve(puzzle, submit_a=True, submit_b=True)
