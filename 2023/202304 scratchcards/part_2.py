import utils


@utils.timeit
def solve(input: str) -> int:
    m = {}

    for i, x in enumerate(input.splitlines()):
        if i not in m:
            m[i] = 1

        x = x.split(":")[1].strip()
        a, b = [list(map(int, k.split())) for k in x.split(" | ")]
        j = sum(q in a for q in b)

        for n in range(i + 1, i + j + 1):
            m[n] = m.get(n, 1) + m[i]

    return sum(m.values())


if __name__ == "__main__":
    with open("2023/202304 scratchcards/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
