import utils
from itertools import combinations


def get_expanded(grid: list[list[str]]) -> list[list[str]]:
    rows_to_expand = [
        r for r, row in enumerate(grid) if all([char == "." for char in row])
    ]
    cols_to_expand = [
        c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)
    ]
    expanded_width = len(grid[0]) + len(cols_to_expand)
    expanded = []
    for r, row in enumerate(grid):
        if r in rows_to_expand:
            expanded.append(["."] * expanded_width)
            expanded.append(["."] * expanded_width)
            continue
        expanded_row = []
        for c, char in enumerate(row):
            expanded_row.append(char)
            if c in cols_to_expand:
                expanded_row.append(".")
        expanded.append(expanded_row)

    return expanded


@utils.timeit
def solve(input: str) -> int:
    grid = [[char for char in row] for row in input.splitlines()]
    expanded = get_expanded(grid)
    galaxies = {
        (r, c)
        for r, row in enumerate(expanded)
        for c, char in enumerate(row)
        if char == "#"
    }
    pairs = list(combinations(galaxies, 2))

    distances = [
        abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in pairs
    ]
    return sum(distances)


if __name__ == "__main__":
    with open("2023/202311 cosmic-expansion/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
