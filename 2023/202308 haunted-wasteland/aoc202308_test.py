import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "input,expected,extra",
    [
        (
            "RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)",
            "2",
            None,
        )
    ],
)
def test_202308_part_1(input, expected, extra):
    assert part_1.solve(input) == int(expected)
    # assert part_1.solve(input, extra) == int(expected)


@pytest.mark.parametrize(
    "input,expected,extra",
    [
        (
            "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)",
            "6",
            None,
        )
    ],
)
def test_202308_part_2(input, expected, extra):
    assert part_2.solve(input) == int(expected)
    # assert part_2.solve(input, extra) == int(expected)
