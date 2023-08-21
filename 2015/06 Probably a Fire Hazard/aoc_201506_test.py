import pytest
import aoc_201506 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("turn on 0,0 through 999,999", 1000000),
        ("toggle 0,0 through 999,0", 1000),
        ("turn off 499,499 through 500,500", 0),
    ],
)
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [("turn on 0,0 through 0,0", 1), ("toggle 0,0 through 999,999", 2000000)],
)
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
