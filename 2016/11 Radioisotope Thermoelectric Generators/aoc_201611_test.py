import pytest
import aoc_201611 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            [2, 1, 1, 0],
            "9",  # note 11 was the answer in the aoc site example!
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
