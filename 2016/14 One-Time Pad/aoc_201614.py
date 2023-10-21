import aoc_201614_utilities as aoc_util
from itertools import count
import hashlib


def get_md5_hex(value: str) -> str:
    encoded = value.encode()
    return hashlib.md5(encoded).hexdigest()


def get_triplet_char(hash: str) -> str:
    for a, b, c in zip(hash, hash[1:], hash[2:]):
        if a == b == c:
            return a
    return ""


@aoc_util.timeit
def solve(salt: str, is_b=False) -> str:
    keys = set()
    for index in count(start=0):
        candidate_key = get_md5_hex(salt + str(index))

        # if is_b:
        #     for _ in range(2016):
        #         candidate_key = get_md5_hex(candidate_key)

        char = get_triplet_char(candidate_key)
        if char:
            for step in range(1000):
                hash = get_md5_hex(salt + str(index + step + 1))
                if 5 * char in hash:
                    keys.add(index)
                    if len(keys) == 64:
                        return str(index)
    return str("")


if __name__ == "__main__":
    answer_a = solve("jlmsuwbz")
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    # Couldn't get this to work
    # answer_b = solve(aoc_util.PUZZLE.input_data, is_b=True)
    # print(f"Part b: {answer_b}")
    # aoc_util.send_answer(part="b", answer=answer_b)
