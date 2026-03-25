from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion
from typing import Dict


def create_knights() -> Dict:

    red_knight = Knight(
        name="Red Knight",
        hp=70,
        power=40,
        weapon=Weapon("Sword", 45),
        armour=[Armour("breastplate", 25)],
        potion=Potion("Blessing", {"hp": 10, "power": 5}),
    )

    x_knight = Knight(
        name="X Knight",
        hp=100,
        power=70,
        weapon=Weapon("Axe", 0),
        armour=[Armour("shield", 35)],
        potion=None,
    )

    return red_knight, x_knight
