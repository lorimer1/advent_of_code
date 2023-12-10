import utils


@utils.timeit
def solve(input: str) -> int:
    t = 0

    for x in input.splitlines():
        x = x.split(":")[1].strip()
        a, b = [list(map(int, k.split())) for k in x.split(" | ")]
        j = sum(q in a for q in b)
        if j > 0:
            t += 2 ** (j - 1)

    return t


if __name__ == "__main__":
    with open("2023/202304 scratchcards/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
