import aoc_201613_utilities as aoc_util
from dataclasses import dataclass, field
from collections import deque


@dataclass
class Maze:
    loc: complex = 0  # current location: real = col, imag = row
    WALL: str = "#"  # structure
    DIR: dict[str, complex] = field(default_factory=dict)  # directions: L, R, U, D

    def __post_init__(self):
        self.DIR = {"L": -1, "R": 1, "U": -1j, "D": +1j}


def val_at_loc(maze: Maze, location: complex, fav_num: int) -> str:
    x = int(location.real)
    y = int(location.imag)
    num = x * x + 3 * x + 2 * x * y + y + y * y
    num += fav_num
    num = bin(num).count("1")
    return maze.WALL if bool(num % 2) else ""


@aoc_util.timeit
def solve(puzzle_input: int, start: complex, target: complex, is_b=False) -> str:
    maze = Maze(loc=start)
    que: deque[tuple[complex, int]] = deque([(maze.loc, 0)])
    seen: set[complex] = set()

    while que:
        maze.loc, steps = que.popleft()

        if not is_b and maze.loc == target:
            # print(maze.get_printable(path=seen))
            return str(steps)

        if is_b and steps > 50:
            return str(len(seen))

        seen.add(maze.loc)

        for dir in maze.DIR.values():
            new_loc = maze.loc + dir
            if not (
                new_loc in seen
                or any(n < 0 for n in (new_loc.real, new_loc.imag))
                or val_at_loc(maze=maze, location=new_loc, fav_num=puzzle_input)
                == maze.WALL
            ):
                que.append((new_loc, steps + 1))

    return str("")


if __name__ == "__main__":
    answer_a = solve(puzzle_input=1364, start=1 + 1j, target=31 + 39j)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(puzzle_input=1364, start=1 + 1j, target=31 + 39j, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
