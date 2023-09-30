import pytest
import aoc_201608 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1",
            "6",
            "im=7x3",
        )
    ],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve_a(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve_b(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
