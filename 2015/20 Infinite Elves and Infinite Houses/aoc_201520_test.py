import pytest
import aoc_201520 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (5, "1", ""),
        (25, "2", ""),
        (35, "3", ""),
        (65, "4", ""),
        (115, "6", ""),
        (145, "8", ""),
    ],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve_a(puzzle_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve_b(puzzle_input) == expected
