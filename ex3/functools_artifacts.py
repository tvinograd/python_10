#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{power} damage of {element} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "water": partial(base_enchantment, 50, "water"),
        "stone": partial(base_enchantment, 50, "stone"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def ft_dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @ft_dispatch.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @ft_dispatch.register(str)
    def _(spell: str) -> str:
        return spell

    @ft_dispatch.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return ft_dispatch


def main() -> None:
    # Ancient Library Test Data
    spell_powers = [50, 22, 40, 47, 38, 47]
    fibonacci_tests = [13, 11, 17]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    for enchanter in enchantments:
        print(enchantments[enchanter]("Goblin"))

    print("\nTesting memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(f"{dispatcher(3.14)}")


if __name__ == "__main__":
    main()
