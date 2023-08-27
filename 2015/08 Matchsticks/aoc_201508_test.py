import pytest
import aoc_201508 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [(r'""', 2), (r'"abc"', 2), (r'"aaa\"aaa"', 3), (r'"\x27"', 5)],
)
def test_part1(puzzle_input, expected):
    assert aoc.solve1(puzzle_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.solve2(puzzle_input) == expected
