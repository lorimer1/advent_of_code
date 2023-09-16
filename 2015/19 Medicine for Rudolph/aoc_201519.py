import aoc_201519_utilities as aoc_util
from collections import defaultdict
from typing import NamedTuple


class Input(NamedTuple):
    molecule: str
    replacements: defaultdict[str, list[str]]


def parse_input(puzzle_input: str) -> Input:
    equations, molecule = puzzle_input.split("\n\n")
    return Input(molecule=molecule, replacements=parse_equations(equations))


def parse_equations(equations: str) -> defaultdict[str, list[str]]:
    replacements = defaultdict(list)
    for equation in equations.splitlines():
        key, val = equation.split(" => ")
        replacements[key].append(val)
    return replacements


def get_alternatives(input: Input, replacements: list[str], element: str) -> list[str]:
    alternatives = []
    for replacement in replacements:
        start = 0
        while start < len(input.molecule):
            index = input.molecule.find(element, start)
            if index == -1:
                break
            alternatives.append(
                input.molecule[:index]
                + replacement
                + input.molecule[index + len(element) :]
            )
            start = index + 1
    return alternatives


@aoc_util.timeit
def solve(puzzle_input: str, is_b: bool = False) -> str:
    input: Input = parse_input(puzzle_input)
    molecules: set[str] = set()
    for element, replacements in input.replacements.items():
        alternative_molecules = get_alternatives(input, replacements, element)
        for alternative_molecule in alternative_molecules:
            molecules.add(alternative_molecule)
    return str(len(molecules))


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    input: Input = parse_input(puzzle_input)
    elements = sum(c.isupper() for c in input.molecule)
    rn = input.molecule.count("Rn")
    y = input.molecule.count("Y")
    return str(elements - 2 * rn - 2 * y - 1)


if __name__ == "__main__":
    part1 = solve(aoc_util.PUZZLE.input_data)
    print(f"Part 1: {part1}")
    if not aoc_util.PUZZLE.answered_a:
        aoc_util.PUZZLE.answer_a = part1

    part2 = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part 2: {part2}")
    if not aoc_util.PUZZLE.answered_b:
        aoc_util.PUZZLE.answer_b = part2
