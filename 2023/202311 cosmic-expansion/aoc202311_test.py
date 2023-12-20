import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [('...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....', '374', None)],
)
def test_202311_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [('...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....', '374', None)],
)
def test_202311_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
