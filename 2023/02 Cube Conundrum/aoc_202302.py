import aoc_202302_utilities as aoc_util
from dataclasses import dataclass, field

TEST_COUNTS = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Game:
    input: str
    number: int = 0
    revealed: dict[str, list[int]] = field(default_factory=dict)

    def __post_init__(self):
        self.revealed = {colour: [] for colour in TEST_COUNTS}
        game_str, details = self.input.split(": ")
        _, number = game_str.split()
        self.number = int(number)
        handfuls = details.split("; ")
        for handful in handfuls:
            cubes = handful.split(", ")
            for cube in cubes:
                count, colour = cube.split()
                self.revealed[colour].append(int(count))

    def is_possible_game(self) -> bool:
        return all(
            max(self.revealed[colour]) <= target
            for colour, target in TEST_COUNTS.items()
        )

    def power(self) -> int:
        return (
            max(self.revealed["red"])
            * max(self.revealed["green"])
            * max(self.revealed["blue"])
        )


@dataclass
class Input:
    puzzle_input: str
    data: list[str] = field(default_factory=list)
    games: list[Game] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.data = self.puzzle_input.splitlines()
        self.games = [Game(line) for line in self.data]


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    input = Input(puzzle_input)
    if not is_b:
        return str(sum(game.number for game in input.games if game.is_possible_game()))
    return str(sum(game.power() for game in input.games))


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
