import aoc_201510_utilities as aoc_util


def parse(puzzle_input: str) -> list[str]:
    data = list(map(int, puzzle_input))
    return data


def solve(puzzle_input: str, iterations: int = 1) -> str:
    data = parse(puzzle_input)
    for _ in range(iterations):
        current_digit = data[0]
        reps = 0
        new_data = []
        for digit in data:
            if digit == current_digit:
                reps += 1
            else:
                new_data.append(reps)
                new_data.append(current_digit)
                current_digit = digit
                reps = 1
        new_data.append(reps)
        new_data.append(current_digit)
        data = new_data

    return len(data)


if __name__ == "__main__":
    input_data = aoc_util.PUZZLE.input_data

    part1 = solve(input_data, iterations=40)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve(input_data, iterations=50)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
