import pytest
import aoc_201616 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [("110010110100", "100", "disk_length=12"), ("10000", "01100", "disk_length=20")],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, disk_length=int(extra.split("=")[-1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [("", "", ""), ("", "", ""), ("", "", "")]
)
def test_part_b(puzzle_input, expected, extra):
    assert (
        aoc.solve(puzzle_input, disk_length=int(extra.split("=")[-1]), is_b=True)
        == expected
    )
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
