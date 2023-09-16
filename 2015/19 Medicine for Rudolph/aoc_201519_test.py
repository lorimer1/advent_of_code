import pytest
import aoc_201519 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        ("H => HO\nH => OH\nO => HH\n\nHOH", "4", None),
        ("H => HO\nH => OH\nO => HH\n\nHOHOHO", "7", None),
    ],
)
def test_part1(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part2(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, is_b=True) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
