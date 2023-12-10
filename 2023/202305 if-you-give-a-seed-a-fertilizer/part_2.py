import utils


@utils.timeit
def solve(input: str) -> int:
    inputs, *blocks = input.split("\n\n")

    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
        seeds = new

    return min(seeds)[0]


if __name__ == "__main__":
    with open("2023/202305 if-you-give-a-seed-a-fertilizer/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")