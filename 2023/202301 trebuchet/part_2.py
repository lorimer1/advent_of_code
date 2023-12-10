import re


def solve(input: str) -> int:
    t = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"

    def f(x):
        if x in n:
            return str(n.index(x) + 1)
        return x

    for x in input.splitlines():
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])

    return t


if __name__ == "__main__":
    with open("2023/202301 trebuchet/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
