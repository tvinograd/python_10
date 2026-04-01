#!/usr/bin/env python3
from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args, **kwargs) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier
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
