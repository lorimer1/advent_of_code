import aoc_201603_utilities as aoc_util
from dataclasses import dataclass, field
from itertools import chain


@dataclass
class Input:
    puzzle_input: str
    data: list[list] = field(default_factory=list)

    def __post_init__(self):
        self.data = [
            [int(value) for value in line.split()]
            for line in self.puzzle_input.splitlines()
        ]


def is_triangle(sides: list[int]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(sum(is_triangle(candidate) for candidate in input.data))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    candidates = list(chain.from_iterable(zip(*input.data)))
    return str(
        sum(
            is_triangle(candidates[i : i + 3]) for i in range(0, len(candidates) - 2, 3)
        )
    )


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
