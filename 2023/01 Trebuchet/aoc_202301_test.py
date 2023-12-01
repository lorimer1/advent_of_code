import pytest
import aoc_202301 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet", "142", None)],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen",
            "281",
            None,
        )
    ],
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, is_b=True) == expected
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
