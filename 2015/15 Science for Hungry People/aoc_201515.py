import aoc_201515_utilities as aoc_util
from collections import namedtuple


def parse(puzzle_input: str) -> dict:
    ingredients = dict()
    for line in puzzle_input.splitlines():
        name, parts = line.split(": ")
        attributes = dict()
        for part in parts.split(", "):
            key, val = part.split(" ")
            attributes[key] = int(val)
        ingredients[name] = attributes
    return ingredients


def calc_attribute(
    ingredients: dict,
    attribute: str,
    sugar: int,
    sprinkles: int,
    candy: int,
    chocolate: int,
) -> int:
    return (
        sugar * ingredients["Sugar"][attribute]
        + sprinkles * ingredients["Sprinkles"][attribute]
        + candy * ingredients["Candy"][attribute]
        + chocolate * ingredients["Chocolate"][attribute]
    )


def calc_score(
    ingredients: dict, sugar: int, sprinkles: int, candy: int, chocolate: int
):
    attr_vals = {
        attribute: calc_attribute(
            ingredients, attribute, sugar, sprinkles, candy, chocolate
        )
        for attribute in ["capacity", "durability", "flavor", "texture", "calories"]
    }
    if min(attr_vals.values()) < 0:
        return 0, attr_vals["calories"]
    return (
        attr_vals["capacity"]
        * attr_vals["durability"]
        * attr_vals["flavor"]
        * attr_vals["texture"],
        attr_vals["calories"],
    )


def solve(puzzle_input: str, is_b: bool = False):
    ingredients = parse(puzzle_input)
    max_score = 0
    for sugar in range(100):
        for sprinkles in range(100 - sugar):
            for candy in range(100 - sugar - sprinkles):
                chocolate = 100 - sugar - sprinkles - candy
                score, calories = calc_score(
                    ingredients, sugar, sprinkles, candy, chocolate
                )
                if is_b and not calories == 500:
                    continue
                max_score = max(
                    max_score,
                    score,
                )

    return max_score


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
