import aoc_201611_utilities as aoc_util

items_part_one = [4, 2, 4, 0]  # items on each floor 1, 2, 3, 4
items_part_two = [8, 2, 4, 0]  # items on each floor 1, 2, 3, 4


def solve(items):
    """
    Through playing around with bolts and nuts,
    I came across the optimal strategy, move things up a floor at a time

    I also discovered to move n items up 1 floor,
        it requires 2 * (n - 1) - 1 moves

    So assuming a "good" start state, it doesn't matter what is on what floor
    Just the number of things per floor
    """
    moves = 0
    while items[-1] != sum(items):
        # print moves, items
        lowest_floor = 0
        while items[lowest_floor] == 0:
            lowest_floor += 1
        moves += 2 * (items[lowest_floor] - 1) - 1
        items[lowest_floor + 1] += items[lowest_floor]
        items[lowest_floor] = 0
    return str(moves)


if __name__ == "__main__":
    answer_a = solve(items_part_one)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve(items_part_two)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
