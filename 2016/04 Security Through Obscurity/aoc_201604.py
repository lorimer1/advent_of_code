import aoc_201604_utilities as aoc_util
from dataclasses import dataclass, field
from collections import Counter
import re


@dataclass
class CodedRoom:
    encrypted_name: str
    sector_id: int
    checksum: str


@dataclass
class Input:
    """
    Provides a useful data structure for the puzzle input.
        puzzle_input: text from input file
        data: structured puzzle input
    """

    puzzle_input: str
    data: list[CodedRoom] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""

        pattern = r"([a-z\-]+)-(\d+)\[([a-z]+)\]"

        for line in self.puzzle_input.splitlines():
            match = re.match(pattern, line)
            if match:
                self.data.append(
                    CodedRoom(
                        encrypted_name=match.group(1),
                        sector_id=int(match.group(2)),
                        checksum=match.group(3),
                    )
                )


def is_real_room(room: CodedRoom) -> bool:
    char_counts = Counter(room.encrypted_name.replace("-", ""))
    char_counts_sorted = sorted(
        char_counts.items(), key=lambda item: (-item[1], item[0])
    )
    checksum = "".join(letter for letter, _ in char_counts_sorted[:5])
    return checksum == room.checksum


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def decode(room: CodedRoom) -> str:
    def decode_char(char: str, steps: int) -> str:
        if char == "-":
            return " "
        index = ALPHABET.index(char)
        return ALPHABET[(index + steps) % 26]

    decoded: str = ""
    for char in room.encrypted_name:
        decoded += decode_char(char, room.sector_id)

    return decoded


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    return str(sum(room.sector_id for room in input.data if is_real_room(room)))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input = Input(puzzle_input)
    for room in input.data:
        if is_real_room(room) and "northpole" in decode(room):
            return str(room.sector_id)

    return str("")


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
