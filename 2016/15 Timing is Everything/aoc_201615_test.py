import pytest
import aoc_201615 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "Disc #1 has 5 positions; at time=0, it is at position 4.\nDisc #2 has 2 positions; at time=0, it is at position 1.",
            "5",
            None,
        )
    ],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, is_b=True) == expected
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
