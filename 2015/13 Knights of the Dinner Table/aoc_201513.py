import aoc_201513_utilities as aoc_util
import itertools


def parse_line(line: str) -> tuple:
    tokens = line.split()
    multiplier: int = 1 if tokens[2] == "gain" else -1
    return tokens[0], tokens[-1][:-1], multiplier * int(tokens[3])


def parse(puzzle_input: str) -> dict:
    data = puzzle_input.splitlines()
    data = list(map(parse_line, data))
    pair_scores = dict()
    persons = set()
    for a, b, score in data:
        pair_scores[(a, b)] = score
        persons.add(a)
        persons.add(b)
    return pair_scores, persons


def solve(puzzle_input: str, is_b=False):
    pair_scores, persons = parse(puzzle_input)
    if is_b:
        for person in persons:
            pair_scores[("me", person)] = 0
            pair_scores[(person, "me")] = 0
        persons.add("me")

    table_scores = []
    for this_perm in itertools.permutations(persons):
        clockwise = list(this_perm)
        clockwise.append(
            clockwise[0]
        )  # last person is sitting next to first (circular table)
        this_score = 0
        # clockwise
        for pair in zip(clockwise, clockwise[1:]):
            this_score += pair_scores[pair]

        # anti-clockwise
        anti_clockwise = list(reversed(clockwise))
        for pair in zip(anti_clockwise, anti_clockwise[1:]):
            this_score += pair_scores[pair]

        table_scores.append(this_score)

    return max(table_scores)


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
