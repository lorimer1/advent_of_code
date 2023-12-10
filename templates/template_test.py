import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    $test_1,
)
def test_$year_day_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    $test_2,
)
def test_$year_day_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
