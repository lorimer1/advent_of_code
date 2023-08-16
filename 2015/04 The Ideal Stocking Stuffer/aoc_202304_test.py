import pytest
import aoc_202304 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected", [("abcdef", 609043), ("pqrstuv", 1048970)]
)
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected
