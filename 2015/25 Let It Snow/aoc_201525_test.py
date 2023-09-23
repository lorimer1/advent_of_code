import pytest
import aoc_201525 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 1.",
            "20151125",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 2.",
            "18749137",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 3.",
            "17289845",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 4.",
            "30943339",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 5.",
            "10071777",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 6.",
            "33511524",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 1.",
            "31916031",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 2.",
            "21629792",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 3.",
            "16929656",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 4.",
            "7726640",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 5.",
            "15514188",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 2, column 6.",
            "4041754",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 1.",
            "16080970",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 2.",
            "8057251",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 3.",
            "1601130",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 4.",
            "7981243",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 5.",
            "11661866",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 3, column 6.",
            "16474243",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 1.",
            "24592653",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 2.",
            "32451966",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 3.",
            "21345942",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 4.",
            "9380097",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 5.",
            "10600672",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 4, column 6.",
            "31527494",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 1.",
            "77061",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 2.",
            "17552253",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 3.",
            "28094349",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 4.",
            "6899651",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 5.",
            "9250759",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 5, column 6.",
            "31663883",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 1.",
            "33071741",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 2.",
            "6796745",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 3.",
            "25397450",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 4.",
            "24659492",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 5.",
            "1534922",
            None,
        ),
        (
            "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 6.",
            "27995004",
            None,
        ),
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
