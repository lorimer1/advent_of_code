import utils


def get_next_val(sequence: list[int]) -> int:
    if all(x == 0 for x in sequence):
        return 0
    diff_sequence = [y - x for x, y in zip(sequence, sequence[1:])]
    return sequence[0] - get_next_val(diff_sequence)


@utils.timeit
def solve(input: str) -> int:
    sequences = [list(map(int, sequence.split())) for sequence in input.splitlines()]
    return sum(map(get_next_val, sequences))


if __name__ == "__main__":
    with open("2023/202309 mirage-maintenance/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
