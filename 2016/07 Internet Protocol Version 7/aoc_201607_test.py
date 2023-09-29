import pytest
import aoc_201607 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        ("abba[mnop]qrst", "1", None),
        ("abcd[bddb]xyyx", "0", None),
        ("aaaa[qwer]tyui", "0", None),
        ("ioxxoj[asdfgh]zxcvbn", "1", None),
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
