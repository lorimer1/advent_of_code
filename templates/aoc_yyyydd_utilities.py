import aocd.models
from functools import wraps
import os
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__}: {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def file_name() -> str:
    return __file__.split(os.path.sep)[-1]


def aoc_year_from_path() -> int:
    return int(file_name()[4:8])


def aoc_day_from_path() -> int:
    return int(file_name()[8:10])


def print_test_info():
    test_data: dict[str, list[tuple[str, str, str]]]
    example: aocd.models.examples.Example

    test_data = {"a": [], "b": []}
    for example in PUZZLE.examples:
        part = "b" if example.answer_a is None else "a"
        answer = getattr(example, f"answer_{part}")
        test_data[part].append((example.input_data, answer, example.extra))
    print(test_data)


def send_answer(part: str, answer: str):
    answered = getattr(PUZZLE, f"answered_{part}")
    if not answered:
        if part == "a":
            PUZZLE.answer_a = answer
        else:
            PUZZLE.answer_b = answer


PUZZLE = aocd.models.Puzzle(year=aoc_year_from_path(), day=aoc_day_from_path())


if __name__ == "__main__":
    print_test_info()
