import pytest
import aoc_201601 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [("R2, L3", "5", None), ("R2, R2, R2", "2", None), ("R5, L5, R5, R3", "12", None)],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve_a(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize("puzzle_input,expected,extra", [("R8, R4, R4, R8", "4", None)])
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve_b(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
