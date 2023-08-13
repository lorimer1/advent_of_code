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
    """Test part 1 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.part1(parsed_input) == expected


@pytest.mark.parametrize("puzzle_input,expected", [(")", 1), ("()())", 5)])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.part2(parsed_input) == expected
