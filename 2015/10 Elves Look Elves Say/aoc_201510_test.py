import pytest
import aoc_201510 as aoc


@pytest.mark.parametrize(
    "puzzle_input,iterations, expected",
    [
        ("1", 1, 2),
        ("11", 1, 2),
        ("21", 1, 4),
        ("1211", 1, 6),
        ("111221", 1, 6),
        ("1", 5, 6),
    ],
)
def test_part1(puzzle_input, iterations, expected):
    assert aoc.solve(puzzle_input, iterations) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.solve(puzzle_input) == expected
