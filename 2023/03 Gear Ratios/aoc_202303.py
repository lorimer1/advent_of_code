import aoc_202303_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Input:
    puzzle_input: str
    grid: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.grid = self.puzzle_input.splitlines()


def get_sym_part_coords(
    grid: list[str], r_idx: int, c_idx: int
) -> set[tuple[int, int]]:
    sym_part_coords = set()
    # symbol found, test coords around symbol for digit
    for test_r_idx in range(r_idx - 1, r_idx + 2):
        for test_c_idx in range(c_idx - 1, c_idx + 2):
            if (
                test_r_idx < 0
                or test_r_idx >= len(grid)
                or test_c_idx < 0
                or test_c_idx >= len(grid[test_r_idx])
                or not grid[test_r_idx][test_c_idx].isdigit()
            ):
                continue
            # digit found, test for beginning of number and store it's coord
            while test_c_idx > 0 and grid[test_r_idx][test_c_idx - 1].isdigit():
                test_c_idx -= 1
            sym_part_coords.add((test_r_idx, test_c_idx))
    return sym_part_coords


def get_all_part_coords(grid: list[str]) -> set[tuple[int, int]]:
    part_coords = set()
    for r_idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            sym_part_coords = get_sym_part_coords(grid, r_idx, c_idx)
            part_coords.update(sym_part_coords)
    return part_coords


def get_part_nums(grid: list[str], num_coords: set[tuple[int, int]]) -> list[int]:
    part_nums = []
    for r_idx, c_idx in num_coords:
        s = ""
        while c_idx < len(grid[r_idx]) and grid[r_idx][c_idx].isdigit():
            s += grid[r_idx][c_idx]
            c_idx += 1
        part_nums.append(int(s))
    return part_nums


def get_gear_ratios(grid: list[str]) -> list[int]:
    gear_ratios = []
    for r_idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char != "*":
                continue
            sym_part_coords = get_sym_part_coords(grid, r_idx, c_idx)
            if len(sym_part_coords) == 2:
                sym_part_nums = get_part_nums(grid, sym_part_coords)
                gear_ratios.append(sym_part_nums[0] * sym_part_nums[1])
    return gear_ratios


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    input = Input(puzzle_input)
    if not is_b:
        part_coords = get_all_part_coords(input.grid)
        part_nums = get_part_nums(input.grid, part_coords)
        return str(sum(part_nums))
    return str(sum(get_gear_ratios(input.grid)))


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
