import utils


@utils.timeit
def solve(input: str) -> int:
    seeds, *blocks = input.split("\n\n")

    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new

    return min(seeds)


if __name__ == "__main__":
    with open("2023/202305 if-you-give-a-seed-a-fertilizer/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
