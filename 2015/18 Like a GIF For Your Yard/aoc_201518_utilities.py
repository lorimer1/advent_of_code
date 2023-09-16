from aocd.models import Puzzle
import os


def file_name() -> str:
    return __file__.split(os.path.sep)[-1]


def aoc_year_from_path() -> int:
    return int(file_name()[4:8])


def aoc_day_from_path() -> int:
    return int(file_name()[8:10])


def print_test_info():
    test_data = {"a": [], "b": []}
    for example in PUZZLE.examples:
        part = "b" if example.answer_a is None else "a"
        answer = getattr(example, f"answer_{part}")
        test_data[part].append((example.input_data, answer, example.extra))
    print(test_data)


PUZZLE = Puzzle(year=aoc_year_from_path(), day=aoc_day_from_path())


if __name__ == "__main__":
    print_test_info()
