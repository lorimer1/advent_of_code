import aoc_201523_utilities as aoc_util
from dataclasses import dataclass
from typing import NamedTuple
from operator import add, sub


OPERATORS = {"+": add, "-": sub}


class Instruction(NamedTuple):
    inst: str
    reg: str
    jmp: str


@dataclass
class Computer:
    pc: int
    a: int
    b: int
    prog: list[Instruction]


def jump(pc: int, jmp: str) -> int:
    return OPERATORS[jmp[0]](pc, int(jmp[1:]))


def parse_input(puzzle_input: str) -> Computer:
    prog = []
    for line in puzzle_input.splitlines():
        inst, operand = line[:3], line[4:]
        reg = ""
        jmp = ""
        if inst == "jmp":
            jmp = operand
        elif inst in ["jie", "jio"]:
            reg, jmp = operand.split(", ")
        else:
            reg = operand

        prog.append(Instruction(inst, reg, jmp))
    return Computer(pc=0, a=0, b=0, prog=prog)


@aoc_util.timeit
def solve_a(puzzle_input: str, is_b=False) -> str:
    c = parse_input(puzzle_input)
    c.a = 1 if is_b else 0
    while 0 <= c.pc < len(c.prog):
        code: Instruction = c.prog[c.pc]
        if code.inst == "hlf":
            c.a //= 2 if code.reg == "a" else 1
            c.b //= 2 if code.reg == "b" else 1
        elif code.inst == "tpl":
            c.a *= 3 if code.reg == "a" else 1
            c.b *= 2 if code.reg == "b" else 1
        elif code.inst == "inc":
            c.a += 1 if code.reg == "a" else 0
            c.b += 1 if code.reg == "b" else 0
        elif code.inst == "jmp":
            c.pc = jump(c.pc, code.jmp)
            continue
        elif code.inst == "jie":
            pc = c.pc
            c.pc = jump(c.pc, code.jmp) if code.reg == "a" and not c.a % 2 else c.pc
            c.pc = jump(c.pc, code.jmp) if code.reg == "b" and not c.b % 2 else c.pc
            if pc != c.pc:
                continue
        elif code.inst == "jio":
            pc = c.pc
            c.pc = jump(c.pc, code.jmp) if code.reg == "a" and c.a == 1 else c.pc
            c.pc = jump(c.pc, code.jmp) if code.reg == "b" and c.b == 1 else c.pc
            if pc != c.pc:
                continue
        else:
            raise ValueError("Invalid instruction")

        c.pc += 1
    return str(c.b)


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    return solve_a(puzzle_input, is_b=True)


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
