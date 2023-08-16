import pytest
import aoc_201505 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("ugknbfddgicrmopn", 1),
        ("aaa", 1),
        ("jchzalrnumimnmhp", 0),
        ("haegwjzuvuyypxyu", 0),
        ("dvszwmarrgswjxmb", 0),
    ],
)
def test_part1(puzzle_input, expected):
    assert aoc.part1(puzzle_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("qjhvhtzxzqqjkmpb", 1),
        ("xxyxx", 1),
        ("uurcxstgmygtbstg", 0),
        ("ieodomkazucvgmuy", 0),
    ],
)
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
