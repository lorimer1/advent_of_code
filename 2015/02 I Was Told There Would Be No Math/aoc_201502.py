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


def parse(puzzle_input: str) -> list[list[int]]:
    return [
        [int(side) for side in line.split("x")] for line in puzzle_input.split("\n")
    ]


def part1(puzzle_input: str) -> int:
    data = parse(puzzle_input)  # pre-process input
    return sum(
        (3 * l * w) + (2 * w * h) + (2 * h * l)
        for box in data
        for l, w, h in [sorted(box)]
    )


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    return sum((2 * (l + w)) + (l * w * h) for box in data for l, w, h in [sorted(box)])


def solve(puzzle: Puzzle, submit_a=False, submit_b=False):
    solution1 = part1(puzzle.input_data)
    solution2 = part2(puzzle.input_data)

    print(solution1)
    print(solution2)

    if submit_a and not puzzle.answered_a:
        puzzle.answer_a = solution1
    if submit_b and not puzzle.answered_b:
        puzzle.answer_b = solution2


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=2)  # I Was Told There Would Be No Math
    # print_example_test_data(puzzle)
    # print(puzzle.input_data)
    solve(puzzle, submit_a=True, submit_b=True)
