import pytest
import aoc_yyyymm as aoc


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
