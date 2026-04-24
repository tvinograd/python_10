#!/usr/bin/env python3

import time
from functools import wraps
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
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
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def main() -> None:
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

    print("\nTesting power validator...")

    @power_validator(10)
    def lightning(power: int) -> str:
        return f"Successfully cast {lightning.__name__} with {power} power"

    print(lightning(15))
    print(lightning(5))


if __name__ == "__main__":
    main()
