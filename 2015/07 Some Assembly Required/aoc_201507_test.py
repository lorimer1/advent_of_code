import pytest
import aoc_201507 as aoc


@pytest.mark.parametrize(
    "puzzle_input,wire, expected",
    [
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "d",
            72,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "e",
            507,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "f",
            492,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "g",
            114,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "h",
            65412,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "i",
            65079,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "x",
            123,
        ),
        (
            "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i",
            "y",
            456,
        ),
    ],
)
def test_part1(puzzle_input, wire, expected):
    assert aoc.part1(puzzle_input, wire) == expected


@pytest.mark.parametrize("puzzle_input,expected", [("", ""), ("", ""), ("", "")])
def test_part2(puzzle_input, expected):
    assert aoc.part2(puzzle_input) == expected
