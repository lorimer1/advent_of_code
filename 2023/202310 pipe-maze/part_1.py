import utils

W = -1 + 0j
E = 1 + 0j
N = -1j
S = +1j

COMPATIBLE_ENDS = {N: S, E: W, S: N, W: E}

TILES = {
    "|": [N, S],
    "-": [E, W],
    "L": [N, E],
    "J": [N, W],
    "7": [S, W],
    "F": [S, E],
}


def get_start_coord(grid: list[list[str]]) -> complex:
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "S":
                return complex(c, r)
    raise ValueError("S not found")


def get_tile_type(grid: list[list[str]], loc: complex) -> str:
    return grid[int(loc.imag)][int(loc.real)]


@utils.timeit
def solve(input: str) -> int:
    grid = [[tile for tile in line] for line in input.splitlines()]
    loc = get_start_coord(grid)
    seen = {loc}

    # get first tile
    adjacent = {dir: get_tile_type(grid, loc + dir) for dir in [N, S, E, W]}
    for dir, tile in adjacent.items():
        if tile in TILES and COMPATIBLE_ENDS[dir] in TILES[tile]:
            loc += dir
            break

    # Navigate the pipe tiles
    while True:
        seen.add(loc)
        tile = get_tile_type(grid, loc)
        next_dir = [dir for dir in TILES[tile] if not loc + dir in seen]
        if not next_dir:
            break
        loc += next_dir[0]  # should be only one compatible direction

    return len(seen) // 2


if __name__ == "__main__":
    with open("2023/202310 pipe-maze/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
