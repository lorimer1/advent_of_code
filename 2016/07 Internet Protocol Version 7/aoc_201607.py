import aoc_201607_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Input:
    """
    Provides a useful data structure for the puzzle input.
        puzzle_input: text from input file
        data: structured puzzle input
    """

    puzzle_input: str
    data: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.data = [line for line in self.puzzle_input.splitlines()]


def is_abba(sequence: str) -> bool:
    return any(
        a + b == d + c and a != b
        for a, b, c, d in zip(sequence, sequence[1:], sequence[2:], sequence[3:])
    )


def is_ababab(supernet: str, hypernet: str) -> bool:
    return any(
        a == c and a != b and b + a + b in hypernet
        for a, b, c in zip(supernet, supernet[1:], supernet[2:])
    )


def is_valid_a(supernet: str, hypernet: str) -> bool:
    return is_abba(supernet) and not is_abba(hypernet)


def is_valid_b(supernet: str, hypernet: str) -> bool:
    return is_ababab(supernet, hypernet)


def solve(addresses: list[str], is_valid) -> int:
    valid_ip_count = 0
    for address in addresses:
        supernet = ""
        hypernet = ""
        is_supernet = True
        sequence = ""
        for char in address:
            if char in "[]":
                supernet += " " + sequence if is_supernet else ""
                hypernet += " " + sequence if not is_supernet else ""
                is_supernet = True if char == "]" else False
                sequence = ""
                continue
            sequence += char
        supernet += " " + sequence
        valid_ip_count += 1 if is_valid(supernet, hypernet) else 0

    return valid_ip_count


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(solve(input.data, is_valid_a))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(solve(input.data, is_valid_b))


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
