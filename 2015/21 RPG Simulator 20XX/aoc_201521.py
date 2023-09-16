import aoc_201521_utilities as aoc_util
from typing import NamedTuple
from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Player:
    name: str
    armour: int
    damage: int
    hit_points: int
    cost: int


class Item(NamedTuple):
    name: str
    gold: int
    damage: int
    armour: int


class Shop(NamedTuple):
    weapons: list[Item]
    armour: list[Item]
    rings: list[Item]


def get_shop() -> Shop:
    weapons = [
        Item(name="Dagger", gold=8, damage=4, armour=0),
        Item(name="Shortsword", gold=10, damage=5, armour=0),
        Item(name="Warhammer", gold=25, damage=6, armour=0),
        Item(name="Longsword", gold=40, damage=7, armour=0),
        Item(name="Greataxe", gold=74, damage=8, armour=0),
    ]
    armor = [
        Item(name="none", gold=0, damage=0, armour=0),
        Item(name="Leather", gold=13, damage=0, armour=1),
        Item(name="Chainmail", gold=31, damage=0, armour=2),
        Item(name="Splintmail", gold=53, damage=0, armour=3),
        Item(name="Bandedmail", gold=75, damage=0, armour=4),
        Item(name="Platemail", gold=102, damage=0, armour=5),
    ]
    rings = [
        Item(name="none left hand", gold=0, damage=0, armour=0),
        Item(name="none right hand", gold=0, damage=0, armour=0),
        Item(name="Damage +1", gold=25, damage=1, armour=0),
        Item(name="Damage +2", gold=50, damage=2, armour=0),
        Item(name="Damage +3", gold=100, damage=3, armour=0),
        Item(name="Defense +1", gold=20, damage=0, armour=1),
        Item(name="Defense +2", gold=40, damage=0, armour=2),
        Item(name="Defense +3", gold=80, damage=0, armour=3),
    ]
    return Shop(weapons=weapons, armour=armor, rings=rings)


def get_boss(puzzle_input: str) -> Player:
    value_gen = (int(line.split(": ")[1]) for line in puzzle_input.splitlines())
    hit_points = next(value_gen)
    damage = next(value_gen)
    armour = next(value_gen)
    return Player("boss", armour, damage, hit_points, cost=0)


def get_player(weapon: Item, armour: Item, ring_1: Item, ring_2: Item) -> Player:
    player = Player("player", armour=0, damage=0, hit_points=100, cost=0)
    player.armour = weapon.armour + armour.armour + ring_1.armour + ring_2.armour
    player.damage = weapon.damage + armour.damage + ring_1.damage + ring_2.damage
    player.cost = weapon.gold + armour.gold + ring_1.gold + ring_2.gold
    return player


def play_game(player: Player, boss: Player) -> Player:
    attacker = player
    defender = boss
    while True:
        hit_points = attacker.damage - defender.armour
        defender.hit_points -= hit_points if hit_points > 0 else 1
        if defender.hit_points <= 0:
            break
        attacker, defender = defender, attacker
    return attacker


def shop_item_combinations():
    shop = get_shop()
    for weapon in shop.weapons:
        for armour in shop.armour:
            for ring_1 in shop.rings:
                for ring_2 in shop.rings:
                    if ring_1.name == ring_2.name:
                        continue
                    yield weapon, armour, ring_1, ring_2


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    min_cost: int = 9999
    for weapon, armour, ring_1, ring_2 in shop_item_combinations():
        boss = get_boss(puzzle_input)
        player = get_player(weapon, armour, ring_1, ring_2)
        winner = play_game(player, boss)
        if winner is player:
            min_cost = min(player.cost, min_cost)
    return str(min_cost)


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    max_cost: int = 0
    for weapon, armour, ring_1, ring_2 in shop_item_combinations():
        boss = get_boss(puzzle_input)
        player = get_player(weapon, armour, ring_1, ring_2)
        winner = play_game(player, boss)
        if winner is boss:
            max_cost = max(player.cost, max_cost)
    return str(max_cost)


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")
    aoc_util.send_answer(part="b", answer=answer_b)
