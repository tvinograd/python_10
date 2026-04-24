#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: str) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    # Memory Depths Test Data
    initial_powers = [50, 55, 73]
    power_additions = [12, 16, 19, 12, 10]
    enchantment_types = ['Earthen', 'Shocking', 'Windy']
    items_to_enchant = ['Shield', 'Sword', 'Amulet', 'Armor']

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(initial_powers[0])
    print(f"Starting power: {initial_powers[0]}")
    for addition in power_additions:
        print(f"+ {addition} = {accumulator(addition)}")

    print("\nTesting enchantment factory...")
    enchantment = enchantment_factory(enchantment_types[0])
    for item in items_to_enchant:
        print(f"{enchantment(item)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret'= 42")
    vault['store']('secret', '42')
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
