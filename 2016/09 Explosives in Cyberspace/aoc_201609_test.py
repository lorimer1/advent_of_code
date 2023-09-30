import pytest
import aoc_201609 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        ("ADVENT", "6", None),
        ("A(1x5)BC", "7", None),
        ("(3x3)XYZ", "9", None),
        ("A(2x2)BCD(2x2)EFG", "11", None),
        ("(6x1)(1x3)A", "6", None),
        ("X(8x2)(3x3)ABCY", "18", None),
    ],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve_a(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        ("(3x3)XYZ", "9", None),
        ("X(8x2)(3x3)ABCY", "20", None),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", "241920", None),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", "445", None),
    ],
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve_b(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
