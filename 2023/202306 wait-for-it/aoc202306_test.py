import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [("Time:      7  15   30\nDistance:  9  40  200", "288", None)],
)
def test_202306_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [("Time:      7  15   30\nDistance:  9  40  200", "71503", None)],
)
def test_202306_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
