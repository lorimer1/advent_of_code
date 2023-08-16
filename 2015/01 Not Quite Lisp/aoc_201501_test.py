import pytest
import aoc_201501 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [(")", 1), ("()())", 5)])
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
