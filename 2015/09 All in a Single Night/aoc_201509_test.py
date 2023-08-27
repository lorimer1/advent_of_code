import pytest
import aoc_201509 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [("London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141", 605)],
)
def test_part1(puzzle_input, expected):
    assert aoc.solve(puzzle_input, min) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.solve(puzzle_input, max) == expected
