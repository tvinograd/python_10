#!/usr/bin/env python3
from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combiner(*args: Any) -> tuple:
        return (spell1(*args), spell2(*args))
    return combiner


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args: Any) -> int:
        return base_spell(*args) * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args: Any) -> str:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args: Any) -> list:
        return [spell(*args) for spell in spells]
    return sequence


def higher_magic() -> None:
    test_values = [24, 23, 24]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(value: int) -> int:
        return value

    def is_good(target: str) -> bool:
        return target != 'Goblin'

    print("\nTesting spell combiner...")
    combiner = spell_combiner(fireball, heal)
    result = combiner(test_targets[0])
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(damage, 3)
    original = test_values[0]
    print(f"Original: {original}, Amplified: {amplifier(original)}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(is_good, heal)
    for target in test_targets[:2]:
        print(f"{target}: {caster(target)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    results = sequence(test_targets[0])
    for r in results:
        print(r)
    print()


if __name__ == "__main__":
    higher_magic()
