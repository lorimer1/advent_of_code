import utils
from functools import reduce


def get_win_count(time, distance) -> int:
    count = 0
    for charge_time in range(time):
        my_distance = (time - charge_time) * charge_time
        count += 1 if my_distance > distance else 0
    return count


@utils.timeit
def solve(input: str) -> int:
    times, distances = [
        list(map(int, row.split(":")[1].strip().split())) for row in input.splitlines()
    ]
    counts = [get_win_count(times[race], distances[race]) for race in range(len(times))]
    return reduce(lambda x, y: x * y, counts)


if __name__ == "__main__":
    with open("2023/202306 wait-for-it/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
