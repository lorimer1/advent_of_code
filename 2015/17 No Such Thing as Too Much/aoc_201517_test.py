import pytest
import aoc_201517 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("20\n15\n10\n5\n5", "4", "liters=25")]
)
def test_part1(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part2(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
