import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [("0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45", "114", None)],
)
def test_202309_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [("0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45", "2", None)],
)
def test_202309_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
