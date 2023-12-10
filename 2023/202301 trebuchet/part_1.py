def solve(input: str) -> int:
    t = 0

    for x in input.splitlines():
        digits = [ch for ch in x if ch.isdigit()]
        t += int(digits[0] + digits[-1])

    return t


if __name__ == "__main__":
    with open("2023/202301 trebuchet/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
