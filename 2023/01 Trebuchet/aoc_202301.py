import aoc_202301_utilities as aoc_util
from dataclasses import dataclass, field

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


@dataclass
class Input:
    puzzle_input: str
    data: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.data = self.puzzle_input.splitlines()


def find_digit(line: str, is_from_end: bool, is_check_spelled: bool) -> int:
    if not is_from_end:
        for index, char in enumerate(line):
            if char.isdigit():
                return int(char)
            if is_check_spelled:
                for num_str, num in NUMBERS.items():
                    if line.startswith(num_str, index):
                        return num
        raise ValueError("Start number not found")

    for index in range(len(line) - 1, -1, -1):
        if line[index].isdigit():
            return int(line[index])
        if is_check_spelled:
            for num_str, num in NUMBERS.items():
                if line.startswith(num_str, index):
                    return num
    raise ValueError("End number not found")


def decode_line(line: str, is_b: bool) -> int:
    start_digit = find_digit(line, is_from_end=False, is_check_spelled=is_b)
    end_digit = find_digit(line, is_from_end=True, is_check_spelled=is_b)
    return (10 * start_digit) + end_digit


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    input = Input(puzzle_input)
    return str(sum([decode_line(line, is_b) for line in input.data]))


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
