import aoc_201509_utilities as aoc_util
from itertools import permutations


def parse_line(line):
    a, _, b, _, dist = line.split()
    return a, b, int(dist)


def parse(puzzle_input: str) -> list:
    data = [parse_line(line) for line in puzzle_input.splitlines()]
    return data


def create_relations(data):
    locations = set()
    relations = dict()
    for a, b, dist in data:
        locations |= {a, b}
        relations[(a, b)] = dist
        relations[(b, a)] = dist
    return locations, relations


def solve(puzzle_input: str, func):
    data = parse(puzzle_input)
    locations, relations = create_relations(data)
    totals = []
    for route in permutations(locations):
        this_total = 0
        for trip in zip(route, route[1:]):
            this_total += relations[trip]
        totals.append(this_total)

    return func(totals)


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data, min)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(input_data, max)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
