import pytest
import aoc_202302 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            "8",
            None,
        )
    ],
)
def test_part_a(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input) == expected
    # assert aoc.solve(puzzle_input, extra) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            "2286",
            None,
        )
    ],
)
def test_part_b(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, is_b=True) == expected
    # assert aoc.solve_b(puzzle_input, extra, is_b=True) == expected
