import utils


@utils.timeit
def solve(input: str) -> int:
    raise NotImplementedError()


if __name__ == "__main__":
    with open("$relative_path/input.txt", "r") as file:
        input = file.read()
    print(f"Part $part: {solve(input)}")
