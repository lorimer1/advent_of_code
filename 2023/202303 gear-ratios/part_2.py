def solve(input: str) -> int:
    grid = input.splitlines()
    total = 0

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue

            cs = set()

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if (
                        cr < 0
                        or cr >= len(grid)
                        or cc < 0
                        or cc >= len(grid[cr])
                        or not grid[cr][cc].isdigit()
                    ):
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

            if len(cs) != 2:
                continue

            ns = []

            for cr, cc in cs:
                s = ""
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    s += grid[cr][cc]
                    cc += 1
                ns.append(int(s))

            total += ns[0] * ns[1]

    return total


if __name__ == "__main__":
    with open("2023/202303 gear-ratios/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
