import aoc_201615_utilities as aoc_util
from dataclasses import dataclass, field
from itertools import count


@dataclass
class Disc:
    positions: int
    start_position: int


@dataclass
class Input:
    puzzle_input: str
    discs: list[Disc] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        for line in self.puzzle_input.splitlines():
            # example line: Disc #1 has 5 positions; at time=0, it is at position 4.
            words = line.split()
            self.discs.append(
                Disc(positions=int(words[3]), start_position=int(words[-1][0]))
            )


def is_in_position(disc: Disc, time: int, position: int = 0) -> bool:
    return ((disc.start_position + time) % disc.positions) == position


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    input = Input(puzzle_input)

    if is_b:
        input.discs.append(Disc(positions=11, start_position=0))

    for time in count(start=1):
        if all(
            is_in_position(disc, time=time + disc_num)
            for disc_num, disc in enumerate(input.discs, start=1)
        ):
            return str(time)

    raise ValueError("Answer not found")


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
