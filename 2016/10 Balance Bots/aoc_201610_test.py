import pytest
import aoc_201610 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2",
            "2",
            "chips=value-5,value-2",
        )
    ],
)
def test_part_a(puzzle_input, expected, extra):
    # assert aoc.solve_a(puzzle_input) == expected
    assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2",
            "30",
            "chips=value-5,value-2",
        )
    ],
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, extra, is_b=True) == expected
