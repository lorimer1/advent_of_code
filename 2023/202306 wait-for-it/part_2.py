import utils


def get_win_count(time, distance) -> int:
    count = 0
    for charge_time in range(time):
        my_distance = (time - charge_time) * charge_time
        count += 1 if my_distance > distance else 0
    return count


@utils.timeit
def solve(input: str) -> int:
    times, distances = [row.split(":")[1].strip().split() for row in input.splitlines()]
    time = int("".join(times))
    distance = int("".join(distances))
    return get_win_count(time, distance)


if __name__ == "__main__":
    with open("2023/202306 wait-for-it/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
