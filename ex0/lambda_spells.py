#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Light Prism', 'power': 60, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 68, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 105, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 66, 'type': 'focus'}
    ]
    mages = [
        {'name': 'Ash', 'power': 50, 'element': 'light'},
        {'name': 'Casey', 'power': 56, 'element': 'light'},
        {'name': 'Jordan', 'power': 50, 'element': 'light'},
        {'name': 'Phoenix', 'power': 69, 'element': 'ice'},
        {'name': 'Morgan', 'power': 85, 'element': 'water'}
    ]
    spells = ['flash', 'tornado', 'blizzard', 'freeze']

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")

    print("\nTesting power filter (min_power = 55)...")
    filtered = power_filter(mages, 55)
    for mage in filtered:
        print(f"{mage['name']} ({mage['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(f"{spell}")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}\n")


if __name__ == "__main__":
    main()
