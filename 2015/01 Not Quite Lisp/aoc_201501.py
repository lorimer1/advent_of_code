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


def parse(puzzle_input):
    return puzzle_input


def part1(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    return data.count("(") - data.count(")")


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    acc = 0
    for pos, char in enumerate(data):
        if char == "(":
            acc += 1
        else:
            acc -= 1
        if acc == -1:
            return pos + 1


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
    puzzle: Puzzle = Puzzle(year=2015, day=1)  # Not Quite Lisp
    print_example_test_data(puzzle)
    solve(puzzle, submit_a=False, submit_b=False)
