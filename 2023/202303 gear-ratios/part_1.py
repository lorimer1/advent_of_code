def solve(input: str) -> int:
    grid = input.splitlines()
    cs = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    if (
                        dr < 0
                        or dr >= len(grid)
                        or dc < 0
                        or dc >= len(grid[dr])
                        or not grid[dr][dc].isdigit()
                    ):
                        continue
                    while dc > 0 and grid[dr][dc - 1].isdigit():
                        dc -= 1
                    cs.add((dr, dc))

    ns = []

    for r, c in cs:
        s = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        ns.append(int(s))

    return sum(ns)


if __name__ == "__main__":
    with open("2023/202303 gear-ratios/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
