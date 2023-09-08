import aoc_201517_utilities as aoc_util
from itertools import combinations


def parse(puzzle_input: str) -> list[int]:
    return [int(val) for val in puzzle_input.splitlines()]


def solve(puzzle_input: str, is_b: bool = False) -> int:
    data = parse(puzzle_input)
    container_counts = []
    combos = (com for sub in range(len(data)) for com in combinations(data, sub + 1))
    count_a = 0
    for combo in combos:
        if sum(combo) == 150:
            count_a += 1
            container_counts.append(len(combo))

    least = min(container_counts)
    count_b = len([count for count in container_counts if count == least])
    if is_b:
        return count_b
    return count_a


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(input_data, is_b=True)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
