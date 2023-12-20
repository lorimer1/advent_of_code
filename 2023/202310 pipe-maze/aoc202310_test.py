import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [(".....\n.S-7.\n.|.|.\n.L-J.\n.....", "4", None)],
)
def test_202310_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [(".....\n.S-7.\n.|.|.\n.L-J.\n.....", "1", None)],
)
def test_202310_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
