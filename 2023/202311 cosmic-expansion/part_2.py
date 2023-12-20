import utils
from itertools import combinations


@utils.timeit
def solve(input: str) -> int:
    grid = [[char for char in row] for row in input.splitlines()]
    rows_to_expand = [
        r for r, row in enumerate(grid) if all([char == "." for char in row])
    ]
    cols_to_expand = [
        c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)
    ]
    points = [
        (r, c)
        for r, row in enumerate(grid)
        for c, char in enumerate(row)
        if char == "#"
    ]

    expand = 1_000_000
    distance = 0
    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                distance += expand if r in rows_to_expand else 1
            for c in range(min(c1, c2), max(c1, c2)):
                distance += expand if c in cols_to_expand else 1

    return distance


if __name__ == "__main__":
    with open("2023/202311 cosmic-expansion/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
