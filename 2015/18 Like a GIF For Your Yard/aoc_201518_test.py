import pytest
import aoc_201518 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", "11", "iterations=1"),
        ("..##..\n..##.#\n...##.\n......\n#.....\n#.##..", "8", "iterations=1"),
        ("..###.\n......\n..###.\n......\n.#....\n.#....", "4", "iterations=1"),
        ("...#..\n......\n...#..\n..##..\n......\n......", "4", "iterations=1"),
        (".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", "4", "iterations=4"),
    ],
)
def test_part1(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, int(extra.split("=")[1])) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected,extra",
    [
        (".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", "17", "iterations=5"),
    ],
)
def test_part2(puzzle_input, expected, extra):
    assert aoc.solve(puzzle_input, int(extra.split("=")[1]), is_b=True) == expected
