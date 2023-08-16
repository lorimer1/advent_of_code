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


from itertools import accumulate


def parse(puzzle_input):
    return puzzle_input


def part1(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    return data.count("(") - data.count(")")


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    travel = lambda acc, c: acc + (1 if c == "(" else -1)
    floors_visited = list(accumulate(data, travel, initial=0))
    return next(i for i, floor in enumerate(floors_visited) if floor < 0)


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=1)  # Not Quite Lisp
    print_example_test_data(puzzle)
    solve(puzzle, submit_a=False, submit_b=False)
