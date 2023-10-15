import aoc_201613_utilities as aoc_util
from dataclasses import dataclass, field
from collections import defaultdict, deque


@dataclass
class Maze:
    loc: complex = 0  # current location: real = col, imag = row
    dir: complex = 0  # current direction: real = left or right, imag = up or down
    grid: defaultdict[complex, str] = field(
        default_factory=lambda: defaultdict(str)
    )  # use get_grid_as_point_dict()

    WALL: str = "#"  # structure
    OPEN: str = "."  # not a structure
    DIR: dict[str, complex] = field(default_factory=dict)  # directions: L, R, U, D
    TURN: dict[str, complex] = field(default_factory=dict)  # turns: L, R

    def __post_init__(self):
        # self.MOVE = {"U": -1j, "D": +1j, "L": -1, "R": 1}
        self.MOVE = {"R": 1, "L": -1, "D": +1j, "U": -1j}
        self.TURN = {"L": 1j, "R": -1j}

    def manhattan_dist(self):
        """manhattan distance from 0 + 0j"""
        return int(abs(self.loc.real) + abs(self.loc.imag))

    def move(self, steps: int = 1):
        """move n steps in current direction"""
        self.loc += steps * self.dir

    def turn_lr(self, lr: str):
        """change direction by 90 degrees left or right"""
        self.dir *= self.TURN[lr]

    def set_dir(self, dir: str):
        """set the current direction"""
        self.dir = self.DIR[dir]

    def max_row_idex(self) -> int:
        """get the grid maximum row index"""
        row_indexes = [int(loc.imag) for loc in self.grid.keys()]
        return max(row_indexes)

    def max_col_idex(self) -> int:
        """get the grid maximum col index"""
        col_indexes = [int(loc.real) for loc in self.grid.keys()]
        return max(col_indexes)

    def set_grid(self, grid: list[list[str]]):
        """create grid from a list representation of a grid"""
        self.grid = defaultdict(str)
        for r, row in enumerate(grid):
            for c, point_value in enumerate(row):
                point = complex(real=c, imag=r)
                self.grid[point] = point_value

    def get_printable(self):
        """get a printable version of the grid"""
        result = []
        for row in range(self.max_row_idex() + 1):
            row_str = ""
            for col in range(self.max_col_idex() + 1):
                val = self.grid[complex(real=col, imag=row)]
                row_str += val if val else " "
            result.append(row_str)
        return "\n".join(result)


def val_at_loc(maze: Maze, location: complex, fav_num: int) -> str:
    x = int(location.real)
    y = int(location.imag)
    num = x * x + 3 * x + 2 * x * y + y + y * y
    num += fav_num
    num = bin(num).count("1")
    return maze.WALL if bool(num % 2) else maze.OPEN


@aoc_util.timeit
def solve(puzzle_input: int, start: complex, target: complex, is_b=False) -> str:
    maze = Maze(loc=start)
    que: deque[tuple[complex, int]] = deque([(maze.loc, 0)])
    seen: set[complex] = set()

    while que:
        loc, steps = que.popleft()

        if not is_b and loc == target:
            return str(steps)

        if is_b and steps > 50:
            return str(len(seen))

        seen.add(loc)

        for step in maze.MOVE.values():
            new_loc = loc + step

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
