import aoc_201520_utilities as aoc_util
import itertools
import math


def get_elves(presents) -> list[int]:
    elves = []
    for i in range(1, int(math.sqrt(presents)) + 1):
        if presents % i == 0:
            elves.append(i)
            if i != presents // i:
                elves.append(presents // i)
    return elves


@aoc_util.timeit
def solve_a(input: int) -> str:
    answer = 0
    for house in itertools.count(start=1):
        presents = 0
        for elf in get_elves(house):
            presents += 10 * elf
        if presents >= input:
            answer = house
            break
    return str(answer)


@aoc_util.timeit
def solve_b(input: int) -> str:
    answer = 0
    for house in itertools.count(start=1):
        presents = 0
        for elf in get_elves(house):
            if house // elf <= 50:
                presents += 11 * elf
        if presents >= input:
            answer = house
            break
    return str(answer)


if __name__ == "__main__":
    answer_a = solve_a(29000000)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(29000000)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
