import aoc_201522_utilities as aoc_util
from typing import NamedTuple
from dataclasses import dataclass
from typing import NamedTuple
from copy import deepcopy


class Spell(NamedTuple):
    name: str
    cost: int
    damage: int
    heal: int
    armour: int
    mana: int
    duration: int


SPELLS = [
    Spell(
        name="Magic Missile", cost=53, damage=4, heal=0, armour=0, mana=0, duration=0
    ),
    Spell(name="Drain", cost=73, damage=2, heal=2, armour=0, mana=0, duration=0),
    Spell(name="Shield", cost=113, damage=0, heal=0, armour=7, mana=0, duration=6),
    Spell(name="Poison", cost=173, damage=3, heal=0, armour=0, mana=0, duration=6),
    Spell(name="Recharge", cost=229, damage=0, heal=0, armour=0, mana=101, duration=5),
]


@dataclass
class ActiveSpell:
    spell: Spell
    duration: int


@dataclass
class Player:
    name: str
    damage: int
    hit_points: int
    armour: int
    mana: int
    active_spells: list
    spent_mana: int


@dataclass
class Game:
    player: Player
    boss: Player


def get_boss(puzzle_input: str) -> Player:
    value_gen = (int(line.split(": ")[1]) for line in puzzle_input.splitlines())
    hit_points = next(value_gen)
    damage = next(value_gen)
    return Player(
        "boss", damage, hit_points, armour=0, mana=0, active_spells=[], spent_mana=0
    )


def get_player() -> Player:
    return Player(
        "player",
        damage=0,
        hit_points=50,
        armour=0,
        mana=500,
        active_spells=[],
        spent_mana=0,
    )


def update_spell_states(player: Player):
    updated_spells = []
    active_spell: ActiveSpell
    for active_spell in player.active_spells:
        if active_spell.duration > 1:
            updated_spells.append(
                ActiveSpell(active_spell.spell, active_spell.duration - 1)
            )
    player.active_spells = updated_spells


def apply_effects(game: Game, attacker: Player):
    active_spell: ActiveSpell
    for active_spell in game.player.active_spells:
        game.boss.hit_points -= active_spell.spell.damage
        game.player.mana += active_spell.spell.mana
        game.player.hit_points += active_spell.spell.heal
        if active_spell.spell.armour > 0 and attacker is game.boss:
            game.player.hit_points += 7

    update_spell_states(game.player)


def ok_to_add_spell(spell: Spell, player: Player, min_cost: int):
    is_spell_used = False
    active_spell: ActiveSpell
    for active_spell in player.active_spells:
        if active_spell.spell.name == spell.name:
            is_spell_used = True
    if (
        spell.cost <= player.mana
        and player.spent_mana + spell.cost < min_cost
        and not is_spell_used
    ):
        return True
    return False


def play_games(puzzle_input: str, is_hard_mode: bool) -> str:
    games = [Game(get_player(), get_boss(puzzle_input))]
    min_cost = 9999
    while games:
        game = games.pop()
        game.player.hit_points -= 1 if is_hard_mode else 0
        if game.player.hit_points <= 0:
            continue

        apply_effects(game, attacker=game.player)
        if game.boss.hit_points <= 0:
            min_cost = min(min_cost, game.player.spent_mana)
            continue

        spell: Spell
        for spell in SPELLS:
            if ok_to_add_spell(spell, game.player, min_cost):
                new_game = deepcopy(game)
                new_game.player.mana -= spell.cost
                new_game.player.spent_mana += spell.cost
                new_game.player.active_spells.append(ActiveSpell(spell, spell.duration))
                apply_effects(new_game, attacker=new_game.boss)
                if new_game.boss.hit_points <= 0:
                    min_cost = min(min_cost, new_game.player.spent_mana)
                    continue
                new_game.player.hit_points -= new_game.boss.damage
                if new_game.player.hit_points > 0:
                    games.append(new_game)

    return str(min_cost)


@aoc_util.timeit
def solve_a(puzzle_input: str) -> str:
    return play_games(puzzle_input, is_hard_mode=False)


@aoc_util.timeit
def solve_b(puzzle_input: str) -> str:
    return play_games(puzzle_input, is_hard_mode=True)


if __name__ == "__main__":
    answer_a = solve_a(aoc_util.PUZZLE.input_data)
    print(f"Part a: {answer_a}")  # 953
    aoc_util.send_answer(part="a", answer=answer_a)

    answer_b = solve_b(aoc_util.PUZZLE.input_data)
    print(f"Part b: {answer_b}")  # 1289
    aoc_util.send_answer(part="b", answer=answer_b)
