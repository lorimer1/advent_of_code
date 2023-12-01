import aocd.models
from functools import wraps
import os
import time
from dataclasses import dataclass, field
import hashlib
import math
from operator import add, sub
from collections import defaultdict, deque

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
OPERATORS = {"+": add, "-": sub}


@dataclass
class Instruction:
    op: str  # Opcode
    ops: list[str] = field(default_factory=list)  # Operands


@dataclass
class Computer:
    pc: int = 0
    regs: dict[str, int] = field(default_factory=dict)
    prog: list[Instruction] = field(default_factory=list)

    def __post_init__(self):
        self.regs = {"a": 0, "b": 0, "c": 0, "d": 0}

    def load_prog_from_assembly(self, code: str):
        for line in code.splitlines():
            tokens = line.split(" ")
            op_2 = tokens[2] if len(tokens) == 3 else ""
            self.prog.append(Instruction(op=tokens[0], ops=[tokens[1], op_2]))

    def run(self):
        while 0 <= self.pc < len(self.prog):
            self.execute_instruction(self.prog[self.pc])

    def execute_instruction(self, instruction: Instruction):
        do_inst = getattr(self, instruction.op, None)
        if do_inst:
            do_inst(instruction.ops)
        else:
            raise ValueError("invalid opcode")

        if instruction.op in ["cpy", "inc", "dec"]:
            self.pc += 1

    def cpy(self, ops: list[str]):
        self.regs[ops[1]] = (
            int(self.regs[ops[0]]) if ops[0] in self.regs else int(ops[0])
        )

    def dec(self, ops: list[str]):
        self.regs[ops[0]] -= 1

    def inc(self, ops: list[str]):
        self.regs[ops[0]] += 1

    def jnz(self, ops: list[str]):
        self.pc += (
            int(ops[1])
            if (int(self.regs[ops[0]]) if ops[0] in self.regs else int(ops[0]))
            else 1
        )


@dataclass
class Maze:
    loc: complex = 0  # current location: real = col, imag = row
    dir: complex = 0  # current direction: real = left or right, imag = up or down
    grid: defaultdict[complex, str] = field(
        default_factory=lambda: defaultdict(str)
    )  # use get_grid_as_point_dict()

    WALL: str = "#"  # structure
    OPEN: str = "."  # not a structure
    PATH: str = "O"  # part of path
    DIR: dict[str, complex] = field(default_factory=dict)  # directions: L, R, U, D
    TURN: dict[str, complex] = field(default_factory=dict)  # turns: L, R

    def __post_init__(self):
        self.DIR = {"L": -1, "R": 1, "U": -1j, "D": +1j}
        self.TURN = {"L": 1j, "R": -1j}

    def manhattan_dist(self):
        """manhattan distance from 0 + 0j"""
        return int(abs(self.loc.real) + abs(self.loc.imag))

    def move(self, steps: int = 1):
        """move n steps in current direction"""
        self.loc += steps * self.dir

    def turn_lr(self, lr: str):
        """change direction by 90 degrees left or right"""
        self.dir *= self.TURN[lr]

    def set_dir(self, dir: str):
        """set the current direction"""
        self.dir = self.DIR[dir]

    def max_row_idex(self) -> int:
        """get the grid maximum row index"""
        row_indexes = [int(loc.imag) for loc in self.grid.keys()]
        return max(row_indexes)

    def max_col_idex(self) -> int:
        """get the grid maximum col index"""
        col_indexes = [int(loc.real) for loc in self.grid.keys()]
        return max(col_indexes)

    def set_grid(self, grid: list[list[str]]):
        """create grid from a list representation of a grid"""
        self.grid = defaultdict(str)
        for r, row in enumerate(grid):
            for c, point_value in enumerate(row):
                point = complex(real=c, imag=r)
                self.grid[point] = point_value

    def get_printable(self, path: set[complex] = set()):
        """get a printable version of the grid"""
        result = []
        for row in range(self.max_row_idex() + 1):
            row_str = ""
            for col in range(self.max_col_idex() + 1):
                loc = complex(real=col, imag=row)
                val = self.PATH if loc in path else self.grid[loc]
                row_str += val if val else " "
            result.append(row_str)
        return "\n".join(result)

    def val_at_loc(self, loc: complex):
        if not loc in self.grid.keys():
            raise ValueError(f"Location {loc} is not in grid")
        return self.grid[loc]


def alphabet_circle(char: str, steps: int) -> str:
    index = ALPHABET.index(char)
    return ALPHABET[(index + steps) % 26]


def get_factors(number: int) -> list[int]:
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return factors


def get_md5_hex(value: str) -> str:
    encoded = value.encode()
    return hashlib.md5(encoded).hexdigest()


def is_triangle(sides: list[int]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c


def transpose(array: list[list]) -> list[list]:
    return [list(x) for x in zip(*array)]


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__}: {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def file_name() -> str:
    return __file__.split(os.path.sep)[-1]


def aoc_year_from_path() -> int:
    return int(file_name()[4:8])


def aoc_day_from_path() -> int:
    return int(file_name()[8:10])


def print_test_info():
    test_data: dict[str, list[tuple[str, str, str]]]
    example: aocd.models.examples.Example

    test_data = {"a": [], "b": []}
    for example in PUZZLE.examples:
        part = "b" if example.answer_a is None else "a"
        answer = getattr(example, f"answer_{part}")
        test_data[part].append((example.input_data, answer, example.extra))
    print(test_data)


def send_answer(part: str, answer: str):
    answered = getattr(PUZZLE, f"answered_{part}")
    if not answered:
        if part == "a":
            PUZZLE.answer_a = answer
        else:
            PUZZLE.answer_b = answer


PUZZLE = aocd.models.Puzzle(year=aoc_year_from_path(), day=aoc_day_from_path())


if __name__ == "__main__":
    print_test_info()
