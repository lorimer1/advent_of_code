import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [("32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483", "6440", None)],
)
def test_202307_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [("32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483", "5905", None)],
)
def test_202307_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
