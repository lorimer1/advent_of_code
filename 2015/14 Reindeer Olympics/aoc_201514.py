import aoc_201514_utilities as aoc_util
from collections import namedtuple

# Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.

Deer = namedtuple("Deer", ["name", "speed", "on_time", "off_time"])


def parse(puzzle_input: str) -> list[str]:
    racers = dict()
    data = list()
    for line in puzzle_input.splitlines():
        tokens = line.split()
        racers[tokens[0]] = 0
        data.append(
            Deer(
                name=tokens[0],
                speed=int(tokens[3]),
                on_time=int(tokens[6]),
                off_time=int(tokens[-2]),
            )
        )
    return racers, data


def distance(deer: Deer, sec: int) -> int:
    cycles, remaining_sec = divmod(sec, deer.on_time + deer.off_time)
    return deer.speed * ((cycles * deer.on_time) + min(deer.on_time, remaining_sec))


def solve(puzzle_input: str, time: int, is_b=False):
    racers, data = parse(puzzle_input)
    if not is_b:
        return max((distance(deer, time) for deer in data))
    for sec in range(1, time + 1):
        deer_distances = {deer.name: distance(deer, sec) for deer in data}
        max_distance = max(deer_distances.values())
        for name, dist in deer_distances.items():
            if dist == max_distance:
                racers[name] += 1
    return max(racers.values())


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data, time=2503)  # 2696
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(input_data, time=2503, is_b=True)  # 1084
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
