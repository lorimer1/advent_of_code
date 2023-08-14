import pytest
import aoc_201503 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)]
)
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected", [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)]
)
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
