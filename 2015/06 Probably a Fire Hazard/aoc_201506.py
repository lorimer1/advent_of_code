from aocd.models import Puzzle
from collections import namedtuple

# Define a namedtuple to represent each statement
Statement = namedtuple("Statement", ["action", "start_x", "start_y", "end_x", "end_y"])


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


def parse(puzzle_input: list[str]) -> list[namedtuple]:
    result = []

    for statement in puzzle_input.split("\n"):
        parts = statement.split(" ")
        action = parts[-4]
        start_x, start_y = map(int, parts[-3].split(","))
        end_x, end_y = map(int, parts[-1].split(","))
        statement_obj = Statement(action, start_x, start_y, end_x, end_y)
        result.append(statement_obj)

    return result


def part1(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for statement in data:
        for x in range(statement.start_x, statement.end_x + 1):
            for y in range(statement.start_y, statement.end_y + 1):
                if statement.action == "on":
                    grid[x][y] = 1
                elif statement.action == "off":
                    grid[x][y] = 0
                else:
                    grid[x][y] = 0 if grid[x][y] == 1 else 1

    return sum(value for row in grid for value in row)


def part2(puzzle_input: str):
    data = parse(puzzle_input)  # pre-process input
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for statement in data:
        for x in range(statement.start_x, statement.end_x + 1):
            for y in range(statement.start_y, statement.end_y + 1):
                if statement.action == "on":
                    grid[x][y] += 1
                elif statement.action == "off":
                    grid[x][y] -= 1 if grid[x][y] > 0 else 0
                else:
                    grid[x][y] += 2

    return sum(value for row in grid for value in row)


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=6)
    # print_example_test_data(puzzle)
    solve(puzzle, submit_a=True, submit_b=True)
