import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [('1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet', '142', None)],
)
def test_202301_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [('1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet', '142', None)],
)
def test_202301_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
