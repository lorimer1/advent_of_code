from aocd.models import Puzzle
from functools import lru_cache
from operator import and_, or_, lshift, rshift


def print_example_test_data(puzzle: Puzzle):
    if not puzzle.answered_a:
        print(
            [
                (example.input_data, int(example.answer_a))
                for example in puzzle.examples
                if not example.answer_a is None
            ]
        )
        return

    print(
        [
            (example.input_data, int(example.answer_b))
            for example in puzzle.examples
            if not example.answer_b is None
        ]
    )


def solve(puzzle: Puzzle, submit_a=False, submit_b=False):
    solution1 = part1(puzzle.input_data, "a")
    solution2 = part2(puzzle.input_data, "a", wire_b=str(solution1))

    print(solution1)
    print(solution2)

    if submit_a and not puzzle.answered_a:
        puzzle.answer_a = solution1
    if submit_b and not puzzle.answered_b:
        puzzle.answer_b = solution2


def parse(puzzle_input):
    result = {}
    for line in puzzle_input.splitlines():
        s = line.split(" -> ")
        result[s[1]] = s[0].split()
    return result


def solve_part(puzzle_input: str, wire: str, wire_b: str = None):
    wires = parse(puzzle_input)
    if wire_b:
        wires["b"] = [wire_b]

    gates = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}

    @lru_cache
    def get_wire_value(wire):
        try:
            return int(wire)
        except ValueError:
            gate_config = wires[wire]
            if len(gate_config) == 1:
                return get_wire_value(gate_config[0])
            elif len(gate_config) == 2:
                return ~get_wire_value(gate_config[1]) & 0xFFFF
            else:
                gate = gates[gate_config[1]]
                return gate(
                    get_wire_value(gate_config[0]), get_wire_value(gate_config[2])
                )

    return get_wire_value(wire)


def part1(puzzle_input: str, wire: str):
    return solve_part(puzzle_input, wire)


def part2(puzzle_input: str, wire: str, wire_b: str):
    return solve_part(puzzle_input, wire, wire_b)


if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(year=2015, day=7)
    # print_example_test_data(puzzle)
    solve(puzzle, submit_a=True, submit_b=True)
