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
    s_coord = get_start_coord(grid)
    seen = {s_coord}
    s_ends = []
    loc = s_coord

    # get first tile
    adjacent = {dir: get_tile_type(grid, loc + dir) for dir in [N, S, E, W]}
    for dir, tile in adjacent.items():
        if tile in TILES and COMPATIBLE_ENDS[dir] in TILES[tile]:
            loc += dir
            s_ends.append(dir)
            break

    # Navigate the pipe tiles until next tile is S
    while True:
        seen.add(loc)
        tile = get_tile_type(grid, loc)
        next_dir = [dir for dir in TILES[tile] if not loc + dir in seen]
        if not next_dir:
            break
        loc += next_dir[0]  # should be only one compatible direction

    # Determine S tile
    s_ends += [COMPATIBLE_ENDS[dir] for dir in TILES[tile] if loc + dir == s_coord]
    s_tile = [
        tile for tile, ends in TILES.items() if s_ends[0] in ends and s_ends[1] in ends
    ]

    # Change S tile to actual tile
    grid[int(s_coord.imag)][int(s_coord.real)] = s_tile[0]

    # Replace pipe tiles that aren't part of the pipe with "."
    grid = [
        [
            get_tile_type(grid, loc) if loc in seen else "."
            for c, _ in enumerate(row)
            if (loc := complex(c, r)) or (c >= 0 and r >= 0)
        ]
        for r, row in enumerate(grid)
    ]

    outside = set()

    for r, row in enumerate(grid):
        within = False
        up = None
        for c, tile in enumerate(row):
            if tile == "|":
                within = not within
            elif tile == "-":
                pass
            elif tile in "LF":
                up = tile == "L"
            elif tile in "7J":
                if tile != ("J" if up else "7"):
                    within = not within
                up = None
            else:  # will be "."
                pass

            if not within:
                outside.add(complex(c, r))

    return len(grid) * len(grid[0]) - len(outside | seen)


if __name__ == "__main__":
    with open("2023/202310 pipe-maze/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
