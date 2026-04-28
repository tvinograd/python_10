#!/usr/bin/env python3

import time
from functools import wraps
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Wrapper docstring"""
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator that validates power levels."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def main() -> None:
    # Master's Tower Test Data
    test_powers = [5, 13, 8, 11]
    spell_names = ['tsunami', 'heal', 'fireball', 'darkness']
    mage_names = ['Alex', 'Nova', 'Phoenix', 'Rowan', 'River', 'Morgan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    # Spell timer
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        """Fireball docstring"""
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting @wraps by commenting it in/out:")
    print("fireball.__name__: ", fireball.__name__)
    print("fireball.__doc__: ", fireball.__doc__)

    # Power validator
    print("\nTesting power validator...")

    @power_validator(10)
    def lightning(power: int) -> str:
        return f"Successfully cast {lightning.__name__} with {power} power"

    for n in test_powers:
        print(f"{n} - {lightning(n)}")

    # Spell retry
    print("\nTesting retrying spell...")
    attempts = 0

    @retry_spell(3)
    def retry() -> str:
        nonlocal attempts
        attempts += 1
        if attempts <= 3:
            raise ValueError()
        return "Waaaaaaagh spelled !"

    print(retry())

    # MageGuild class
    print("\nTesting MageGuild...")
    for name in mage_names:
        print(f"{name} - {MageGuild.validate_mage_name(name)}")
    print()
    for name in invalid_names:
        print(f"{name} - {MageGuild.validate_mage_name(name)}")
    print()

    guild = MageGuild()
    for n in test_powers:
        print(guild.cast_spell(spell_names[0], n))


if __name__ == "__main__":
    main()
