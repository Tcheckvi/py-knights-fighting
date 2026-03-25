# app/main.py

from typing import Dict


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            },
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {
            "name": "Sword",
            "power": 45,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def _prepare_knight(knight: Dict) -> Dict:
    prepared = knight.copy()

    # protection
    prepared["protection"] = sum(
        armour["protection"] for armour in prepared["armour"]
    )

    # weapon
    prepared["power"] = prepared["power"] + prepared["weapon"]["power"]

    # potion
    potion = prepared.get("potion")
    if potion:
        effects = potion.get("effect", {})
        prepared["power"] += effects.get("power", 0)
        prepared["protection"] += effects.get("protection", 0)
        prepared["hp"] += effects.get("hp", 0)

    return prepared


def _fight(k1: Dict, k2: Dict) -> None:
    k1["hp"] -= k2["power"] - k1["protection"]
    k2["hp"] -= k1["power"] - k2["protection"]

    k1["hp"] = max(k1["hp"], 0)
    k2["hp"] = max(k2["hp"], 0)


def battle(knightsconfig: Dict) -> Dict:
    knights = {
        name: _prepare_knight(data)
        for name, data in knightsconfig.items()
    }

    _fight(knights["lancelot"], knights["mordred"])
    _fight(knights["arthur"], knights["red_knight"])

    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
