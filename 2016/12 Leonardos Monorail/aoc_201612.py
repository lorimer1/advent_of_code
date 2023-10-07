import aoc_201612_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Instruction:
    opcode: str
    operands: list[str] = field(default_factory=list)


@dataclass
class Computer:
    counter: int = 0
    registers: dict[str, int] = field(default_factory=dict)
    program: list[Instruction] = field(default_factory=list)

    def __post_init__(self):
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}

    def load_program(self, assembly_code: str):
        for line in assembly_code.splitlines():
            tokens = line.split(" ")
            operand_2 = tokens[2] if len(tokens) == 3 else ""
            self.program.append(
                Instruction(opcode=tokens[0], operands=[tokens[1], operand_2])
            )

    def execute_instruction(self):
        instruction: Instruction = self.program[self.counter]
        if instruction.opcode == "cpy":
            self.registers[instruction.operands[1]] = (
                int(self.registers[instruction.operands[0]])
                if instruction.operands[0] in self.registers
                else int(instruction.operands[0])
            )
            self.counter += 1
        elif instruction.opcode == "inc":
            self.registers[instruction.operands[0]] += 1
            self.counter += 1
        elif instruction.opcode == "dec":
            self.registers[instruction.operands[0]] -= 1
            self.counter += 1
        elif instruction.opcode == "jnz":
            self.counter += (
                int(instruction.operands[1])
                if (
                    int(self.registers[instruction.operands[0]])
                    if instruction.operands[0] in self.registers
                    else int(instruction.operands[0])
                )
                else 1
            )
        else:
            raise ValueError("invalid opcode")

    def run(self):
        while 0 <= self.counter < len(self.program):
            self.execute_instruction()


@aoc_util.timeit
def solve(puzzle_input: str, is_b=False) -> str:
    computer = Computer()
    computer.registers["c"] = 1 if is_b else 0
    computer.load_program(assembly_code=puzzle_input)
    computer.run()
    return str(computer.registers["a"])


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
