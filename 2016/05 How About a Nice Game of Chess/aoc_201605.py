import aoc_201605_utilities as aoc_util
from itertools import count
import hashlib


def get_md5_hex(value: str) -> str:
    encoded = value.encode()
    return hashlib.md5(encoded).hexdigest()


@aoc_util.timeit
def solve_a(input: str) -> str:
    password = ""
    for index in count():
        md5_hex = get_md5_hex(input + str(index))
        if md5_hex.startswith("00000"):
            password += md5_hex[5]
        if len(password) == 8:
            break
    return password


@aoc_util.timeit
def solve_b(input: str) -> str:
    password = ""
    password_chars = [""] * 8
    for index in count():
        md5_hex = get_md5_hex(input + str(index))
        if md5_hex.startswith("00000"):
            position = md5_hex[5]
            if position in "01234567" and not password_chars[int(position)]:
                password_chars[int(position)] = md5_hex[6]
                password = "".join(password_chars)
        if len(password) == 8:
            break
    return password


if __name__ == "__main__":
    answer_a = solve_a("ugkcyxxp")
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
