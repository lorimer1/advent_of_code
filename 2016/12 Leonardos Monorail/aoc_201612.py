import aoc_201612_utilities as aoc_util
from dataclasses import dataclass, field


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


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    computer = Computer()
    computer.regs["c"] = 1 if is_b else 0
    computer.load_prog_from_assembly(code=puzzle_input)
    computer.run()
    return str(computer.regs["a"])


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
