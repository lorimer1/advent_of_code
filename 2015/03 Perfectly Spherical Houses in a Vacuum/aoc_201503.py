from aocd.models import Puzzle
from collections import Counter


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

    dirs = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    x, y = 0, 0
    locations: set = set()
    locations.add((x, y))

    for dir in puzzle_input:
        dx, dy = dirs[dir][0], dirs[dir][1]
        x += dx
        y += dy
        locations.add((x, y))

    return len(locations)


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input

    dirs = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    x, y = 0, 0
    locations = set()
    locations.add((x, y))

    workers = {"santa": [x, y], "robo": [x, y]}
    worker = "santa"

    x_idx, y_idx = 0, 1

    for dir in puzzle_input:
        dx, dy = dirs[dir][0], dirs[dir][1]
        workers[worker][x_idx] += dx
        workers[worker][y_idx] += dy
        locations.add((workers[worker][x_idx], workers[worker][y_idx]))
        worker = "robo" if worker == "santa" else "santa"

    return len(locations)


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
    puzzle: Puzzle = Puzzle(year=2015, day=3)
    print_example_test_data(puzzle)
    solve(puzzle, submit_a=True, submit_b=True)
