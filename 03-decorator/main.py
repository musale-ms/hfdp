"""
Decorator pattern: attaches additional responsibilites to an object dynamically.
"""

from abc import abstractmethod, ABC
from enum import Enum
from typing import Literal


class Size(Enum):
    """
    Coffee sizes.
    """

    small = "tall"
    medium = "grande"
    large = "venti"


CupSize = Literal[Size.small, Size.medium, Size.large]


class Beverage(ABC):
    """
    The abstract component.
    """

    description: str
    size: Size

    def get_description(self) -> str:
        return self.description

    def set_size(self, size: Literal[Size.small, Size.medium, Size.large]) -> None:
        self.size = size

    def get_size(self) -> Size:
        return self.size

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class CondimentDecorator(Beverage):
    """
    The abstract condiment decorator.
    """

    beverage: Beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class Espresso(Beverage):
    """
    Concrete component Espresso.
    """

    size_costs = {Size.small: 0.10, Size.medium: 0.15, Size.large: 0.20}

    def __init__(self, size: CupSize) -> None:
        self.description = "Espresso"
        self.size = size

    def cost(self) -> float:
        cup_cost: float = self.size_costs.get(self.get_size(), 0.0)
        return 1.99 + cup_cost


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    def __init__(self) -> None:
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05


class Mocha(CondimentDecorator):
    """
    Mocha condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    """
    Soy condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    """
    Whip condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10


if __name__ == "__main__":
    # Espresso with no condiments
    beverage: Beverage = Espresso(size=Size.small)
    print(f"{beverage.get_description()} ${beverage.cost()}")

    # Double mocha soy latte with whip
    # Combine HouseBlend, Soy, 2 shots of Mocha and Whip
    beverage_2: Beverage = HouseBlend()
    beverage_2 = Soy(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    print(f"{beverage_2.get_description()} ${beverage_2.cost()}")

    small: Size = Size.small

    print(small)
