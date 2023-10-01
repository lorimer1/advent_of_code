import aoc_201610_utilities as aoc_util
from dataclasses import dataclass, field


@dataclass
class Input:
    puzzle_input: str
    instructions: list[str] = field(default_factory=list)

    def __post_init__(self):
        """parse the puzzle input"""
        self.instructions = [line for line in self.puzzle_input.splitlines()]


@dataclass
class Bot:
    low_out_type: str
    low_out_val: int
    high_out_type: str
    high_out_val: int
    current_chips: list[int] = field(default_factory=list)


@dataclass
class Factory:
    bots: dict[int, Bot] = field(default_factory=dict)
    outputs: dict[int, list[int]] = field(default_factory=dict)


def create_factory(instructions: list[str]) -> Factory:
    factory = Factory()

    for instruction in instructions:
        if instruction.startswith("bot"):
            tokens = instruction.split()
            bot = Bot(
                low_out_type=tokens[5],
                low_out_val=int(tokens[6]),
                high_out_type=tokens[-2],
                high_out_val=int(tokens[-1]),
            )
            factory.bots[int(tokens[1])] = bot
            if bot.low_out_type == "output":
                factory.outputs[bot.low_out_val] = []
            if bot.high_out_type == "output":
                factory.outputs[bot.high_out_val] = []

    for instruction in instructions:
        if instruction.startswith("value"):
            _, val, _, _, _, bot = instruction.split()
            factory.bots[int(bot)].current_chips.append(int(val))
    return factory


def get_bots_to_unload(factory: Factory) -> list[int]:
    return [
        bot_num for bot_num, bot in factory.bots.items() if len(bot.current_chips) == 2
    ]


def get_chips_to_compare(chips: str) -> list[int]:
    chips_to_compare = []
    tokens = chips.split(",")
    for token in tokens:
        chips_to_compare.append(int(token.split("-")[1]))
    return chips_to_compare


@aoc_util.timeit
def solve(puzzle_input: str, chips: str, is_b: bool = False) -> str:
    input = Input(puzzle_input)
    factory = create_factory(input.instructions)
    chips_to_compare = get_chips_to_compare(chips)

    bots_to_unload = get_bots_to_unload(factory)

    while bots_to_unload:
        bot: Bot
        for bot_num in bots_to_unload:
            bot = factory.bots[bot_num]
            if len(bot.current_chips) == 2:
                if (
                    not is_b
                    and chips_to_compare[0] in bot.current_chips
                    and chips_to_compare[1] in bot.current_chips
                ):
                    return str(bot_num)
                bot.current_chips.sort()
                if bot.low_out_type == "bot":
                    factory.bots[bot.low_out_val].current_chips.append(
                        bot.current_chips.pop(0)
                    )
                else:
                    factory.outputs[bot.low_out_val].append(bot.current_chips.pop(0))
                if bot.high_out_type == "bot":
                    factory.bots[bot.high_out_val].current_chips.append(
                        bot.current_chips.pop(0)
                    )
                else:
                    factory.outputs[bot.high_out_val].append(bot.current_chips.pop(0))
        bots_to_unload = get_bots_to_unload(factory)

    return str(factory.outputs[0][0] * factory.outputs[1][0] * factory.outputs[2][0])


if __name__ == "__main__":
    answer_a = solve(aoc_util.PUZZLE.input_data, chips="chips=value-61,value-17")
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(
        aoc_util.PUZZLE.input_data, chips="chips=value-61,value-17", is_b=True
    )
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
