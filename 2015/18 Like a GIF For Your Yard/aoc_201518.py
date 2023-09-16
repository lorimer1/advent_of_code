import aoc_201518_utilities as aoc_util
import copy

OFFSETS = [-1, 0, 1]


def get_max(grid: list[list]):
    return len(grid) - 1, len(grid[0]) - 1


def turn_corners_on(grid: list[list], boundary: tuple):
    r_max, c_max = boundary
    grid[0][0] = "#"
    grid[0][c_max] = "#"
    grid[r_max][0] = "#"
    grid[r_max][c_max] = "#"


def parse(puzzle_input: str, is_b: bool = False) -> list[str]:
    grid = [[c for c in line] for line in puzzle_input.splitlines()]
    r_max, c_max = get_max(grid)
    if is_b:
        turn_corners_on(grid, (r_max, c_max))
    return grid, r_max, c_max


def count_on_neigbours(grid: list[list], location: tuple, boundary: tuple) -> int:
    r_max, c_max = boundary
    r, c = location
    r_test, c_test = 0, 0
    on_count = 0
    for r_offset in OFFSETS:
        for c_offset in OFFSETS:
            r_test, c_test = (
                r + r_offset,
                c + c_offset,
            )
            if (
                (r_test == r and c_test == c)
                or not (0 <= r_test <= r_max)
                or not (0 <= c_test <= c_max)
            ):
                continue
            if grid[r_test][c_test] == "#":
                on_count += 1
    return on_count


def new_state(
    grid: list[list], location: tuple, current_state: str, boundary: tuple, is_b: bool
):
    r_max, c_max = boundary
    r, c = location
    if is_b and r in [0, r_max] and c in [0, c_max]:
        return current_state
    on_count = count_on_neigbours(grid, (r, c), (r_max, c_max))
    if current_state == "#":
        return "#" if on_count in [2, 3] else "."

    return "#" if on_count == 3 else "."


def solve(puzzle_input: str, iterations: int, is_b: bool = False):
    grid, r_max, c_max = parse(puzzle_input, is_b)

    while iterations:
        new_grid = copy.deepcopy(grid)
        for r, row in enumerate(grid):
            for c, state in enumerate(row):
                new_grid[r][c] = new_state(grid, (r, c), state, (r_max, c_max), is_b)
        grid = new_grid
        iterations -= 1

    return str(sum(row.count("#") for row in grid))


if __name__ == "__main__":
    grid = aoc_util.PUZZLE.input_data

    part1 = solve(grid, iterations=100)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(grid, iterations=100, is_b=True)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
