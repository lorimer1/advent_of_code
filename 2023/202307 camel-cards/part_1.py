import utils

CARD_RANKS = "23456789TJQKA"

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def classify(hand: str) -> int:
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return FIVE_OF_A_KIND
    if 4 in counts:
        return FOUR_OF_A_KIND
    if 3 in counts:
        if 2 in counts:
            return FULL_HOUSE
        else:
            return THREE_OF_A_KIND
    if counts.count(2) == 4:
        return TWO_PAIR
    if 2 in counts:
        return ONE_PAIR
    return HIGH_CARD


def hand_sort_key(hand: str) -> tuple[int, list[int]]:
    return (classify(hand), [CARD_RANKS.index(card) for card in hand])


@utils.timeit
def solve(input: str) -> int:
    hands = [
        (hand, int(bid)) for line in input.splitlines() for hand, bid in [line.split()]
    ]
    hands.sort(key=lambda hand: hand_sort_key(hand[0]))
    return sum(idx * bid for idx, (_, bid) in enumerate(hands, 1))


if __name__ == "__main__":
    with open("2023/202307 camel-cards/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
