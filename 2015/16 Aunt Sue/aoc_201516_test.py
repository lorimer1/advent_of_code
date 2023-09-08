import pytest
import aoc_201516 as aoc


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part1(puzzle_input, expected):
    assert aoc.solve(puzzle_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.solve(puzzle_input) == expected
