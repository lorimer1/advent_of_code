import pytest
import aoc_201614 as aoc


@pytest.mark.parametrize("puzzle_input,expected,extra", [("abc", "22728", None)])
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize("puzzle_input,expected,extra", [("abc", "22551", None)])
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, is_b=True) == expected
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
