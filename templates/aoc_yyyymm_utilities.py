from aocd.models import Puzzle

AOC_YEAR = 0
AOC_MONTH = 0

PUZZLE = Puzzle(year=AOC_YEAR, day=AOC_MONTH)


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


if __name__ == "__main__":
    print_example_test_data(PUZZLE)