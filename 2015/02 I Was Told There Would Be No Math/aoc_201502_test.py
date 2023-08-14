import pytest
import aoc_201502 as aoc


@pytest.mark.parametrize("puzzle_input,expected", [("2x3x4", 58), ("1x1x10", 43)])
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("2x3x4", 34), ("1x1x10", 14)])
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
