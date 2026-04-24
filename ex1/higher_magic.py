#!/usr/bin/env python3

from typing import Any
from collections.abc import Callable


# Spells
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def condition(target: str, power: int) -> bool:
    return target != 'Goblin'


# Spell modificatons
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args, **kwargs) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
    # Higher Realm Test Data
    test_values = [22, 13, 10]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined(test_targets[0], test_values[0])
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(test_targets[0], test_values[0])}")
    print(f"Amplified: {mega_fireball(test_targets[0], test_values[0])}")

    print("\nTesting conditional caster...")
    safe_heal = conditional_caster(condition, heal)
    for target in test_targets:
        print(f"{target}: {safe_heal(target, test_values[0])}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for target in test_targets[:2]:
        results = sequence(target, test_values[0])
        for r in results:
            print(r)
    print()


if __name__ == "__main__":
    main()
