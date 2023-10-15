import pytest
import aoc_201613 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [([10, 1 + 1j, 7 + 4j], "11", None)]
)
def test_part_a(puzzle_input, expected, extra):
    assert (
        aoc.solve(
            puzzle_input=puzzle_input[0], start=puzzle_input[1], target=puzzle_input[2]
        )
        == expected
    )
    # assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra", [([10, 1 + 1j, 7 + 4j], "11", None)]
)
def test_part_b(puzzle_input, expected, extra):
    assert (
        aoc.solve(
            puzzle_input=puzzle_input[0],
            start=puzzle_input[1],
            target=puzzle_input[2],
            is_b=True,
        )
        == expected
    )
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
