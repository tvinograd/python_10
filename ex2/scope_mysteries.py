#!/usr/bin/env python3
from typing import Callable


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


def scope_mysteries() -> None:
    initial_powers = [50, 55, 73]
    power_additions = [12, 16, 19, 12, 10]
    enchantment_types = ['Earthen', 'Shocking', 'Windy']
    items_to_enchant = ['Shield', 'Sword', 'Amulet', 'Armor']

    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

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
    vault['store']('fireball', 'Fireball hits target')
    vault['store']('heal', 'Heals target')
    print(f"fireball: {vault['recall']('fireball')}")
    print(f"heal: {vault['recall']('heal')}")
    print(f"snowball: {vault['recall']('snowball')}")


if __name__ == "__main__":
    scope_mysteries()
