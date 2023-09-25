import pytest
import aoc_201602 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("ULL\nRRDDD\nLURDL\nUUUUD", "1985", None)]
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve_a(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("ULL\nRRDDD\nLURDL\nUUUUD", "5DB3", None)]
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve_b(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
